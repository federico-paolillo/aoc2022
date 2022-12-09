import math

def offset(val: int) -> int:
    return +1 if val > 1 else -1 if val < -1 else 0

def chessboard_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    distance = max(abs(x2 - x1), abs(y2 - y1)) 
    return 0 if distance == 0 else distance - 1 # I just need the number of distance "steps" not the numerical distance

def compensating_movement(head_x: int, head_y: int, tail_x: int, tail_y: int) -> tuple[int, int]:
    distance = chessboard_distance(head_x, head_y, tail_x, tail_y)

    if distance == 0:
        return (0, 0)

    x_diff = head_x - tail_x        
    y_diff = head_y - tail_y

    offset_x = offset(x_diff)
    offset_y = offset(y_diff)

    return (x_diff - offset_x, y_diff - offset_y)

def transform(x: int, y: int, ) -> tuple[int, int]:
    return