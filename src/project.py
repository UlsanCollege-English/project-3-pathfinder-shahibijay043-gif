"""Project 3: Pathfinder.

Implement graph utilities for an undirected weighted map.
"""

from __future__ import annotations

from collections import deque
import heapq
import json
import math
from pathlib import Path


Graph = dict[str, dict[str, int]]


def load_graph(path: str) -> Graph:
    """Load a weighted graph from a JSON file."""

    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        graph = json.load(file)

    if not isinstance(graph, dict):
        raise ValueError("Top level JSON must be a dictionary.")

    for node, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            raise ValueError(
                f"Neighbors for {node} must be a dictionary."
            )

        for neighbor, weight in neighbors.items():
            if not isinstance(weight, int):
                raise ValueError(
                    "Weights must be positive integers."
                )

            if weight <= 0:
                raise ValueError(
                    "Weights must be positive integers."
                )

    return graph


def get_neighbors(graph: Graph, node: str) -> dict[str, int]:
    """Return the neighbors and weights for node."""

    return graph.get(node, {})


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first traversal order."""

    if start not in graph:
        return []

    visited = set()
    order = []

    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dijkstra_distances(
    graph: Graph,
    start: str,
) -> dict[str, float]:
    """Return shortest distances from start."""

    if start not in graph:
        return {}

    distances = {start: 0}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = (
            heapq.heappop(priority_queue)
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            if weight <= 0:
                raise ValueError(
                    "Weights must be positive."
                )

            new_distance = (
                current_distance + weight
            )

            if (
                neighbor not in distances
                or new_distance < distances[neighbor]
            ):
                distances[neighbor] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor),
                )

    return distances


def shortest_path(
    graph: Graph,
    start: str,
    target: str,
) -> list[str]:
    """Return the shortest path from start to target."""

    if start not in graph:
        return []

    if target not in graph:
        return []

    if start == target:
        return [start]

    distances = {start: 0}

    previous: dict[str, str | None] = {
        start: None
    }

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = (
            heapq.heappop(priority_queue)
        )

        if current_node == target:
            break

        if (
            current_distance
            > distances[current_node]
        ):
            continue

        for neighbor, weight in graph[current_node].items():

            if weight <= 0:
                raise ValueError(
                    "Weights must be positive."
                )

            new_distance = (
                current_distance + weight
            )

            if (
                neighbor not in distances
                or new_distance < distances[neighbor]
            ):
                distances[neighbor] = new_distance

                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor),
                )

    if target not in distances:
        return []

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path


def demo() -> None:
    """Print a short demonstration."""

    graph = load_graph("data/map.json")

    print("=== Pathfinder Demo ===")

    print(
        f"Number of locations: {len(graph)}"
    )

    bfs_result = bfs_order(
        graph,
        "Gate",
    )

    print(
        f"BFS Order from Gate: {bfs_result}"
    )

    distances = dijkstra_distances(
        graph,
        "Gate",
    )

    print(
        f"Shortest distances from Gate:"
    )

    for node, distance in distances.items():
        print(f"{node}: {distance}")

    path = shortest_path(
        graph,
        "Gate",
        "Rest Area",
    )

    print(
        f"Shortest path from Gate to Rest Area:"
    )

    print(path)


if __name__ == "__main__":
    demo()