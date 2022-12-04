from dataclasses import dataclass
from enum import Enum
from typing import Callable, List


class _RockPaperScissorsMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class _RockPaperScissorsRoundOutcome(Enum):
    DRAW = 0
    WIN = 1
    LOSS = 2


@dataclass
class RockPaperScissorsStrategyGuideEntry:
    first_column: str
    second_column: str


@dataclass
class RockPaperScissorsRound:
    _WINNING_MOVES = {
        _RockPaperScissorsMove.ROCK: _RockPaperScissorsMove.PAPER,
        _RockPaperScissorsMove.PAPER: _RockPaperScissorsMove.SCISSORS,
        _RockPaperScissorsMove.SCISSORS: _RockPaperScissorsMove.ROCK,
    }

    _LOSING_MOVES = {
        _RockPaperScissorsMove.ROCK: _RockPaperScissorsMove.SCISSORS,
        _RockPaperScissorsMove.PAPER: _RockPaperScissorsMove.ROCK,
        _RockPaperScissorsMove.SCISSORS: _RockPaperScissorsMove.PAPER,
    }

    _MOVE_SCORES = {
        _RockPaperScissorsMove.ROCK: 1,
        _RockPaperScissorsMove.PAPER: 2,
        _RockPaperScissorsMove.SCISSORS: 3,
    }

    opponent_move: _RockPaperScissorsMove
    your_move: _RockPaperScissorsMove

    def outcome(self) -> _RockPaperScissorsRoundOutcome:
        if self.opponent_move == self.your_move:
            return _RockPaperScissorsRoundOutcome.DRAW

        if self.your_move == RockPaperScissorsRound._WINNING_MOVES[self.opponent_move]:
            return _RockPaperScissorsRoundOutcome.WIN

        return _RockPaperScissorsRoundOutcome.LOSS

    def score(self) -> int:
        outcome_score = 0
        move_score = RockPaperScissorsRound._MOVE_SCORES[self.your_move]

        match self.outcome():
            case _RockPaperScissorsRoundOutcome.DRAW:
                outcome_score = 3
            case _RockPaperScissorsRoundOutcome.WIN:
                outcome_score = 6
            case _:
                outcome_score = 0

        return outcome_score + move_score

    @staticmethod
    def from_outcome(
        opponent_move: _RockPaperScissorsMove,
        desired_outcome: _RockPaperScissorsRoundOutcome,
    ) -> "RockPaperScissorsRound":
        if desired_outcome == _RockPaperScissorsRoundOutcome.DRAW:
            return RockPaperScissorsRound(opponent_move, opponent_move)

        if desired_outcome == _RockPaperScissorsRoundOutcome.WIN:
            return RockPaperScissorsRound(
                opponent_move, RockPaperScissorsRound._WINNING_MOVES[opponent_move]
            )

        if desired_outcome == _RockPaperScissorsRoundOutcome.LOSS:
            return RockPaperScissorsRound(
                opponent_move, RockPaperScissorsRound._LOSING_MOVES[opponent_move]
            )


_GUIDE_CONVENTION_FOR_OPPONENT_MOVES = {
    "A": _RockPaperScissorsMove.ROCK,
    "B": _RockPaperScissorsMove.PAPER,
    "C": _RockPaperScissorsMove.SCISSORS,
}

_GUIDE_CONVENTION_FOR_YOUR_MOVES = {
    "X": _RockPaperScissorsMove.ROCK,
    "Y": _RockPaperScissorsMove.PAPER,
    "Z": _RockPaperScissorsMove.SCISSORS,
}

_GUIDE_CONVENTION_FOR_OUTCOMES = {
    "X": _RockPaperScissorsRoundOutcome.LOSS,
    "Y": _RockPaperScissorsRoundOutcome.DRAW,
    "Z": _RockPaperScissorsRoundOutcome.WIN,
}


def _interpret_second_column_as_desired_outcome(
    strat_guide_entry: RockPaperScissorsStrategyGuideEntry,
) -> RockPaperScissorsRound:
    return RockPaperScissorsRound.from_outcome(
        _GUIDE_CONVENTION_FOR_OPPONENT_MOVES[strat_guide_entry.first_column],
        _GUIDE_CONVENTION_FOR_OUTCOMES[strat_guide_entry.second_column],
    )


def _interpret_both_columns_as_moves(
    strat_guide_entry: RockPaperScissorsStrategyGuideEntry,
) -> RockPaperScissorsRound:
    return RockPaperScissorsRound(
        _GUIDE_CONVENTION_FOR_OPPONENT_MOVES[strat_guide_entry.first_column],
        _GUIDE_CONVENTION_FOR_YOUR_MOVES[strat_guide_entry.second_column],
    )


def _calculate_score(
    strategy_guide_entries: List[RockPaperScissorsStrategyGuideEntry],
    entry_interpretation: Callable[
        [RockPaperScissorsStrategyGuideEntry], _RockPaperScissorsRoundOutcome
    ],
) -> int:
    rps_rounds = (entry_interpretation(entry) for entry in strategy_guide_entries)
    return sum(rps_round.score() for rps_round in rps_rounds)


def read_rps_strategy_guide_entries(
    file_path: str,
) -> List[RockPaperScissorsStrategyGuideEntry]:
    result: List[RockPaperScissorsStrategyGuideEntry] = []

    with open(file_path, "r") as file:
        for guide_line in file:
            if not guide_line.isspace():
                first_column, second_column = guide_line.strip().split(" ")
                entry = RockPaperScissorsStrategyGuideEntry(first_column, second_column)
                result.append(entry)

    return result


def part_one(strategy_guide_entries: List[RockPaperScissorsStrategyGuideEntry]) -> int:
    return _calculate_score(strategy_guide_entries, _interpret_both_columns_as_moves)


def part_two(strategy_guide_entries: List[RockPaperScissorsStrategyGuideEntry]) -> int:
    return _calculate_score(
        strategy_guide_entries, _interpret_second_column_as_desired_outcome
    )
