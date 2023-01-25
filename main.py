import sys
import problem
import solver

# TODO: We want the user to be able to enter an arbitrary initial state
# For now, we will hardcode an arbitrary initial state
# We will use 0 to represent the blank space
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 0, 8]
initial_state = [row1, row2, row3]

# Initialize problem and solver
eight_puzzle = problem.Problem(8)
my_solver = solver.Solver()

print('Welcome to vgajj002\'s 8-puzzle solver.')

# Choose whether to use the default or a custom initial state
print('Type \'1\' to use a default puzzle or type \'2\' to enter your own puzzle.')
initial_state_response = input()
if initial_state_response == '1':
    pass
elif initial_state_response == '2':
    print('Enter your puzzle, using a 0 to represent the blank.')
    print('Enter the first row, using spaces or tabs between numbers: ', end='')
    first_row_input = input()
    print('Enter the second row, using spaces or tabs between numbers: ', end='')
    second_row_input = input()
    print('Enter the third row, using spaces or tabs between numbers: ', end='')
    third_row_input = input()
else:
    sys.exit('Invalid response. Goodbye!')

# Get choice of algorithm from user
print('Enter your choice of algorithm.')
print('1. Uniform cost search (h(n) = 0).')
print('2. A* with misplaced tile heuristic.')
print('3. A* with euclidean distance heuristic.')
algorithm_choice = input()