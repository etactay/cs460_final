# The Torchbearer

**Student Name:** Eufrecino R. Tactay III
**Student ID:** 828198534
**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  _It isn't enough because it only considers the smallest travel distance from the start to every node. Meaning, it doesn't help with choosing an optimal path for visiting every node before exiting._

- **What decision remains after all inter-location costs are known:**
  _After realizing the costs, the path taken from start to finish still needs to be decided while also minimizing the total fuel consumption._

- **Why this requires a search over orders (one sentence):**
  _This requires a search because different orders lead to different fuel costs, therefore, the algorithm must be able to search from different routes to get the minimum cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source                                                                                                      |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| _Spawn node_     | _We start at the spawn, making it vital to find the shortest paths_                                                     |
| _Relics nodes_   | _To help us compare the different routes, we'll need to be able to find the distances from the relic nodes to the exit_ |

### Part 2b: Distance Storage


| Property | Your answer                                      |
|---|--------------------------------------------------|
| Data structure name | Nested Dictionary                                |
| What the keys represent | Source nodes and destination nodes               |
| What the values represent | Contains the minimum fuel cost between the nodes |
| Lookup time complexity | O(1)                                             |
| Why O(1) lookup is possible | It uses a hash table lookup via key              |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** _'k' runs, where k is dependent on the number of source nodes_
- **Cost per run:** _O(E log V)_
- **Total complexity:** _O(k(E log V))_
- **Justification (one line):** _We run Dijkstra's algorithm for each and every selected source node._

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _For all the finalized nodes, their shortest paths have already been determined and cannot be improved._

- **For nodes not yet finalized (not in S):**
  _For nodes that are not finalized yet, the stored distance represents the shortest path currently found using only the finalized nodes in between._

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  - _At initialization, the source node starts with distance 0 and every other node starts at infinity because no shorter paths have been discovered._
  - _This satisfies the invariant since no other paths to other nodes have been found yet._

- **Maintenance : why finalizing the min-dist node is always correct:**
  - _Since all edge weights are nonnegative, the node with the smallest current distance IS the shortest possible path._
  - _Other future paths would have a greater total cost_

- **Termination : what the invariant guarantees when the algorithm ends:**
  - _Once the algorithm finishes, all reachable nodes will contain their correct shortest-path distances in the distance table._

### Part 3c: Why This Matters for the Route Planner


_This matters because the route planner is dependent on the idea that the travel costs are true to determine the best order to visit relics._

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** 
  - _A greedy strategy can fail because the locally cheapest relic choice may create a more expensive total route later._
- **Counter-example setup:** 
  - _Let's assume S connects to some relic node B with a cost of 1 and to C with a cost of 2._
  - But, the paths coming out of node B are more expensive, while paths from C to the remaining relic nodes and the exit are cheaper.
- **What greedy picks:** 
  - _Greedy would choose relic B first because it is the cheapest option that is reachable from the starting node._
- **What optimal picks:** 
  - _Instead of choosing the cheapest immediate relic, the optimal solution would select C first to minimize the total travel cost._
- **Why greedy loses:** 
  - _Greedy loses because it only considers the current cheapest cost and ignores how future path costs affect the overall fuel consumption._

### What the Algorithm Must Explore


- _The algorithm must explore different visitation orders because each order can lead to a different total fuel cost._

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component | Variable name in code | Data type | Description                                             |
|---|--------------------|-----|---------------------------------------------------------|
| Current location | current_loc        | node | The current node where the route search is taking place |
| Relics already collected | relics_visited_order | list | Contains the order in which the relics were collected   |
| Fuel cost so far | cost_so_far        | int | Contains the total fuel cost by that current route      |

### Part 5b: Data Structure for Visited Relics


| Property | Your answer                                                                                            |
|---|--------------------------------------------------------------------------------------------------------|
| Data structure chosen | Set                                                                                                    |
| Operation: check if relic already collected | Time complexity: O(1)                                                                                  |
| Operation: mark a relic as collected | Time complexity: O(1)                                                                                  |
| Operation: unmark a relic (backtrack) | Time complexity: O(1)                                                                                  |
| Why this structure fits | A set is useful because relics can be checked, added, and removed during the backtracking of recursion |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** _O(k!) with k being the number of relics._
- **Why:** _Worst case scenario, the algorithm would need to try each and every order of visiting the relic chambers._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** _The algorithm keeps track of the best known total fuel cost along with its corresponding route._
- **When it is used:** _It's used during the recursive exploration to help compare the different routes against the best known route._
- **What it allows the algorithm to skip:** _It allows it to skip exploring those partial routes whose current fuel cost cannot beat the best known route._

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** _At the current state, the algorithm knows its current node, the remaining relics, the collected relic order, and the current total fuel cost._
- **What the lower bound accounts for:** _The lower bound accounts for the fuel cost that has already been accumulated while traveling through the current route._
- **Why it never overestimates:** _Since the edge weights are nonnegative, any travel done after the current state can only increase the route cost._

### Part 6c: Pruning Correctness


- _Pruning is safe because if the current route cost is already greater than or equal to the best known route, then searching won't find a cheaper route_
- _Since the travel costs are nonnegative, other movements can only increase the total cost, therefore, pruning wouldn't remove any optimal solutions_

---

## References


- _Lecture Notes._
- _GeeksforGeeks.  – “Dijkstra's Algorithm | Greedy Algo-7” https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/. "Used to understand the overall structure of Dijkstra's algorithm, which included distance initialization, priority queue processing, and edge relaxation. Verified via tracing through provided test cases."_
