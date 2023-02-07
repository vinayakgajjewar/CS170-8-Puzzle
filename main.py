import sys
import solver

# Initial state of the problem
# 3x3 list
initial_state = []

print('Welcome to vgajj002\'s 8-puzzle solver.')

# Choose whether to use the default or a custom initial state
print('Type \'1\' to use a default puzzle or type \'2\' to enter your own puzzle.')
initial_state_response = input()
if initial_state_response == '1':
    row1 = [1, 0, 3]
    row2 = [4, 2, 6]
    row3 = [7, 5, 8]
    initial_state = [row1, row2, row3]
elif initial_state_response == '2':
    print('Enter your puzzle, using a 0 to represent the blank.')
    print('Enter the first row, using spaces between numbers: ', end='')
    first_row_input = input()
    print('Enter the second row, using spaces between numbers: ', end='')
    second_row_input = input()
    print('Enter the third row, using spaces between numbers: ', end='')
    third_row_input = input()

    # Convert text input into numeric rows
    str_row1 = first_row_input.split(' ')
    str_row2 = second_row_input.split(' ')
    str_row3 = third_row_input.split(' ')

    # Smart way of converting strings to ints
    row1 = [eval(i) for i in str_row1]
    row2 = [eval(i) for i in str_row2]
    row3 = [eval(i) for i in str_row3]
    initial_state = [row1, row2, row3]
else:
    sys.exit('Invalid response. Goodbye!')

# Get choice of algorithm from user
print('Enter your choice of algorithm.')
print('1. Uniform cost search (h(n) = 0).')
print('2. A* with misplaced tile heuristic.')
print('3. A* with euclidean distance heuristic.')

# TODO: we need this choice to actually matter
algorithm_choice = input()

# Initialize solver and perform graph search
s = solver.Solver(initial_state)
s.graph_search()