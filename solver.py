# solver.py

import sys
import tree

# This class is designed to run the graph search algorithm on a problem tree
class Solver:

    # This class attribute will store the initial state of the puzzle as a 3x3 list
    problem = []

    # This class attribute tells us which algorithm to use
    # '1': Uniform cost search (h(n) = 0)
    # '2': A* with misplaced tile heuristic
    # '3': A* with Euclidean distance heuristic
    alg = -1

    # Constructor
    def __init__(self, problem, alg):
        self.problem = problem
        self.alg = alg

    # This function will run graph search on the problem passed into it
    def graph_search(self):

        # Initialize problem tree
        t1 = tree.Tree(self.problem)

        # Keep track of the number of expanded nodes
        num_nodes_expanded = 0

        # Keep track of the max number of nodes in the frontier
        max_nodes_in_frontier = 0

        # Loop until we either find a solution or exhaust all possibilities
        while True:

            # If the frontier is empty, return a failure
            if t1.is_frontier_empty():
                print('We have not found a solution.')
                break

            # Pick a leaf node and remove it from the frontier
            leaf = t1.pop_leaf_node()
            g_n = leaf.g_n
            h_n = leaf.euclidean_distance_heuristic()
            print(f'Popped the following node from the frontier (g(n)={g_n}, h(n)={h_n}):')
            print(leaf)

            # If the node contains a goal state, return the corresponding solution
            if leaf.is_goal_state():
                print('We have found the solution.')

                # Now that we found the solution, let's compute the solution depth
                # This is inefficient and unnecessary but it works
                depth = leaf.compute_depth()
                print(f'The solution is at depth {depth}.')

                # Let's compute the path
                trace = leaf.trace()
                print('Solution path:')
                print(trace)
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

                    # Update max_nodes_in_frontier if necessary
                    if max_nodes_in_frontier < len(t1.frontier):
                        max_nodes_in_frontier = len(t1.frontier)
        
        # How many nodes did we expand?
        print(f'We expanded {num_nodes_expanded} nodes.')

        # What was the max number of nodes in the frontier at any one time?
        print(f'The max number of nodes in the frontier at any one time was {max_nodes_in_frontier}.')

if __name__ == '__main__':
    sys.exit('Don\'t run solver.py directly!')