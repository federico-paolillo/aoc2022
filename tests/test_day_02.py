import unittest

from aoc2022.day_02 import (
    RockPaperScissorsStrategyGuideEntry,
    part_one,
    part_two,
    read_rps_strategy_guide_entries,
)


class DayTwoTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                RockPaperScissorsStrategyGuideEntry("A", "Y"),
                RockPaperScissorsStrategyGuideEntry("B", "X"),
                RockPaperScissorsStrategyGuideEntry("C", "Z"),
            ]
        )

        self.assertEqual(result, 15)

    def test_part_one_solves_real_input(self):
        rps_strategy_guide_entries = read_rps_strategy_guide_entries(
            "inputs/day_02.txt"
        )
        result = part_one(rps_strategy_guide_entries)
        self.assertEqual(result, 14297)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                RockPaperScissorsStrategyGuideEntry("A", "Y"),
                RockPaperScissorsStrategyGuideEntry("B", "X"),
                RockPaperScissorsStrategyGuideEntry("C", "Z"),
            ]
        )

        self.assertEqual(result, 12)

    def test_part_two_solves_real_input(self):
        rps_strategy_guide_entries = read_rps_strategy_guide_entries(
            "inputs/day_02.txt"
        )
        result = part_two(rps_strategy_guide_entries)
        self.assertEqual(result, 10498)
