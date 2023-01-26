import sys

class Problem:

    # Initial state
    initial_row_1 = []
    initial_row_2 = []
    initial_row_3 = []

    # Goal state
    goal_row_1 = [1, 2, 3]
    goal_row_2 = [4, 5, 6]
    goal_row_3 = [7, 8, 0]

    operators = []

    def __init__(self, size):
        #print(f'Initializing problem with size {size}')
        self.size = size

if __name__ == '__main__':
    sys.exit('Don\'t run problem.py directly!')