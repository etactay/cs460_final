# Development Log – The Torchbearer

**Student Name:** Eufrecino R. Tactay III
**Student ID:** 828198534

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/12]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_I first read the scenario to understand the overall problem structure to see what type of algorithm I should use for the dungeon._
Afterwards, I noticed that this scenario had more complexity to its nature than just a normal shortest-path problem. This is because
the final fuel consumption is also dependent on the order in which the relic chambers are visited. Overall, I think the recursive
functions and pruning parts would be the most difficult because it requires us to track all possible routes to find the optimal solution.
I plan to test it by using the provided test and then adding a couple small graphs to ensure that the calculations are done properly.

---

## Entry 2 – [5/12]: [Unreachable Exits]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_While I was testing the algorithm, I realized that not every graph would have a valid path from the relics to the exit. Initially,_
I was only focused on finding the cheapest order of relic visits, but one of the tests (3) revealed that the algorithm also needed
to be able to handle scenarios where the exit cannot be reached. To solve this issue, I made sure to include a line that stored
unreachable paths as 'float('inf')'. This made it so that when we evaluated the possible routes, the routes which had an unreachable
segment wouldn't be considered for the best solution.

---

## Entry 3 – [5/13]: [Search and Route Exploration]

_Today I finished Part 4 and started with the implementation for Parts 5 and 6. I worked on designing the recursive search which is used_
_to help us look at different relic visitation orders and started in the 'explore()' helper function. One thing I did focus on was_
_understanding how the backtracking works, particularly, the removing and re-adding relics after the recursive calls. I also inlcuded_
_the pruning logic which skips paths  that already cost more than the best solution found so far. While doing so, I also traced the_
_recursive calls manually because it was really easy to lost track of how the visitation order and remaining sets were changing during recursion._ 

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|----------------|
| Part 1: Problem Analysis | ~1             |
| Part 2: Precomputation Design | ~5 - 6         |
| Part 3: Algorithm Correctness | ~1             |
| Part 4: Search Design | ~0:45 - 1:00   |
| Part 5: State and Search Space | ~3             |
| Part 6: Pruning | ~1             |
| Part 7: Implementation |                |
| README and DEVLOG writing |                |
| **Total** |                |
