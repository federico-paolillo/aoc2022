import unittest

from aoc2022.day_09 import compensating_movement


class DayNineTestCase(unittest.TestCase):
    def test_tail_follow_head_1(self):
        # .....
        # .TH..
        # .....

        movement = compensating_movement(3, 2, 2, 2)

        self.assertEqual((0, 0), movement) # Tail does not move

    def test_tail_follow_head_4(self):
        # ....
        # .H..
        # ..T.
        # ....

        movement = compensating_movement(2, 2, 3, 3)

        self.assertEqual((0, 0), movement) # Tail does not move

    def test_tail_follow_head_4(self):
        # ...
        # .H. (H covers T)
        # ...

        movement = compensating_movement(2, 2, 2, 2)

        self.assertEqual((0, 0), movement) # Tail does not move

    def test_tail_follow_head_4(self):
        # .....    .....
        # .T.H. -> ..TH.
        # .....    .....

        movement = compensating_movement(4, 2, 2, 2)

        self.assertEqual((1, 0), movement) # Tail moves one step to the right

    def test_tail_follow_head_5(self):
        # ...    ...
        # .T.    ...
        # ... -> .T.
        # .H.    .H.
        # ...    ...

        movement = compensating_movement(2, 4, 2, 2)

        self.assertEqual((0, 1), movement) # Tail moves one step down

    def test_tail_follow_head_6(self):
        # .....    .....
        # ..H..    ..H..
        # ..... -> ..T..
        # .T...    .....
        # .....    .....

        movement = compensating_movement(3, 2, 2, 4)

        self.assertEqual((1, -1), movement) # Tail moves one step up and one step right

    def test_tail_follow_head_7(self):
        # .....    .....
        # .....    .....
        # ...H. -> ..TH.
        # .T...    .....
        # .....    .....

        movement = compensating_movement(4, 3, 2, 4)

        self.assertEqual((1, -1), movement) # Tail moves one step up and one step right