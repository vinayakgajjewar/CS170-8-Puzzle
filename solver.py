import sys
import heapq

class Solver:
    def __init__(self):
        #print('Initializing solver')
        pass

    # This function will run graph search on the problem passed into it
    def graph_search(self, problem):

        # TODO: initialize frontier using initial state of problem
        frontier = []
        heapq.heapify(frontier)

        # Initialize empty explored set
        explored_set = []

        while True:

            # If the frontier is empty, return a failure
            if len(frontier) == 0:
                print("Could not find a solution.")
            
            # Pick a leaf node and remove it from the frontier

            # If the node contains a goal state, return the corresponding solution

            # Add the node to the explored set

            # Expand the chosen node and add the resulting nodes to the frontier
            # Only if they're not already in the frontier or the explored set

if __name__ == '__main__':
    sys.exit('Don\'t run solver.py directly!')