# test_node.py
# Script to test Node class functionality

import node

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 0]

n1 = node.Node(row1, row2, row3)
print(n1)
print(f'Tile 2 is located at {n1.locate_tile(2)}') # Should be [1, 2]
print(f'The tile at [2, 1] is {n1.get_tile(2, 1)}')

new_rows = n1.blank_up()
n2 = node.Node(new_rows[0], new_rows[1], new_rows[2])
print(n2)