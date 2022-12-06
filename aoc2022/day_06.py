class SlidingSlice:
    def __init__(self, slice_size, some_list_to_slice: list[str]):
        self._slice_size = slice_size
        self._current_position = 0
        self._some_list_to_slice = some_list_to_slice

    def slide_forward(self, slide_amount: int):
        if not self.end_of_list():
            self._current_position = self._current_position + 1

    def slice(self) -> list[str]:
        slice_boundary_start, slice_boundary_end = self.boundary()
        return self._some_list_to_slice[slice_boundary_start:slice_boundary_end]

    def boundary(self) -> tuple[int, int]:
        return (self._current_position, self._current_position + self._slice_size)

    def end_of_list(self) -> bool:
        _, slice_boundary_end = self.boundary()
        return slice_boundary_end >= len(self._some_list_to_slice)


def is_marker(candidate_marker: list[str]) -> bool:
    return len(set(candidate_marker)) == len(candidate_marker)


def find_marker(datastream_buffer: str, marker_size: int) -> int:
    sliding_slice = SlidingSlice(marker_size, datastream_buffer)

    while not sliding_slice.end_of_list():
        if is_marker(sliding_slice.slice()):
            _, slice_boundary_end = sliding_slice.boundary()
            return slice_boundary_end
        else:
            sliding_slice.slide_forward(1)

    return -1


def part_one(datastream_buffer: str) -> int:
    return find_marker(datastream_buffer, 4)

def part_two(datastream_buffer: str) -> int:
    return find_marker(datastream_buffer, 14)