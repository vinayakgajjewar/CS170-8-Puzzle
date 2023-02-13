import sys
import heapq
import node

class Tree:

    # Explored set
    explored_set = []

    # Frontier
    # This will be implemented as a priority queue
    frontier = []

    # Head node
    # This is the initial state of the problem
    head = None

    # Constructor
    # initial_state is a list of rows representing the initial state of the problem
    # algorithm has 3 possible values:
    # "uniform-cost"
    # "a-star-misplaced-tile"
    # "a-star-euclidean-distance"
    def __init__(self, initial_state, algorithm):

        # Create the initial node
        init_row1 = initial_state[0]
        init_row2 = initial_state[1]
        init_row3 = initial_state[2]
        head = node.Node(init_row1, init_row2, init_row3, algorithm)

        # Initialize the frontier with the initial state of the problem
        heapq.heapify(self.frontier)
        heapq.heappush(self.frontier, head)

    # Utility method to check if the frontier is empty
    # Return true if the frontier is empty
    # Return false if there are nodes in the frontier
    def is_frontier_empty(self):
        if len(self.frontier) == 0:
            return True
        else:
            return False
    
    # Pop a leaf node from the frontier
    def pop_leaf_node(self):
        return heapq.heappop(self.frontier)

    # Add a node to the explored set
    def add_to_explored(self, node):
        self.frontier.append(node)
    
    # Add a node to the frontier
    def add_to_frontier(self, node):
        heapq.heappush(self.frontier, node)


if __name__ == '__main__':
    sys.exit('Don\'t run tree.py directly!')