# test_expansion.py

import node

row1 = [1, 0, 3]
row2 = [4, 2, 6]
row3 = [7, 5, 8]
n1 = node.Node(row1, row2, row3)
print('Initial node:')
print(n1)
expansion = n1.expand()
print('Expansions:')
for node in expansion:
    print(node)
    print()