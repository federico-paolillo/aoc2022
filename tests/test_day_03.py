import unittest

from aoc2022.day_03 import part_one, part_two, read_rucksacks_file


class DayThreeTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ]
        )

        self.assertEqual(result, 157)

    def test_part_one_solves_real_input(self):
        rucksack_items_lines = read_rucksacks_file("inputs/day_03.txt")
        result = part_one(rucksack_items_lines)
        self.assertEqual(result, 7701)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ]
        )

        self.assertEqual(result, 70)

    def test_part_two_solves_real_input(self):
        rucksack_items_lines = read_rucksacks_file("inputs/day_03.txt")
        result = part_two(rucksack_items_lines)
        self.assertEqual(result, 2644)
