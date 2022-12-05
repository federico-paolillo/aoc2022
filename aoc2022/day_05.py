from dataclasses import dataclass
from collections import deque


@dataclass
class CrateMoveInstruction:
    crates_to_move: int
    from_crate: int
    to_crate: int


class CrateMover9000:
    def __init__(self, initial_state: list[list[str]]) -> None:
        self.crate_stacks = [deque(crates_stack) for crates_stack in initial_state]

    def apply_move_instruction(self, crate_move_instruction: CrateMoveInstruction):
        from_crate_index = crate_move_instruction.from_crate - 1
        to_crate_index = crate_move_instruction.to_crate - 1

        for i in range(0, crate_move_instruction.crates_to_move):
            self.crate_stacks[to_crate_index].append(
                self.crate_stacks[from_crate_index].pop()
            )


class CrateMover9001:
    def __init__(self, initial_state: list[list[str]]) -> None:
        self.crate_stacks = [list(crates_stack) for crates_stack in initial_state]

    def apply_move_instruction(self, crate_move_instruction: CrateMoveInstruction):
        from_crate_index = crate_move_instruction.from_crate - 1
        to_crate_index = crate_move_instruction.to_crate - 1

        substack = self.crate_stacks[from_crate_index][
            -crate_move_instruction.crates_to_move :
        ]

        del self.crate_stacks[from_crate_index][
            -crate_move_instruction.crates_to_move :
        ]

        self.crate_stacks[to_crate_index].extend(substack)


def read_moving_instruction(file_path: str) -> list[CrateMoveInstruction]:
    result: list[CrateMoveInstruction] = []

    with open(file_path, "r") as file:
        for move_instruction_line in file:
            if not move_instruction_line.isspace():
                (
                    _,
                    crates_to_move_to_parse,
                    _,
                    from_to_parse,
                    _,
                    to_to_parse,
                ) = move_instruction_line.strip().split(" ")

                crates_to_move = int(crates_to_move_to_parse)
                from_crate = int(from_to_parse)
                to_crate = int(to_to_parse)

                move_instruction = CrateMoveInstruction(
                    crates_to_move, from_crate, to_crate
                )

                result.append(move_instruction)

    return result


def part_one(
    initial_state: list[list[str]], crate_move_instructions: list[CrateMoveInstruction]
) -> str:
    cargo = CrateMover9000(initial_state)

    for crate_move_instruction in crate_move_instructions:
        cargo.apply_move_instruction(crate_move_instruction)

    return "".join(crate_stack[-1] for crate_stack in cargo.crate_stacks if crate_stack)


def part_two(
    initial_state: list[list[str]], crate_move_instructions: list[CrateMoveInstruction]
) -> str:
    cargo = CrateMover9001(initial_state)

    for crate_move_instruction in crate_move_instructions:
        cargo.apply_move_instruction(crate_move_instruction)

    return "".join(crate_stack[-1] for crate_stack in cargo.crate_stacks if crate_stack)
