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
print('Type \'1\' to use a default puzzle or type \'2\' to enter your own puzzle.')
response = input()
if response == '1':
    pass
elif response == '2':
    print('Enter your puzzle, using a 0 to represent the blank.')
    print('Enter the first row, using spaces or tabs between numbers: ')
    print('Enter the second row, using spaces or tabs between numbers: ')
    print('Enter the third row, using spaces or tabs between numbers: ')
else:
    sys.exit('Invalid response. Goodbye!')