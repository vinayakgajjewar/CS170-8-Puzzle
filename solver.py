# solver.py

import sys
import tree

# This class is designed to run the graph search algorithm on a problem tree
class Solver:

    # This class attribute will store the initial state of the puzzle as a 3x3 list
    problem = []

    # Constructor
    def __init__(self, problem):
        self.problem = problem

    # This function will run graph search on the problem passed into it
    def graph_search(self):

        # Initialize problem tree
        t1 = tree.Tree(self.problem)

        # Keep track of the number of expanded nodes
        num_nodes_expanded = 0

        # Loop until we either find a solution or exhaust all possibilities
        while True:

            # If the frontier is empty, return a failure
            if t1.is_frontier_empty():
                print('We have not found a solution.')
                break
        
            # Pick a leaf node and remove it from the frontier
            leaf = t1.pop_leaf_node()
            print('Popped the following node from the frontier:')
            print(leaf)

            # If the node contains a goal state, return the corresponding solution
            if leaf.is_goal_state():
                print('We have found the solution.')
                break

            # Add the node to the explored set
            t1.add_to_explored(leaf)

            # Expand the chosen node and add the resulting node to the frontier
            # Only if they're not already in the frontier or the explored set
            expanded_nodes = leaf.expand()
            for node in expanded_nodes:

                # TODO: check if this is in the right place
                num_nodes_expanded += 1
                if node not in t1.frontier or node not in t1.explored_set:
                    t1.add_to_frontier(node)
        
        # How many nodes did we expand?
        print(f'We expanded {num_nodes_expanded} nodes.')

        # What was the max number of nodes in the frontier at any one time?
        # TODO
        print('The max number of nodes in the frontier at any one time was X.')

        # What is the depth of the solution?
        # TODO
        print('The depth of the solution is ZZZ.')

if __name__ == '__main__':
    sys.exit('Don\'t run solver.py directly!')