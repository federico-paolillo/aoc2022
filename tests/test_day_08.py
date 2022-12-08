import unittest

from aoc2022.day_08 import part_one, part_two, read_jungle_trees_map


class DaySixTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0],
            ]
        )

        self.assertEqual(result, 21)

    def test_part_one_solves_real_input(self):
        jungle_trees_map = read_jungle_trees_map("inputs/day_08.txt")

        result = part_one(jungle_trees_map)

        self.assertEqual(result, 1693)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0],
            ]
        )

        self.assertEqual(result, 8)

    def test_part_two_solves_real_input(self):
        jungle_trees_map = read_jungle_trees_map("inputs/day_08.txt")

        result = part_two(jungle_trees_map)

        self.assertEqual(result, 422059)
