from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional, Union


@dataclass
class GoUpCommand:
    pass


@dataclass
class AddFileCommand:
    name: str
    size: str


@dataclass
class AddFolderCommand:
    name: str


@dataclass
class ChangeFolderCommand:
    name: str


Commands = Union[GoUpCommand, AddFileCommand, AddFolderCommand, ChangeFolderCommand]
ElffsItem = Union["ElffsFile", "ElffsFolder"]
ElffsVisitor = Callable[[ElffsItem], None]


class ElffsFile:
    def __init__(self, name: str, file_size: int):
        self._file_size = file_size
        self.name = name

    def get_size(self) -> int:
        return self._file_size

    def accept_visit(self, visitor: ElffsVisitor):
        return visitor(self)


class ElffsFolder:
    def __init__(self, parent, name):
        self._children: list[ElffsItem] = []
        self.parent: Optional[ElffsFolder] = parent
        self.name: str = name

    def add_item(self, elffs_item: ElffsItem):
        self._children.append(elffs_item)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def find_subfolder_shallow(self, subfolder_name: str) -> Optional["ElffsFolder"]:
        return next(
            (
                folder
                for folder in self._children
                if isinstance(folder, ElffsFolder)
                if folder.name == subfolder_name
            ),
            None,
        )

    def accept_visit(self, visitor: ElffsVisitor):
        visitor(self)

        for child in self._children:
            child.accept_visit(visitor)


def apply_command(current_folder: ElffsFolder, elffs_command: Commands) -> ElffsFolder:
    if isinstance(elffs_command, GoUpCommand):
        return current_folder.parent

    if isinstance(elffs_command, AddFolderCommand):
        current_folder.add_item(ElffsFolder(current_folder, elffs_command.name))
        return current_folder

    if isinstance(elffs_command, AddFileCommand):
        current_folder.add_item(ElffsFile(elffs_command.name, elffs_command.size))
        return current_folder

    if isinstance(elffs_command, ChangeFolderCommand):
        return current_folder.find_subfolder_shallow(elffs_command.name)


def parse_cmd_line(cmd_line: str) -> Optional[Commands]:
    if cmd_line == "$ cd /":
        return None

    if cmd_line == "$ ls":
        return None

    if cmd_line == "$ cd ..":
        return GoUpCommand()

    if cmd_line.startswith("$ cd"):
        _, _, folder_name = cmd_line.split(" ")
        return ChangeFolderCommand(folder_name)

    if cmd_line.startswith("dir"):
        _, folder_name = cmd_line.split(" ")
        return AddFolderCommand(folder_name)

    file_size_to_parse, file_name = cmd_line.split(" ")

    return AddFileCommand(file_name, int(file_size_to_parse))


def read_cmd_lines(file_path: str) -> list[Commands]:
    result: list[Commands] = []

    with open(file_path, "r") as file:
        for cmd_line in file:
            if not cmd_line.isspace():
                command = parse_cmd_line(cmd_line.strip())
                if command:
                    result.append(command)

    return result


def part_one(commands: list[Commands]) -> int:
    root = ElffsFolder(None, "/")

    current_folder = root

    for command in commands:
        if command:
            current_folder = apply_command(current_folder, command)

    folder_sizes = []

    def folder_collector(elffs_item: ElffsItem):
        if isinstance(elffs_item, ElffsFolder):
            folder_sizes.append(elffs_item.get_size())

    root.accept_visit(folder_collector)

    return sum(size for size in folder_sizes if size <= 100_000)


_DISK_TOTAL_SPACE = 70_000_000
_DISK_SPACE_REQUIRED = 30_000_000


def part_two(commands: list[Commands]) -> int:
    root = ElffsFolder(None, "/")

    current_folder = root

    for command in commands:
        if command:
            current_folder = apply_command(current_folder, command)

    disk_space_use = root.get_size()
    disk_space_left = _DISK_TOTAL_SPACE - disk_space_use
    disk_space_needed = _DISK_SPACE_REQUIRED - disk_space_left

    folder_sizes = []

    def folder_collector(elffs_item: ElffsItem):
        if isinstance(elffs_item, ElffsFolder):
            folder_sizes.append(elffs_item.get_size())

    root.accept_visit(folder_collector)

    return next(
        iter(sorted(size for size in folder_sizes if size >= disk_space_needed))
    )
