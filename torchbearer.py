"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Eufrecino R. Tactay III
Student ID:   828198534

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return (
        "It isn't enough because it only considers the smallest travel distance from the start to every node. Meaning, it doesn't help "
        "with choosing an optimal path for visiting every node before exiting.\n\n"
        
        "After realizing the costs, the path taken from start to finish still needs to be decided while also minimizing the total fuel "
        "consumption.\n\n"
        
        "This requires a search because different orders lead to different fuel costs, therefore, the algorithm must be able to search from "
        "different routes to get the minimum cost."
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    # Contains all the unique source points
    sources = []

    # Starting point is added
    sources.append(spawn)

    # Adds all relic nodes into the list, if it hasn't already
    for relic in relics:

        # Checks for duplicates and stops it from being added to the unique list
        if relic in sources:
            continue

        sources.append(relic)

    return sources


def run_dijkstra(graph, source):
    # Stores the known minimum distance to each node
    min_distances = {}

    # Initialize all nodes as unreachable
    for node in graph:
        min_distances[node] = float('inf')

    # Initialize starting node with distance of 0
    min_distances[source] = 0

    # Priority Queue for visiting nodes
    pq = []

    # Adds the starting node to the queue
    heapq.heappush(pq, (0, source))

    # Goes through all the nodes
    while len(pq) > 0:
        # Gets the node with the smallest distance
        current = heapq.heappop(pq)

        current_distance = current[0]
        current_node = current[1]

        # Skip the outdated entries
        if current_distance > min_distances[current_node]:
            continue

        # Goes through all the neighboring nodes
        for edge in graph[current_node]:

            neighbor = edge[0]
            cost = edge[1]

            # Adds up the new possible distance
            total_cost = current_distance + cost

            # If a shorter path is found, update
            if total_cost < min_distances[neighbor]:

                min_distances[neighbor] = total_cost

                # Add the newly updated distance onto the queue
                heapq.heappush(pq, (total_cost, neighbor))

    return min_distances


def precompute_distances(graph, spawn, relics, exit_node):
    # Gets all the important nodes
    source_nodes = select_sources(spawn, relics, exit_node)

    # Stores the shortest path for every source node
    distance_table = {}

    # Runs Dijkstra's algorithm on each of the source nodes
    for sr_node in source_nodes:
        shortest_paths = run_dijkstra(graph, sr_node)

        # Saves The distances for the current source node
        distance_table[sr_node] = shortest_paths

    return distance_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return (
        "Part 3a:\n"
        "- For all the finalized nodes, their shortest paths have already "
        "been determined and cannot be improved.\n\n"

        "- For nodes that are not finalized yet, the stored distance "
        "represents the shortest path currently found using only the "
        "finalized nodes in between.\n\n"

        "Part 3b:\n"
        "- At initialization, the source node starts with distance 0 and "
        "every other node starts at infinity because no shorter paths have "
        "been discovered.\n"
        "- This satisfies the invariant since no other paths to other nodes "
        "have been found yet.\n\n"

        "- Since all edge weights are nonnegative, the node with the "
        "smallest current distance is the shortest possible path.\n"
        "- Other future paths would have a greater total cost.\n\n"

        "- Once the algorithm finishes, all reachable nodes will contain "
        "their correct shortest-path distances in the distance table.\n\n"

        "Part 3c:\n"
        "- This matters because the route planner is dependent on the idea "
        "that the travel costs are true to determine the best order to visit "
        "relics."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
