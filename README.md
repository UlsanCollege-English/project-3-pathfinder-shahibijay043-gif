[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RNukvtFO)
Project 3: Pathfinder
Map Theme

My map theme is a fantasy adventure village. The graph represents different locations inside a fantasy world where travelers move between important places such as gates, markets, rest areas, and castles. The project focuses on finding the shortest and most efficient travel routes between locations using graph algorithms.

Map Picture
![Project map](assets/map.png)

How the Graph Works
Nodes

Each node represents a location in the fantasy village map.

Examples:

Gate
Food Court
Rest Area
Magic Shop
Castle
Edges

Each edge represents a path connecting two locations.

Weights

Each weight represents the travel cost or distance between locations.

Features Implemented
 Load graph from JSON
 Get neighbors
 BFS traversal
 Dijkstra shortest distances
 Shortest path reconstruction
 Demo function
 Extra tests
 Stretch feature: Graph validation
How to Run

Run the project using:

python src/project.py
How to Test

Run all tests using:

pytest -q

or on Windows:

py -m pytest -q
Complexity
BFS

Time:

O(V + E)

Space:

O(V)

Explanation:

Breadth-First Search visits every node and edge at most once. Extra memory is used for the queue and visited set.

Dijkstra

Time:

O((V + E) log V)

Space:

O(V)

Explanation:

Dijkstra’s algorithm processes nodes using a heap priority queue. Heap operations require log V time, and the algorithm may process all vertices and edges.

Shortest Path Reconstruction

Time:

O(P)

Space:

O(P)

Explanation:

Path reconstruction traces backward from the target node to the starting node using the previous dictionary. P represents the number of nodes in the final path.

Edge Cases
 Empty graph
 Missing start node
 Missing target node
 Start equals target
 Unreachable target
 Graph with a cycle
 Graph with one node
 Disconnected graph
 Multiple possible paths
 Zero weight rejected
 Negative weight rejected

Add notes about edge cases here:

The project validates all edge weights before running Dijkstra’s algorithm. Invalid graphs with zero or negative weights raise ValueError. Missing nodes and unreachable targets safely return empty results instead of crashing the program.

Known Limitations
This project only supports undirected weighted graphs.
Negative edge weights are not supported.
Tie paths may return one valid shortest path instead of all shortest paths.
The project does not include a graphical user interface (GUI).
Assistance & Sources
AI Used?

Yes

What AI Helped With

AI helped me:

understand Dijkstra’s algorithm more clearly,
debug test failures,
improve edge-case handling,
organize the README,
improve code readability and structure.
Other Sources
Python documentation for heapq
Class lecture notes
Zybooks examples