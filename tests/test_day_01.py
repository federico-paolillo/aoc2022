import unittest
from aoc2022.day_01 import ElfInventory, part_one, part_two, read_elf_inventory_file


class DayOneTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                ElfInventory([1000, 2000, 3000]),
                ElfInventory([4000]),
                ElfInventory([5000, 6000]),
                ElfInventory([7000, 8000, 9000]),
                ElfInventory([10000]),
            ]
        )

        self.assertEqual(result, 24000)

    def test_part_one_solves_real_input(self):
        inventories_from_file = read_elf_inventory_file("inputs/day_01.txt")
        result = part_one(inventories_from_file)
        self.assertEqual(result, 68467)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                ElfInventory([1000, 2000, 3000]),
                ElfInventory([4000]),
                ElfInventory([5000, 6000]),
                ElfInventory([7000, 8000, 9000]),
                ElfInventory([10000]),
            ]
        )

        self.assertEqual(result, 45000)

    def test_part_two_solves_real_input(self):
        inventories_from_file = read_elf_inventory_file("inputs/day_01.txt")
        result = part_two(inventories_from_file)
        self.assertEqual(result, 1)
