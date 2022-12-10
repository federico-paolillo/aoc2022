from dataclasses import dataclass
from enum import Enum

Point = tuple[int, int]


class MovementDirection(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


_FILE_DIRECTION_TO_MOVEMENT_DIRECTION = {
    "U": MovementDirection.UP,
    "D": MovementDirection.DOWN,
    "L": MovementDirection.LEFT,
    "R": MovementDirection.RIGHT,
}


@dataclass
class Movement:
    direction: MovementDirection
    steps: int

    def vector(self) -> Point:
        match self.direction:
            case MovementDirection.UP:
                return (0, -1)
            case MovementDirection.DOWN:
                return (0, 1)
            case MovementDirection.LEFT:
                return (-1, 0)
            case MovementDirection.RIGHT:
                return (1, 0)

        return (0, 0)


def movement_offset(coordinate_diff: int) -> int:
    return +1 if coordinate_diff > 1 else -1 if coordinate_diff < -1 else 0


def chessboard_distance(head: Point, tail: Point) -> int:
    head_x, head_y = head
    tail_x, tail_y = tail

    distance = max(abs(tail_x - head_x), abs(tail_y - head_y))

    return (
        0 if distance == 0 else distance - 1
    )  # I just need the number of distance "steps" not the numerical distance


def compensating_movement(head: Point, tail: Point) -> Point:
    distance = chessboard_distance(head, tail)

    if distance == 0:
        return (0, 0)

    head_x, head_y = head
    tail_x, tail_y = tail

    x_diff = head_x - tail_x
    y_diff = head_y - tail_y

    offset_x = movement_offset(x_diff)
    offset_y = movement_offset(y_diff)

    return (x_diff - offset_x, y_diff - offset_y)


def translate_point(movement_vector: Point, point: Point) -> Point:
    point_x, point_y = point
    movement_x, movement_y = movement_vector

    return (point_x + movement_x, point_y + movement_y)


def follow_head(head: Point, tail: Point) -> Point:
    tail_compensating_movement = compensating_movement(head, tail)
    return translate_point(tail_compensating_movement, tail)


def apply_movement(movement: Movement, head: Point) -> Point:
    return translate_point(movement.vector(), head)


def read_movements_file(file_path: str) -> list[Movement]:
    result = []

    with open(file_path, "r") as file:
        for movement_row in file:
            if not movement_row.isspace():
                direction, steps = movement_row.strip().split(" ")

                movement = Movement(
                    _FILE_DIRECTION_TO_MOVEMENT_DIRECTION[direction], int(steps)
                )

                result.append(movement)

    return result


def part_one(movements: list[Movement]) -> int:
    head = (0, 0)
    tail = (0, 0)

    unique_tail_positions = {tail}

    for movement in movements:
        for _ in range(0, movement.steps):
            head = apply_movement(movement, head)
            tail = follow_head(head, tail)

            unique_tail_positions.add(tail)

    return len(unique_tail_positions)


_ROPE_SEGMENTS = 10
_HEAD_SEGMENT_INDEX = 0
_TAIL_SEGMENT_INDEX = 9


def part_two(movements: list[Movement]) -> int:
    rope_segments = [(0, 0)] * _ROPE_SEGMENTS

    unique_tail_positions = {rope_segments[_TAIL_SEGMENT_INDEX]}

    for movement in movements:
        for _ in range(0, movement.steps):
            rope_segments[_HEAD_SEGMENT_INDEX] = apply_movement(
                movement, rope_segments[_HEAD_SEGMENT_INDEX]
            )

            for i in range(0, _ROPE_SEGMENTS - 1):
                rope_segments[i + 1] = follow_head(
                    rope_segments[i], rope_segments[i + 1]
                )

            unique_tail_positions.add(rope_segments[_TAIL_SEGMENT_INDEX])

    return len(unique_tail_positions)
