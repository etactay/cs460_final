# Development Log – The Torchbearer

**Student Name:** Eufrecino R. Tactay III
**Student ID:** 828198534



---

## Entry 1 – [05/12]: Initial Plan



_I first read the scenario to understand the overall problem structure to see what type of algorithm I should use for the dungeon._
Afterwards, I noticed that this scenario had more complexity to its nature than just a normal shortest-path problem. This is because
the final fuel consumption is also dependent on the order in which the relic chambers are visited. Overall, I think the recursive
functions and pruning parts would be the most difficult because it requires us to track all possible routes to find the optimal solution.
I plan to test it by using the provided test and then adding a couple small graphs to ensure that the calculations are done properly.

---

## Entry 2 – [5/12]: [Unreachable Exits]



_While I was testing the algorithm, I realized that not every graph would have a valid path from the relics to the exit. Initially,_
I was only focused on finding the cheapest order of relic visits, but one of the tests (3) revealed that the algorithm also needed
to be able to handle scenarios where the exit cannot be reached. To solve this issue, I made sure to include a line that stored
unreachable paths as 'float('inf')'. This made it so that when we evaluated the possible routes, the routes which had an unreachable
segment wouldn't be considered for the best solution.

---

## Entry 3 – [5/13]: [Search and Route Exploration]

_Today I finished Part 4 and started with the implementation for Parts 5 and 6. I worked on designing the recursive search which is used_
_to help us look at different relic visitation orders and started in the 'explore()' helper function. One thing I did focus on was_
_understanding how the backtracking works, particularly, the removing and re-adding relics after the recursive calls. I also included_
_the pruning logic which skips paths  that already cost more than the best solution found so far. While doing so, I also traced the_
_recursive calls manually because it was really easy to lose track of how the visitation order and remaining sets were changing during recursion._ 

---

## Entry 4 – [5/14]: Post-Implementation Reflection



_After completing all the parts, I think what gave me the most problems was the recursive exploration because it needed to have the_
_capabilities to track remaining relics and total fuel cost during backtracking. Something that I could try improving would be the_
_pruning strategy so that the algorithm could avoid exploring more unnecessary routes earlier._

---

## Final Entry – [5/14]: Time Estimate



| Part | Estimated Hours     |
|---|---------------------|
| Part 1: Problem Analysis | ~1          hr      |
| Part 2: Precomputation Design | ~5 - 6    hrs       |
| Part 3: Algorithm Correctness | ~1    hr            |
| Part 4: Search Design | ~0:45 - 1:00    hrs |
| Part 5: State and Search Space | ~3     hr           |
| Part 6: Pruning | ~1          hr      |
| Part 7: Implementation | ~2 hrs              |
| README and DEVLOG writing | ~2 hrs              |
| **Total** | ~17 hrs             |

- Note: Part 7 was mostly done alongside the different parts, so time taken  has been included in the estimated hrs of each corresponding section
- Note: README + DEVLOG writing was done similarly to Part 7