import sys

class Node:

    # Pointer to parent node
    parent = None

    # These class attributes hold the puzzle state in the current node
    row1 = []
    row2 = []
    row3 = []

    # Constructor
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

    # Utility function to get the row and column of whatever tile we want
    def locate_tile(self, tile):
        if tile not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            sys.exit('Error: trying to find a tile that doesn\'t exist.')
        row = None
        col = None

        # Figure out what row the tile is in
        if tile in self.row1:
            row = 1
        elif tile in self.row2:
            row = 2
        elif tile in self.row3:
            row = 3
        else:
            print('Literally how')
        
        # Figure out what column the tile is in
        if self.row1[0] == tile or self.row2[0] == tile or self.row3[0] == tile:
            col = 1
        elif self.row1[1] == tile or self.row2[1] == tile or self.row3[1] == tile:
            col = 2
        elif self.row1[2] == tile or self.row2[2] == tile or self.row3[2] == tile:
            col = 3
        else:
            print('Bruh how')

        # Return row and column of tile
        return [row, col]

    # The below methods return the puzzle state after the corresponding operation is applied
    # If the operator is not valid, these methods will throw an error and complain

    def blank_up(self):
        pass

    def blank_down(self):
        pass

    def blank_left(self):
        pass

    def blank_right(self):
        pass

    # The below methods check if the corresponding operator is legal given the current puzzle state
    # TODO: rewrite these using locate_tile()

    # If the blank is in the first row, we cannot perform this operation
    def is_blank_up_legal(self):
        if 0 in self.row1:
            return False
        else:
            return True

    # If the blank is in the bottom row, we cannot perform this operation
    def is_blank_down_legal(self):
        if 0 in self.row3:
            return False
        else:
            return True

    # If the blank is in the first column, we cannot perform this operation
    def is_blank_left_legal(self):
        if self.row1[0] == 0 or self.row2[0] == 0 or self.row3[0] == 0:
            return False
        else:
            return True

    # If the blank is in the third column, we cannot perform this operation
    def is_blank_right_legal(self):
        if self.row1[2] == 0 or self.row2[2] == 0 or self.row3[2] == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    sys.exit('Don\'t run node.py directly!')