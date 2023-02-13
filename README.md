# CS170 8-Puzzle Solver

This project uses Python 3.10.6. To run the solver, execute the following command and follow the prompts.

```
python3 main.py
```

## Design

For this project, I implemented graph search instead of tree search. I implemented the explored set using a native Python list and the frontier as a priority queue using the 'heapq' package.

## Challenges

One challenge I faced while coding this project is that early on in the project, I hard-coded the number of rows of the puzzle to equal three. This decision made the code much longer and much less abstract than it could have been. Another challenge I faced was figuring out when Python is pass-by-reference or pass-by-value. Many bugs I faced while coding this project came from mistakenly modifying a value across variables instead of performing a shallow copy.

## Heuristic function comparison

While testing the solver, I found that the Euclidean distance heuristic outperforms the misplaced tile heuristic on both the number of expanded nodes and the maximum frontier size. I also found that the heuristic choice only matters for the more complex initial configurations. Any heuristic will yield approximately the same result if the problem is reasonably trivial.

## Findings