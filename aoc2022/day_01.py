from dataclasses import dataclass, field
from itertools import islice
from typing import List, Optional


@dataclass
class ElfInventory:
    carried_snacks_calories: List[int] = field(default_factory=list)

    def total_calories_carried(self) -> int:
        return sum(self.carried_snacks_calories)


def read_elf_inventory_file(file_path: str) -> List[ElfInventory]:
    current_elf_inventory: Optional[ElfInventory] = None
    result: List[ElfInventory] = []

    with open(file_path, "r") as file:
        for inventory_line in file:

            if inventory_line.isspace():
                if current_elf_inventory is not None:
                    result.append(current_elf_inventory)
                    current_elf_inventory = None
                    continue

            snack_calories = int(inventory_line)

            if current_elf_inventory is None:
                current_elf_inventory = ElfInventory([snack_calories])
            else:
                current_elf_inventory.carried_snacks_calories.append(snack_calories)

    return result


def part_one(elf_inventories: List[ElfInventory]) -> int:
    return max(inventory.total_calories_carried() for inventory in elf_inventories)


def part_two(elf_inventories: List[ElfInventory]) -> int:
    return sum(
        islice(
            sorted(
                [inventory.total_calories_carried() for inventory in elf_inventories],
                reverse=True,
            ),
            3,
        )
    )
