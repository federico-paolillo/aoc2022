import unittest

from aoc2022.day_09 import (
    Movement,
    MovementDirection,
    apply_movement,
    follow_head,
    compensating_movement,
    part_one,
    part_two,
    read_movements_file,
)


class DayNineTestCase(unittest.TestCase):
    def test_tail_follows_head_1(self):
        # .....    .....    .....
        # .....    ..H..    ..H..
        # ..H.. -> ..... -> ..T..
        # .T...    .T...    .....
        # .....    .....    .....

        head = (3, 3)
        tail = (2, 4)

        head = apply_movement(Movement(MovementDirection.UP, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (3, 2))
        self.assertEqual(tail, (3, 3))

    def test_tail_follows_head_2(self):
        # .....    .....    .....
        # .....    .....    .....
        # ..H.. -> ...H. -> ..TH.
        # .T...    .T...    .....
        # .....    .....    .....

        head = (3, 3)
        tail = (2, 4)

        head = apply_movement(Movement(MovementDirection.RIGHT, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (4, 3))
        self.assertEqual(tail, (3, 3))

    def test_tail_follows_head_3(self):
        # ...    ...    ...
        # .T.    .T.    ...
        # .H. -> ... -> .T.
        # ...    .H.    .H.
        # ...    ...    ...

        head = (2, 3)
        tail = (2, 2)

        head = apply_movement(Movement(MovementDirection.DOWN, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (2, 4))
        self.assertEqual(tail, (2, 3))

    def test_tail_follows_head_3(self):
        # .....    .....    .....
        # .TH.. -> .T.H. -> ..TH.
        # .....    .....    .....

        head = (3, 2)
        tail = (2, 2)

        head = apply_movement(Movement(MovementDirection.RIGHT, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (4, 2))
        self.assertEqual(tail, (3, 2))

    def test_tail_stands_still_1(self):
        # .....    .....
        # .TH.. -> .T...
        # .....    ..H..

        head = (3, 2)
        tail = (2, 2)

        head = apply_movement(Movement(MovementDirection.DOWN, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (3, 3))
        self.assertEqual(tail, (2, 2))

    def test_tail_stands_still_1(self):
        # .....    .....
        # .TH.. -> .H... (H covers T)
        # .....    .....

        head = (3, 2)
        tail = (2, 2)

        head = apply_movement(Movement(MovementDirection.LEFT, 1), head)
        tail = follow_head(head, tail)

        self.assertEqual(head, (2, 2))
        self.assertEqual(tail, (2, 2))

    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                Movement(MovementDirection.RIGHT, 4),
                Movement(MovementDirection.UP, 4),
                Movement(MovementDirection.LEFT, 3),
                Movement(MovementDirection.DOWN, 1),
                Movement(MovementDirection.RIGHT, 4),
                Movement(MovementDirection.DOWN, 1),
                Movement(MovementDirection.LEFT, 5),
                Movement(MovementDirection.RIGHT, 2),
            ]
        )

        self.assertEqual(13, result)

    def test_part_one_solves_real_input(self):
        movements = read_movements_file("inputs/day_09.txt")

        result = part_one(movements)

        self.assertEqual(6018, result)

    def test_part_two_solves_example_input_1(self):
        result = part_two(
            [
                Movement(MovementDirection.RIGHT, 4),
                Movement(MovementDirection.UP, 4),
                Movement(MovementDirection.LEFT, 3),
                Movement(MovementDirection.DOWN, 1),
                Movement(MovementDirection.RIGHT, 4),
                Movement(MovementDirection.DOWN, 1),
                Movement(MovementDirection.LEFT, 5),
                Movement(MovementDirection.RIGHT, 2),
            ]
        )

        self.assertEqual(1, result)

    def test_part_two_solves_example_input_2(self):
        result = part_two(
            [
                Movement(MovementDirection.RIGHT, 5),
                Movement(MovementDirection.UP, 8),
                Movement(MovementDirection.LEFT, 8),
                Movement(MovementDirection.DOWN, 3),
                Movement(MovementDirection.RIGHT, 17),
                Movement(MovementDirection.DOWN, 10),
                Movement(MovementDirection.LEFT, 25),
                Movement(MovementDirection.UP, 20),
            ]
        )

        self.assertEqual(36, result)

    def test_part_two_solves_real_input(self):
        movements = read_movements_file("inputs/day_09.txt")

        result = part_two(movements)

        self.assertEqual(6018, result)
