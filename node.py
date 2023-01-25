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

    def is_blank_up_legal(self):
        pass

    def is_blank_down_legal(self):
        pass

    def is_blank_left_legal(self):
        pass

    def is_blank_right_legal(self):
        pass

if __name__ == '__main__':
    sys.exit('Don\'t run node.py directly!')