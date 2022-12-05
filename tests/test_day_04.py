import unittest

from aoc2022.day_04 import (
    part_one,
    part_two,
    read_assignment_pairs,
    CleaningAssignmentPair,
)


class DayFourTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                CleaningAssignmentPair(2, 4, 6, 8),
                CleaningAssignmentPair(2, 3, 4, 5),
                CleaningAssignmentPair(5, 7, 7, 9),
                CleaningAssignmentPair(2, 8, 3, 7),
                CleaningAssignmentPair(6, 6, 4, 6),
                CleaningAssignmentPair(2, 6, 4, 8),
            ]
        )

        self.assertEqual(result, 2)

    def test_part_one_solves_real_input(self):
        cleaning_assignment_pairs = read_assignment_pairs("inputs/day_04.txt")
        result = part_one(cleaning_assignment_pairs)
        self.assertEqual(result, 540)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                CleaningAssignmentPair(2, 4, 6, 8),
                CleaningAssignmentPair(2, 3, 4, 5),
                CleaningAssignmentPair(5, 7, 7, 9),
                CleaningAssignmentPair(2, 8, 3, 7),
                CleaningAssignmentPair(6, 6, 4, 6),
                CleaningAssignmentPair(2, 6, 4, 8),
            ]
        )

        self.assertEqual(result, 4)

    def test_part_two_solves_real_input(self):
        cleaning_assignment_pairs = read_assignment_pairs("inputs/day_04.txt")
        result = part_two(cleaning_assignment_pairs)
        self.assertEqual(result, 872)
