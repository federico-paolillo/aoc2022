from dataclasses import dataclass
from enum import Enum
from typing import List


class RockPaperScissorsMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RockPaperScissorsRoundOutcome(Enum):
    DRAW = 0
    WIN = 1
    LOSS = 2


WINNING_MOVES = {
    RockPaperScissorsMove.ROCK: RockPaperScissorsMove.PAPER,
    RockPaperScissorsMove.PAPER: RockPaperScissorsMove.SCISSORS,
    RockPaperScissorsMove.SCISSORS: RockPaperScissorsMove.ROCK,
}

MOVE_SCORES = {
    RockPaperScissorsMove.ROCK: 1,
    RockPaperScissorsMove.PAPER: 2,
    RockPaperScissorsMove.SCISSORS: 3,
}


@dataclass
class RockPaperScissorsRound:
    opponent_move: RockPaperScissorsMove
    your_move: RockPaperScissorsMove

    def outcome(self) -> RockPaperScissorsRoundOutcome:
        if self.opponent_move == self.your_move:
            return RockPaperScissorsRoundOutcome.DRAW

        if self.your_move == WINNING_MOVES[self.opponent_move]:
            return RockPaperScissorsRoundOutcome.WIN

        return RockPaperScissorsRoundOutcome.LOSS

    def score(self) -> int:
        outcome_score = 0
        move_score = MOVE_SCORES[self.your_move]

        match self.outcome():
            case RockPaperScissorsRoundOutcome.DRAW:
                outcome_score = 3
            case RockPaperScissorsRoundOutcome.WIN:
                outcome_score = 6
            case _:
                outcome_score = 0

        return outcome_score + move_score


GUIDE_CONVENTION_FOR_OPPONENT_MOVES_TRANSLATION_TABLE = {
    "A": RockPaperScissorsMove.ROCK,
    "B": RockPaperScissorsMove.PAPER,
    "C": RockPaperScissorsMove.SCISSORS,
}

GUIDE_CONVENTION_FOR_YOUR_MOVES_TRANSLATION_TABLE = {
    "X": RockPaperScissorsMove.ROCK,
    "Y": RockPaperScissorsMove.PAPER,
    "Z": RockPaperScissorsMove.SCISSORS,
}


def read_rock_paper_scissors_guide(file_path: str) -> List[RockPaperScissorsRound]:
    result: List[RockPaperScissorsRound] = []

    with open(file_path, "r") as file:
        for guide_line in file:
            if not guide_line.isspace():
                opponent_move, your_move = guide_line.strip().split(" ")
                rps_round = RockPaperScissorsRound(
                    GUIDE_CONVENTION_FOR_OPPONENT_MOVES_TRANSLATION_TABLE[
                        opponent_move
                    ],
                    GUIDE_CONVENTION_FOR_YOUR_MOVES_TRANSLATION_TABLE[your_move],
                )
                result.append(rps_round)

    return result


def part_one(rps_rounds: List[RockPaperScissorsRound]) -> int:
    return sum(rps_round.score() for rps_round in rps_rounds)
