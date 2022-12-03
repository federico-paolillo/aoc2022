import unittest

from aoc2022.day_02 import RockPaperScissorsMove, RockPaperScissorsRound, part_one, read_rock_paper_scissors_guide


class DayTwoTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                RockPaperScissorsRound(
                    RockPaperScissorsMove.ROCK, RockPaperScissorsMove.PAPER
                ),
                RockPaperScissorsRound(
                    RockPaperScissorsMove.PAPER, RockPaperScissorsMove.ROCK
                ),
                RockPaperScissorsRound(
                    RockPaperScissorsMove.SCISSORS, RockPaperScissorsMove.SCISSORS
                ),
            ]
        )

        self.assertEqual(result, 15)

    def test_part_one_solves_real_input(self):
        inventories_from_file = read_rock_paper_scissors_guide("inputs/day_02.txt")
        result = part_one(inventories_from_file)
        self.assertEqual(result, 14297)