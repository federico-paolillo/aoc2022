import unittest

from aoc2022.day_05 import (
    part_one,
    CrateMoveInstruction,
    part_two,
    read_moving_instruction,
)


class DayFiveTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            [
                CrateMoveInstruction(1, 2, 1),
                CrateMoveInstruction(3, 1, 3),
                CrateMoveInstruction(2, 2, 1),
                CrateMoveInstruction(1, 1, 2),
            ],
        )

        self.assertEqual(result, "CMZ")

    def test_part_one_solves_real_input(self):
        moving_instructions = read_moving_instruction("inputs/day_05.txt")

        result = part_one(
            [
                ["D", "T", "R", "B", "J", "L", "W", "G"],
                ["S", "W", "C"],
                ["R", "Z", "T", "M"],
                ["D", "T", "C", "H", "S", "P", "V"],
                ["G", "P", "T", "L", "D", "Z"],
                ["F", "B", "R", "Z", "J", "Q", "C", "D"],
                ["S", "B", "D", "J", "M", "F", "T", "R"],
                ["L", "H", "R", "B", "T", "V", "M"],
                ["Q", "P", "D", "S", "V"],
            ],
            moving_instructions,
        )

        self.assertEqual(result, "SHMSDGZVC")

    def test_part_two_solves_example_input(self):
        result = part_two(
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            [
                CrateMoveInstruction(1, 2, 1),
                CrateMoveInstruction(3, 1, 3),
                CrateMoveInstruction(2, 2, 1),
                CrateMoveInstruction(1, 1, 2),
            ],
        )

        self.assertEqual(result, "MCD")

    def test_part_two_solves_real_input(self):
        moving_instructions = read_moving_instruction("inputs/day_05.txt")

        result = part_two(
            [
                ["D", "T", "R", "B", "J", "L", "W", "G"],
                ["S", "W", "C"],
                ["R", "Z", "T", "M"],
                ["D", "T", "C", "H", "S", "P", "V"],
                ["G", "P", "T", "L", "D", "Z"],
                ["F", "B", "R", "Z", "J", "Q", "C", "D"],
                ["S", "B", "D", "J", "M", "F", "T", "R"],
                ["L", "H", "R", "B", "T", "V", "M"],
                ["Q", "P", "D", "S", "V"],
            ],
            moving_instructions,
        )

        self.assertEqual(result, "VRZGHDFBQ")
