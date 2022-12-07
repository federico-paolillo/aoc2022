import unittest

from aoc2022.day_07 import part_one, parse_cmd_line, part_two, read_cmd_lines


class DaySixTestCase(unittest.TestCase):
    def test_part_one_solves_example_input(self):
        result = part_one(
            [
                parse_cmd_line("$ cd /"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("dir a"),
                parse_cmd_line("14848514 b.txt"),
                parse_cmd_line("8504156 c.dat"),
                parse_cmd_line("dir d"),
                parse_cmd_line("$ cd a"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("dir e"),
                parse_cmd_line("29116 f"),
                parse_cmd_line("2557 g"),
                parse_cmd_line("62596 h.lst"),
                parse_cmd_line("$ cd e"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("584 i"),
                parse_cmd_line("$ cd .."),
                parse_cmd_line("$ cd .."),
                parse_cmd_line("$ cd d"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("4060174 j"),
                parse_cmd_line("8033020 d.log"),
                parse_cmd_line("5626152 d.ext"),
                parse_cmd_line("7214296 k"),
            ]
        )

        self.assertEqual(result, 95437)

    def test_part_one_solves_real_input(self):
        cmd_lines = read_cmd_lines("inputs/day_07.txt")

        result = part_one(cmd_lines)

        self.assertEqual(result, 1141028)

    def test_part_two_solves_example_input(self):
        result = part_two(
            [
                parse_cmd_line("$ cd /"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("dir a"),
                parse_cmd_line("14848514 b.txt"),
                parse_cmd_line("8504156 c.dat"),
                parse_cmd_line("dir d"),
                parse_cmd_line("$ cd a"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("dir e"),
                parse_cmd_line("29116 f"),
                parse_cmd_line("2557 g"),
                parse_cmd_line("62596 h.lst"),
                parse_cmd_line("$ cd e"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("584 i"),
                parse_cmd_line("$ cd .."),
                parse_cmd_line("$ cd .."),
                parse_cmd_line("$ cd d"),
                parse_cmd_line("$ ls"),
                parse_cmd_line("4060174 j"),
                parse_cmd_line("8033020 d.log"),
                parse_cmd_line("5626152 d.ext"),
                parse_cmd_line("7214296 k"),
            ]
        )

        self.assertEqual(result, 24933642)

    def test_part_two_solves_real_input(self):
        cmd_lines = read_cmd_lines("inputs/day_07.txt")

        result = part_two(cmd_lines)

        self.assertEqual(result, 8278005)
