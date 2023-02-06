# test_tree.py
# Test script for Tree class

import tree

row1 = [1, 0, 3]
row2 = [4, 2, 6]
row3 = [7, 5, 8]
init_state = [row1, row2, row3]
t1 = tree.Tree(init_state)
while True:
    if t1.is_frontier_empty():
        print('We have not found a solution.')
        break
    leaf = t1.pop_leaf_node()
    print('Popped the following node from the frontier.')
    print(leaf)
    if leaf.is_goal_state():
        print('We have found the solution.')
        break
    t1.add_to_explored(leaf)
    expanded_nodes = leaf.expand()