from dataclasses import dataclass
from functools import reduce
from typing import List, Tuple

lowercase_letters_priorities = {chr(x + 97): x + 1 for x in range(0, 26)}
uppercase_letters_priorities = {chr(x + 65): x + 27 for x in range(0, 26)}

priorities = (
    lowercase_letters_priorities | uppercase_letters_priorities
)  # Merge both priorities


def rucksack_line_compartments(items_line: str) -> Tuple[str, str]:
    rucksack_items_line_len = len(items_line)

    items_in_compartment_one = items_line[: rucksack_items_line_len // 2]
    items_in_compartment_two = items_line[rucksack_items_line_len // 2 :]

    return (items_in_compartment_one, items_in_compartment_two)


def find_misplaced_items(rucksack_line: str) -> List[str]:
    rucksack_compartments = rucksack_line_compartments(rucksack_line)

    compartment_one, compartment_two = rucksack_compartments

    compartment_one_items = set(compartment_one)
    compartment_two_items = set(compartment_two)

    return list(compartment_one_items & compartment_two_items)


def find_badge(group_of_rucksack_lines: List[str]) -> str:
    rucksack_items = (set(rucksack_line) for rucksack_line in group_of_rucksack_lines)

    possible_badges = reduce(
        lambda common_items, current_items: current_items
        if len(common_items) == 0
        else current_items & common_items,
        rucksack_items,
        set(),
    )

    return next(iter(list(possible_badges)), None)


def read_rucksacks_file(file_path: str) -> List[str]:
    result: List[str] = []

    with open(file_path, "r") as file:
        for items_line in file:
            if not items_line.isspace():
                result.append(items_line.strip())

    return result


def part_one(rucksack_lines: List[str]) -> int:
    misplaced_items_on_each_rucksack = (
        find_misplaced_items(rucksack_line) for rucksack_line in rucksack_lines
    )

    every_misplaced_item = (
        item_in_common
        for items_in_common in misplaced_items_on_each_rucksack
        for item_in_common in items_in_common
    )  # Ah, yes. flat() in Python

    return sum(priorities[misplaced_item] for misplaced_item in every_misplaced_item)


def part_two(rucksack_lines: List[str]) -> int:
    group_of_rucksacks = (
        rucksack_lines[i : i + 3] for i in range(0, len(rucksack_lines), 3)
    )

    badges = (find_badge(group) for group in group_of_rucksacks)

    return sum(priorities[badge] for badge in badges)
