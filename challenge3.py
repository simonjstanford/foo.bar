def solution(src, dest):
    '''
    To help yourself get to and from your bunk every day, write a function called solution(src, dest) 
    which takes in two parameters: the source square, on which you start, and the destination square, 
    which is where you need to land to solve the puzzle.  The function should return an integer 
    representing the smallest number of moves it will take for you to travel from the source square 
    to the destination square using a chess knight's moves (that is, two squares in any direction 
    immediately followed by one square perpendicular to that direction, or vice versa, in an "L" 
    shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, 
    and are numbered like the example chessboard below:

    -------------------------
    | 0| 1| 2| 3| 4| 5| 6| 7|
    -------------------------
    | 8| 9|10|11|12|13|14|15|
    -------------------------
    |16|17|18|19|20|21|22|23|
    -------------------------
    |24|25|26|27|28|29|30|31|
    -------------------------
    |32|33|34|35|36|37|38|39|
    -------------------------
    |40|41|42|43|44|45|46|47|
    -------------------------
    |48|49|50|51|52|53|54|55|
    -------------------------
    |56|57|58|59|60|61|62|63|
    -------------------------
    '''

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

    if src == dest:
        return 0

    # something like get all possible next positions and track the progress
    # each branch produces an array of position history
    # you can only move to a position you haven't already been to
    # when you're at the position you want to be then return the length of the array

    src_x, src_y = _get_board_pos(src)
    next_moves = []

    up_left = None
    if src_y > 1 and src_x > 0:
        up_left = board[src_y-2][src_x-1]
        next_moves.append(up_left)

    up_right = None
    if src_y > 1 and src_x < 7:
        up_right = board[src_y-2][src_x+1]
        next_moves.append(up_right)

    right_up = None
    if src_y < 6 and src_x > 0:
        right_up = board[src_y-1][src_x+2]
        next_moves.append(right_up)

    right_down = None
    if src_y < 6 and src_x < 7:
        right_down = board[src_y+1][src_x+2]
        next_moves.append(right_down)

    left_up = None
    
def _get_board_pos(n):
    y = n // 8
    x = n - y * 8
    return x, y