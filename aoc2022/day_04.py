from dataclasses import dataclass
from functools import reduce
from typing import List, Tuple


@dataclass
class CleaningAssignment:
    section_start: int
    section_end: int

    def overlaps(self, other: "CleaningAssignment") -> bool:
        return (
            self.section_start <= other.section_start
            and self.section_end >= other.section_end
        )

    def intersects(self, other: 'CleaningAssignment') -> bool:
        if self.section_start >= other.section_start and self.section_start <= other.section_end:
            return True

        if self.section_end >= other.section_start and self.section_end <= other.section_end:
            return True

        return False


class CleaningAssignmentPair:
    assignment_a: CleaningAssignment
    assignment_b: CleaningAssignment

    def __init__(
        self,
        assignment_a_start: int,
        assignment_a_end: int,
        assignment_b_start: int,
        assignment_b_end: int,
    ):
        self.assignment_a = CleaningAssignment(assignment_a_start, assignment_a_end)
        self.assignment_b = CleaningAssignment(assignment_b_start, assignment_b_end)

    def assigments_overlaps(self) -> bool:
        # A contains B ?
        if self.assignment_a.overlaps(self.assignment_b):
            return True

        # B contains A ?
        if self.assignment_b.overlaps(self.assignment_a):
            return True

        return False

    def assignments_intersects(self) -> bool:
        # A intersects B ?
        if self.assignment_a.intersects(self.assignment_b):
            return True

        # B intersects A ?
        if self.assignment_b.intersects(self.assignment_a):
            return True

        return False


def read_assignment_pairs(file_path: str) -> List[CleaningAssignmentPair]:
    result: List[CleaningAssignmentPair] = []

    with open(file_path, "r") as file:
        for cleaning_assignment_pairs_line in file:
            if not cleaning_assignment_pairs_line.isspace():
                pairs_to_parse = cleaning_assignment_pairs_line.strip().split(",")

                assignment_a_start_to_parse, assignment_a_end_to_parse = pairs_to_parse[
                    0
                ].split("-")
                assignment_b_start_to_parse, assignment_b_end_to_parse = pairs_to_parse[
                    1
                ].split("-")

                assignment_a_start = int(assignment_a_start_to_parse)
                assignment_a_end = int(assignment_a_end_to_parse)

                assignment_b_start = int(assignment_b_start_to_parse)
                assignment_b_end = int(assignment_b_end_to_parse)

                assignment_pair = CleaningAssignmentPair(
                    assignment_a_start,
                    assignment_a_end,
                    assignment_b_start,
                    assignment_b_end,
                )

                result.append(assignment_pair)

    return result


def part_one(assignment_pairs: List[CleaningAssignmentPair]) -> int:
    return len(
        [
            assignment_pair
            for assignment_pair in assignment_pairs
            if assignment_pair.assigments_overlaps()
        ]
    )


def part_two(assignment_pairs: List[CleaningAssignmentPair]) -> int:
    return len(
        [
            assignment_pair
            for assignment_pair in assignment_pairs
            if assignment_pair.assignments_intersects()
        ]
    )
