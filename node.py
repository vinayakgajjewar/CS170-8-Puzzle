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

    # Utility method for string representation of the node
    def __str__(self):
        return f'{self.row1[0]} {self.row1[1]} {self.row1[2]}\n{self.row2[0]} {self.row2[1]} {self.row2[2]}\n{self.row3[0]} {self.row3[1]} {self.row3[2]}'

    # Utility function to get the tile at a specified row and column
    # Rows and columns are 1-indexed
    def get_tile(self, row, col):
        if (row not in [1, 2, 3]) or (col not in [1, 2, 3]):
            sys.exit('Error: row/col value not in range.')
        if row == 1:
            return self.row1[col - 1]
        elif row == 2:
            return self.row2[col - 1]
        elif row == 3:
            return self.row3[col - 1]

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

        # Check if the operation is legal
        if self.is_blank_up_legal() == False:
            sys.exit('Error: can\'t move the blank up in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[0] == 2:
            
            # The blank is in the 2nd row, so let's figure out what tile is on top of it
            top_tile = self.get_tile(1, blank_loc[1])

            # Switch the tiles
            self.row1[blank_loc[1] - 1] = 0
            self.row2[blank_loc[1] - 1] = top_tile
        elif blank_loc[0] == 3:
            
            # The blank is in the 3rd row, so let's figure out what tile is on top of it
            top_tile = self.get_tile(2, blank_loc[1])

            # Switch the tiles
            self.row2[blank_loc[1] - 1] = 0
            self.row3[blank_loc[1] - 1] = top_tile
        else:
            sys.exit("We should not be here.")

        new_row1 = self.row1
        new_row2 = self.row2
        new_row3 = self.row3

        return [new_row1, new_row2, new_row3]

    def blank_down(self):

        # Check if the operation is legal
        if self.is_blank_down_legal() == False:
            sys.exit('Error: can\'t move the blank down in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[0] == 1:

            # The blank is in the 1st row, so let's figure out what tile is under it
            bottom_tile = self.get_tile(2, blank_loc[1])

            # Switch the tiles
            self.row2[blank_loc[1] - 1] = 0
            self.row1[blank_loc[1] - 1] = bottom_tile
        elif blank_loc[0] == 2:
            
            # The blank is in the 2nd row, so let's figure out what tile is under it
            bottom_tile = self.get_tile(3, blank_loc[1])

            # Switch the tiles
            self.row3[blank_loc[1] - 1] = 0
            self.row2[blank_loc[1] - 1] = 0
        else:
            sys.exit('We should definitely not be here.')

        new_row1 = self.row1
        new_row2 = self.row2
        new_row3 = self.row3
        return [new_row1, new_row2, new_row3]

    def blank_left(self):

        # Check if the operation is legal
        if self.is_blank_left_legal() == False:
            sys.exit('Error: can\'t move the blank left in this configuration.')

        new_row1 = self.row1
        new_row2 = self.row2
        new_row3 = self.row3
        return [new_row1, new_row2, new_row3]

    def blank_right(self):

        # Check if the operation is legal
        if self.is_blank_right_legal() == False:
            sys.exit('Error: can\'t move the blank right in this configuration.')

        new_row1 = self.row1
        new_row2 = self.row2
        new_row3 = self.row3
        return [new_row1, new_row2, new_row3]

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