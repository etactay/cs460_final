# The Torchbearer

**Student Name:** Eufrecino R. Tactay III
**Student ID:** 828198534
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _It isn't enough because it only considers the smallest travel distance from the start to every node. Meaning, it doesn't help with choosing an optimal path for visiting every node before exiting._

- **What decision remains after all inter-location costs are known:**
  _After realizing the costs, the path taken from start to finish still needs to be decided while also minimizing the total fuel consumption._

- **Why this requires a search over orders (one sentence):**
  _This requires a search because different orders lead to different fuel costs, therefore, the algorithm must be able to search from different routes to get the minimum cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source                                                                                                      |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| _Spawn node_     | _We start at the spawn, making it vital to find the shortest paths_                                                     |
| _Relics nodes_   | _To help us compare the different routes, we'll need to be able to find the distances from the relic nodes to the exit_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer                                      |
|---|--------------------------------------------------|
| Data structure name | Nested Dictionary                                |
| What the keys represent | Source nodes and destination nodes               |
| What the values represent | Contains the minimum fuel cost between the nodes |
| Lookup time complexity | O(1)                                             |
| Why O(1) lookup is possible | It uses a hash table lookup via key              |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _'k' runs, where k is dependent on the number of source nodes_
- **Cost per run:** _O(E log V)_
- **Total complexity:** _O(k(E log V))_
- **Justification (one line):** _We run Dijkstra's algorithm for each and every selected source node._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _For all the finalized nodes, their shortest paths have already been determined and cannot be improved._

- **For nodes not yet finalized (not in S):**
  _For nodes that are not finalized yet, the stored distance represents the shortest path currently found using only the finalized nodes in between._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  - _At initialization, the source node starts with distance 0 and every other node starts at infinity because no shorter paths have been discovered._
  - _This satisfies the invariant since no other paths to other nodes have been found yet._

- **Maintenance : why finalizing the min-dist node is always correct:**
  - _Since all edge weights are nonnegative, the node with the smallest current distance IS the shortest possible path._
  - _Other future paths would have a greater total cost_

- **Termination : what the invariant guarantees when the algorithm ends:**
  - _Once the algorithm finishes, all reachable nodes will contain their correct shortest-path distances in the distance table._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_This matters because the route planner is dependent on the idea that the travel costs are true to determine the best order to visit relics._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Lecture Notes._
- _GeeksforGeeks.  – “Dijkstra's Algorithm | Greedy Algo-7” https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/. "Used to understand the overall structure of Dijkstra's algorithm, which included distance initialization, priority queue processing, and edge relaxation. Verified via tracing through provided test cases."_
