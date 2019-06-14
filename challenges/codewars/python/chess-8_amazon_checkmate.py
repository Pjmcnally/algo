"""Solution for https://www.codewars.com/kata/5897f30d948beb78580000b2.

Work in progress.
"""

# TODO: Continue refactor. Add board class.
def amazon_check_mate(king, amazon):
    """Calculate state of board with Amazon Mate."""
    # Build board
    chess_board = {}
    for y in range(8):
        for x in range(8):
            chess_board[x, y] = None

    # Add King and Amazon Locations
    king_x, king_y = convert_to_xy(king)
    chess_board[(king_x, king_y)] = "K"
    amazon_x, amazon_y = convert_to_xy(amazon)
    chess_board[(amazon_x, amazon_y)] = "A"

    for (square_x, square_y), val in chess_board.items():
        if val is not None:
            continue

        # Check if square is within 1 square of king (illegal location)
        if (
            king_x - 1 <= square_x <= king_x + 1
            and king_y - 1 <= square_y <= king_y + 1
        ):
            val = None
        # Check if square on same row
        elif square_x == amazon_x:
            val = True
        # Check if square is in same column
        elif square_y == amazon_y:
            val = True
        # Check if square is on either diagonal
        elif (
            square_x + square_y == amazon_x + amazon_y
            or square_x - square_y == amazon_x - amazon_y
        ):
            val = True
        # Check if square is within 2 squares of Amazon (covers knight moves)
        elif (
            amazon_x - 2 <= square_x <= amazon_x + 2
            and amazon_y - 2 <= square_y <= amazon_y + 2
        ):
            val = True
        else:
            val = False

        chess_board[(square_x, square_y)] = val

    print("this is a test line")


class Square:
    def __init__(self, x=None, y=None, notation=None, status=None, contains=None):
        self.x = x
        self.y = y
        self.notation = notation
        self.status = status
        self.contains = contains

    def __str__(self):
        return

    @classmethod
    def from_xy(x, y):
        temp = Square()
        temp.x = x
        temp.y = y
        temp.notation = Square.convert_xy_to_note(x, y)
        temp.status = None
        temp.contains = None

        return temp

    @classmethod
    def from_note(note):
        temp = Square()

    @classmethod
    def convert_note_to_xy(self, pos):
        """Convert 'e4' chess notation to x, y notation."""
        x = ord(pos[0]) - ord("a")
        y = int(pos[1]) - 1
        return (x, y)

    @classmethod
    def convert_xy_to_note(self, x, y):
        let = chr(x + 97)
        num = y + 1
        return f"{let}{num}"


amazon_check_mate("a1", "e4")
