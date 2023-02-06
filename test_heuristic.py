# test_heuristic.py

import node

row1 = [2, 4, 3]
row2 = [1, 6, 0]
row3 = [7, 5, 8]
n1 = node.Node(row1, row2, row3)

# Misplaced tile heuristic
# Should be 7
print(f'h(n) with misplaced tile is {n1.misplaced_tile_heuristic()}.')

# Euclidean distance heuristic
print(f'h(n) with euclidean distance is {n1.euclidean_distance_heuristic()}.')