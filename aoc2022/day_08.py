from dataclasses import dataclass
from enum import Enum
import itertools
from typing import Callable, Generator, Iterator, Optional, Union


class LookDirection(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


JungleTreesMap = list[list[int]]


def take_until(
    iterable: Iterator[int], predicate: Callable[[int], bool]
) -> Generator[int, None, None]:
    for x in iterable:
        yield x
        if predicate(x):
            break


def map_size(jungle_trees_map: JungleTreesMap) -> tuple[int, int]:
    # We are talking about max x and y no len() !

    max_y = len(jungle_trees_map) - 1
    max_x = min(len(row) - 1 for row in jungle_trees_map)

    return (max_x, max_y)


def map_slice(
    jungle_trees_map: JungleTreesMap, x: int, y: int, direction: LookDirection
) -> list[int]:
    max_x, max_y = map_size(jungle_trees_map)

    if x == max_x and direction == LookDirection.RIGHT:
        return []

    if y == max_y and direction == LookDirection.DOWN:
        return []

    if x == 0 and direction == LookDirection.LEFT:
        return []

    if y == 0 and direction == LookDirection.UP:
        return []

    # Remember to exclude self and keep "line of sight" order !

    map_slice = []

    match direction:
        case LookDirection.UP:
            map_slice = [row[x] for row in jungle_trees_map[:y]]
            map_slice.reverse()
        case LookDirection.DOWN:
            map_slice = [row[x] for row in jungle_trees_map[y + 1 :]]
        case LookDirection.LEFT:
            map_slice = jungle_trees_map[y][0:x]
            map_slice.reverse()
        case LookDirection.RIGHT:
            map_slice = jungle_trees_map[y][x + 1 :]

    return map_slice


def is_tree_visible(jungle_trees_map: JungleTreesMap, x: int, y: int) -> bool:
    max_x, max_y = map_size(jungle_trees_map)

    # Edge of map trees are always visible

    if x == 0:
        return True

    if x == max_x:
        return True

    if y == 0:
        return True

    if y == max_y:
        return True

    this_tree = jungle_trees_map[y][x]

    # Must be the tallest tree in all 4 directions to be visible

    tallest_trees_in_4_directions = [
        max(map_slice(jungle_trees_map, x, y, LookDirection.RIGHT)),
        max(map_slice(jungle_trees_map, x, y, LookDirection.LEFT)),
        max(map_slice(jungle_trees_map, x, y, LookDirection.UP)),
        max(map_slice(jungle_trees_map, x, y, LookDirection.DOWN)),
    ]

    is_tallest_tree = any(
        True
        for tallest_tree in tallest_trees_in_4_directions
        if this_tree > tallest_tree
    )

    return is_tallest_tree


def scenic_score(jungle_trees_map: JungleTreesMap, x: int, y: int) -> int:
    this_tree = jungle_trees_map[y][x]

    right_view = map_slice(jungle_trees_map, x, y, LookDirection.RIGHT)
    left_view = map_slice(jungle_trees_map, x, y, LookDirection.LEFT)
    up_view = map_slice(jungle_trees_map, x, y, LookDirection.UP)
    down_view = map_slice(jungle_trees_map, x, y, LookDirection.DOWN)

    view_score_right = sum(1 for _ in take_until(right_view, lambda x: x >= this_tree))
    view_score_left = sum(1 for _ in take_until(left_view, lambda x: x >= this_tree))
    view_score_up = sum(1 for _ in take_until(up_view, lambda x: x >= this_tree))
    view_score_down = sum(1 for _ in take_until(down_view, lambda x: x >= this_tree))

    total_scenic_score = (
        view_score_right * view_score_left * view_score_up * view_score_down
    )

    return total_scenic_score


def read_jungle_trees_map(file_path: str) -> JungleTreesMap:
    result = []

    with open(file_path, "r") as file:
        for trees_row in file:
            row = []

            if not trees_row.isspace():
                for height in trees_row.strip():
                    row.append(int(height))

            result.append(row)

    return result


def part_one(jungle_trees_map: JungleTreesMap) -> int:
    max_x, max_y = map_size(jungle_trees_map)

    map_coordinates = itertools.product(range(0, max_x + 1), range(0, max_y + 1))

    return sum(1 for x, y in map_coordinates if is_tree_visible(jungle_trees_map, x, y))


def part_two(jungle_trees_map: JungleTreesMap) -> int:
    max_x, max_y = map_size(jungle_trees_map)

    map_coordinates = itertools.product(range(0, max_x + 1), range(0, max_y + 1))

    return max(scenic_score(jungle_trees_map, x, y) for x, y in map_coordinates)
