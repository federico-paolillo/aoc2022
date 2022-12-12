from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Instruction:
    duration: int
    value: int


@dataclass
class Elfpu:
    cycles: int = field(default=0)
    ip: int = field(default=0)
    ic: int = field(default=0)
    x: int = field(default=1)


@dataclass
class Elfram:
    instructions: list[Instruction] = field(default_factory=list)


TickFn = Callable[[Elfpu], None]


def signal_strength(elfpu: Elfpu) -> int:
    return elfpu.cycles * elfpu.x


def should_probe(elfpu: Elfpu) -> bool:
    return elfpu.cycles % 40 == 20


def pixel_is_lit(elfpu: Elfpu) -> bool:

    sprite_start = elfpu.x - 1
    sprite_end = sprite_start + 2

    current_pixel = (elfpu.cycles - 1) % 40

    is_lit = sprite_start <= current_pixel <= sprite_end

    return is_lit


def dereference(ram: Elfram, address: int) -> Optional[Instruction]:
    return ram.instructions[address] if address < len(ram.instructions) else None


def step(cpu: Elfpu, ram: Elfram, tick_fn: TickFn):
    instruction = dereference(ram, cpu.ip)

    if not instruction:
        return False

    cpu.cycles = cpu.cycles + 1
    cpu.ic = cpu.ic + 1

    if tick_fn:
        tick_fn(cpu)

    if cpu.ic == instruction.duration:
        cpu.x = cpu.x + instruction.value
        cpu.ip = cpu.ip + 1
        cpu.ic = 0

    return True


def emulate(instructions: list[Instruction], tick_fn: TickFn):
    cpu = Elfpu()
    ram = Elfram(instructions)

    while step(cpu, ram, tick_fn):
        pass


def parse_instruction(instruction_to_parse: str):
    if instruction_to_parse.startswith("noop"):
        return Instruction(1, 0)

    _, value_to_parse = instruction_to_parse.split(" ")

    return Instruction(2, int(value_to_parse))


def read_instruction_file(file_path: str) -> list[Instruction]:
    result = []

    with open(file_path, "r") as file:
        for instruction_row in file:
            if not instruction_row.isspace():
                instruction_to_parse = instruction_row.strip()
                result.append(parse_instruction(instruction_to_parse))

    return result


def part_one(instructions: list[Instruction]) -> int:
    signals = []

    def gather_signal(cpu: Elfpu):
        if should_probe(cpu):
            signals.append(signal_strength(cpu))

    emulate(instructions, tick_fn=gather_signal)

    return sum(signals)


def part_two(instructions: list[Instruction]):
    def printer(cpu: Elfpu):
        new_line = "\n" if cpu.cycles % 40 == 0 else ""

        if pixel_is_lit(cpu):
            print("⬜", end=new_line)
        else:
            print("⬛", end=new_line)

    print()

    emulate(instructions, tick_fn=printer)
