# node.py

import sys
import math

class Node:

    # Parent node
    parent = None

    # Children nodes
    children = None

    # These class attributes hold the puzzle state in the current node
    row1 = []
    row2 = []
    row3 = []

    # Implement '<' operator so that we can use a priority queue to store Nodes
    def __lt__(self, other):
        my_val = self.misplaced_tile_heuristic()
        other_val = other.misplaced_tile_heuristic()
        if my_val < other_val:
            return True
        else:
            return False

    # Constructor
    def __init__(self, row1, row2, row3):
        self.children = []
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

    # Utility method for string representation of the node
    def __str__(self):

        # Pretty-print the board state
        return f'{self.row1[0]} {self.row1[1]} {self.row1[2]}\n{self.row2[0]} {self.row2[1]} {self.row2[2]}\n{self.row3[0]} {self.row3[1]} {self.row3[2]}'

    # Expand the current node
    # Return a list of all resulting nodes
    # TODO: update each resulting node with its parent
    def expand(self):
        expanded_nodes = []

        # Check if we can move the blank up
        if self.is_blank_up_legal():
            blank_up_rows = self.blank_up()
            blank_up_node = Node(blank_up_rows[0], blank_up_rows[1], blank_up_rows[2])
            expanded_nodes.append(blank_up_node)

        # Check if we can move the blank down
        if self.is_blank_down_legal():
            blank_down_rows = self.blank_down()
            blank_down_node = Node(blank_down_rows[0], blank_down_rows[1], blank_down_rows[2])
            expanded_nodes.append(blank_down_node)

        # Check if we can move the blank left
        if self.is_blank_left_legal():
            blank_left_rows = self.blank_left()
            blank_left_node = Node(blank_left_rows[0], blank_left_rows[1], blank_left_rows[2])
            expanded_nodes.append(blank_left_node)

        # Check if we can move the blank right
        if self.is_blank_right_legal():
            blank_right_rows = self.blank_right()
            blank_right_node = Node(blank_right_rows[0], blank_right_rows[1], blank_right_rows[2])
            expanded_nodes.append(blank_right_node)
        
        # Loop through each node and update its parent properly
        # This is so that we can reconstruct the goal path later
        for node in expanded_nodes:
            node.parent = self

        # Return all expanded nodes
        return expanded_nodes

    # Check if the node is the goal state
    # Return true if it is
    # Return false if it isn't
    def is_goal_state(self):
        if self.row1 != [1, 2, 3]:
            return False
        if self.row2 != [4, 5, 6]:
            return False
        if self.row3 != [7, 8, 0]:
            return False
        return True

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

        new_row1 = self.row1.copy()
        new_row2 = self.row2.copy()
        new_row3 = self.row3.copy()

        # Check if the operation is legal
        if self.is_blank_up_legal() == False:
            sys.exit('Error: can\'t move the blank up in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[0] == 2:

            # The blank is in the 2nd row, so let's figure out what tile is on top of it
            top_tile = self.get_tile(1, blank_loc[1])

            # Switch the tiles
            new_row1[blank_loc[1] - 1] = 0
            new_row2[blank_loc[1] - 1] = top_tile
        elif blank_loc[0] == 3:
            
            # The blank is in the 3rd row, so let's figure out what tile is on top of it
            top_tile = self.get_tile(2, blank_loc[1])

            # Switch the tiles
            new_row2[blank_loc[1] - 1] = 0
            new_row3[blank_loc[1] - 1] = top_tile
        else:
            sys.exit("We should not be here.")

        return [new_row1, new_row2, new_row3]

    def blank_down(self):

        new_row1 = self.row1.copy()
        new_row2 = self.row2.copy()
        new_row3 = self.row3.copy()

        # Check if the operation is legal
        if self.is_blank_down_legal() == False:
            sys.exit('Error: can\'t move the blank down in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[0] == 1:

            # The blank is in the 1st row, so let's figure out what tile is under it
            bottom_tile = self.get_tile(2, blank_loc[1])

            # Switch the tiles
            new_row2[blank_loc[1] - 1] = 0
            new_row1[blank_loc[1] - 1] = bottom_tile
        elif blank_loc[0] == 2:
            
            # The blank is in the 2nd row, so let's figure out what tile is under it
            bottom_tile = self.get_tile(3, blank_loc[1])

            # Switch the tiles
            new_row3[blank_loc[1] - 1] = 0
            new_row2[blank_loc[1] - 1] = bottom_tile
        else:
            sys.exit('We should definitely not be here.')

        return [new_row1, new_row2, new_row3]

    def blank_left(self):

        new_row1 = self.row1.copy()
        new_row2 = self.row2.copy()
        new_row3 = self.row3.copy()

        # Check if the operation is legal
        if self.is_blank_left_legal() == False:
            sys.exit('Error: can\'t move the blank left in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[1] == 2:

            # The blank is in the 2nd column, so let's figure out what tile is to the left of it
            left_tile = self.get_tile(blank_loc[0], 1)

            # Switch the tiles
            if blank_loc[0] == 1:
                new_row1[0] = 0
                new_row1[1] = left_tile
            elif blank_loc[0] == 2:
                new_row2[0] = 0
                new_row2[1] = left_tile
            elif blank_loc[0] == 3:
                new_row3[0] = 0
                new_row3[1] = left_tile
            else:
                sys.exit('We really should not be here.')
        elif blank_loc[1] == 3:

            # The blank is in the 3rd column, so let's figure out what tile is to the left of it
            left_tile = self.get_tile(blank_loc[0], 2)

            # Switch the tiles
            if blank_loc[0] == 1:
                new_row1[1] = 0
                new_row1[2] = left_tile
            elif blank_loc[0] == 2:
                new_row2[1] = 0
                new_row2[2] = left_tile
            elif blank_loc[0] == 3:
                new_row3[1] = 0
                new_row3[2] = left_tile
            else:
                sys.exit('We really should not be here.')
        else:
            sys.exit('We should not be here.')

        return [new_row1, new_row2, new_row3]

    def blank_right(self):

        new_row1 = self.row1.copy()
        new_row2 = self.row2.copy()
        new_row3 = self.row3.copy()

        # Check if the operation is legal
        if self.is_blank_right_legal() == False:
            sys.exit('Error: can\'t move the blank right in this configuration.')

        # Find the location of the blank
        blank_loc = self.locate_tile(0)

        if blank_loc[1] == 1:

            # The blank is in the 1st column, so let's figure out what tile is to the right of it
            right_tile = self.get_tile(blank_loc[0], 2)

            # Switch the tiles
            if blank_loc[0] == 1:
                new_row1[1] = 0
                new_row1[0] = right_tile
            elif blank_loc[0] == 2:
                new_row2[1] = 0
                new_row2[0] = right_tile
            elif blank_loc[0] == 3:
                new_row3[1] = 0
                new_row3[0] = right_tile
            else:
                sys.exit('We should really not be here.')
        elif blank_loc[1] == 2:

            # The blank is in the 2nd column, so let's figure out what tile is to the right of it
            right_tile = self.get_tile(blank_loc[0], 3)

            # Switch the tiles
            if blank_loc[0] == 1:
                new_row1[2] = 0
                new_row1[1] = right_tile
            elif blank_loc[0] == 2:
                new_row2[2] = 0
                new_row2[1] = right_tile
            elif blank_loc[0] == 3:
                new_row3[2] = 0
                new_row3[1] = right_tile
            else:
                sys.exit('We really should not be here.')
        else:
            sys.exit('We should not be here.')

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

    # The below methods are for heuristics

    # Misplaced tile heuristic
    # Just return the number of tiles that aren't in the proper spot
    def misplaced_tile_heuristic(self):

        # To keep track of the number of misplaced tiles
        count = 0
        
        # There is a more elegant way to do this but I don't care
        if self.row1[0] != 1:
            count += 1
        if self.row1[1] != 2:
            count += 1
        if self.row1[2] != 3:
            count += 1
        if self.row2[0] != 4:
            count += 1
        if self.row2[1] != 5:
            count += 1
        if self.row2[2] != 6:
            count += 1
        if self.row3[0] != 7:
            count += 1
        if self.row3[1] != 8:
            count += 1
        if self.row3[2] != 0:
            count += 1
        
        return count

    # Helper function for the Euclidean distance heuristic
    # loc1 and loc2 are coords in the form [x, y]
    def calc_distance(self, loc1, loc2):
        return math.sqrt((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2)
    
    # Helper function for the Euclidean distance heuristic
    # Given a tile number, return the location it should be in as [x, y]
    def get_correct_pos(self, tile):
        row = 0
        col = 0

        # Figure out what row
        if tile in [1, 2, 3]:
            row = 1
        elif tile in [4, 5, 6]:
            row = 2
        elif tile in [7, 8, 0]:
            row = 3
        else:
            sys.exit('Invalid input.')

        # Figure out what col
        if tile in [1, 4, 7]:
            col = 1
        elif tile in [2, 5, 8]:
            col = 2
        elif tile in [3, 6, 0]:
            col = 3
        else:
            sys.exit('Invalid input.')

        # Return the goal state location of the requested tile
        loc = [row, col]
        return loc

    # Euclidean distance heuristic
    # Sum up the Euclidean distances of each tile to where it should be
    def euclidean_distance_heuristic(self):

        # Sum of distances
        sum = 0

        # Loop through all tiles
        for i in range(9):
            dist = self.calc_distance(self.locate_tile(i), self.get_correct_pos(i))
            #print(f'Distance for {i} tile: {dist}.')
            sum += dist

        return sum
    
    # Hahaha
    def uniform_cost_heuristic(self):
        return 0
    
    # Trace the solution path
    def trace(self):

        # Recursion
        if (self.parent):
            return 1 + self.parent.trace()
        else:
            return 0

if __name__ == '__main__':
    sys.exit('Don\'t run node.py directly!')