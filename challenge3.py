# To help yourself get to and from your bunk every day, write a function called solution(src, dest) 
# which takes in two parameters: the source square, on which you start, and the destination square, 
# which is where you need to land to solve the puzzle.  The function should return an integer 
# representing the smallest number of moves it will take for you to travel from the source square 
# to the destination square using a chess knight's moves (that is, two squares in any direction 
# immediately followed by one square perpendicular to that direction, or vice versa, in an "L" 
# shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, 
# and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

def solution(src, dest):
    board = [
        [0,  1,  2,  3,  4,  5,  6,  7],
        [8,  9,  10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29, 30, 31],
        [32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47],
        [48, 49, 50, 51, 52, 53, 54, 55],
        [56, 57, 58, 59, 60, 61, 62, 63]
    ]
    
    visited = []
    queue = [(src, 0)]

    while queue:
        node = queue.pop(0)
        value = node[0]
        steps = node[1]

        visited.append(value)

        if value == dest:
            return steps

        moves = get_next_moves(value, board)
        for move in moves:
            if move not in visited:
                queue.append((move, steps + 1))
    
    return None

def get_next_moves(src, board):
    src_x, src_y = _get_board_pos(src)
    next_moves = []

    # Up
    # two rows above
    if src_y > 1:
        # not the left edge
        if src_x > 1:
            up_left = board[src_y-2][src_x-1]
            next_moves.append(up_left)

        # not the right edge
        if src_x < 7:
            up_right = board[src_y-2][src_x+1]
            next_moves.append(up_right)

    # Down
    # two rows below
    if src_y < 6:
        # not the left edge
        if src_x > 0:
            down_left = board[src_y+2][src_x-1]
            next_moves.append(down_left)

        # not the right edge
        if src_x < 7:
            down_right = board[src_y+2][src_x+1]
            next_moves.append(down_right)

    # Left
    # two columns to left
    if src_x > 1:
        # not the top edge
        if src_y > 0:
            left_up = board[src_y-1][src_x-2]
            next_moves.append(left_up)

        # not the bottom edge
        if src < 7:
            left_down = board[src_y+1][src_x-2]
            next_moves.append(left_down)

    # Right
    # two columns to right
    if src_x < 6:
        # not the top edge
        if src_y > 0:
            right_up = board[src_y-1][src_x+2]
            next_moves.append(right_up)

        # not the bottom edge
        if src_y < 7:
            right_down = board[src_y+1][src_x+2]
            next_moves.append(right_down)
    return next_moves

    
def _get_board_pos(n):
    y = n // 8
    x = n - y * 8
    return x, y