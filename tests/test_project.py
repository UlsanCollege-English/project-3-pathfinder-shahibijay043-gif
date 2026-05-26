"""Public + extended tests for Project 3: Pathfinder."""

from __future__ import annotations

import json
import pytest

from src.project import (
    bfs_order,
    dijkstra_distances,
    get_neighbors,
    load_graph,
    shortest_path,
)


# =========================================================
# Sample Festival Map (matches your project theme)
# =========================================================

def sample_graph() -> dict[str, dict[str, int]]:
    return {
        "Gate": {
            "Food Court": 4,
            "Main Stage": 7,
        },
        "Food Court": {
            "Gate": 4,
            "Rest Area": 3,
        },
        "Main Stage": {
            "Gate": 7,
            "First Aid": 2,
            "Game Zone": 4,
        },
        "First Aid": {
            "Main Stage": 2,
            "Rest Area": 5,
        },
        "Rest Area": {
            "Food Court": 3,
            "First Aid": 5,
            "Game Zone": 2,
        },
        "Game Zone": {
            "Main Stage": 4,
            "Rest Area": 2,
        },
    }


# =========================================================
# load_graph tests
# =========================================================

def test_load_graph_reads_file(tmp_path):
    graph_data = sample_graph()

    path = tmp_path / "map.json"
    path.write_text(json.dumps(graph_data), encoding="utf-8")

    assert load_graph(str(path)) == graph_data


def test_load_graph_rejects_invalid_weight(tmp_path):
    bad_graph = {
        "A": {"B": 0},
        "B": {"A": 0},
    }

    path = tmp_path / "bad.json"
    path.write_text(json.dumps(bad_graph), encoding="utf-8")

    with pytest.raises(ValueError):
        load_graph(str(path))


def test_load_graph_rejects_negative_weight(tmp_path):
    bad_graph = {
        "A": {"B": -5},
        "B": {"A": -5},
    }

    path = tmp_path / "bad.json"
    path.write_text(json.dumps(bad_graph), encoding="utf-8")

    with pytest.raises(ValueError):
        load_graph(str(path))


# =========================================================
# get_neighbors tests
# =========================================================

def test_get_neighbors_existing():
    graph = sample_graph()

    assert get_neighbors(graph, "Gate") == {
        "Food Court": 4,
        "Main Stage": 7,
    }


def test_get_neighbors_missing():
    graph = sample_graph()

    assert get_neighbors(graph, "Unknown") == {}


# =========================================================
# BFS tests
# =========================================================

def test_bfs_from_gate_visits_nodes():
    graph = sample_graph()

    result = bfs_order(graph, "Gate")

    assert result[0] == "Gate"
    assert "Food Court" in result
    assert "Main Stage" in result
    assert len(result) == len(set(result))


def test_bfs_missing_start():
    graph = sample_graph()

    assert bfs_order(graph, "X") == []


# =========================================================
# Dijkstra tests
# =========================================================

def test_dijkstra_distances():
    graph = sample_graph()

    distances = dijkstra_distances(graph, "Gate")

    assert distances["Gate"] == 0
    assert distances["Food Court"] == 4
    assert distances["First Aid"] == 9


def test_dijkstra_missing_start():
    graph = sample_graph()

    assert dijkstra_distances(graph, "Unknown") == {}


def test_dijkstra_unreachable_node_not_in_result():
    graph = {
        "A": {"B": 2},
        "B": {"A": 2},
        "C": {"D": 1},
        "D": {"C": 1},
    }

    result = dijkstra_distances(graph, "A")

    assert "C" not in result
    assert "D" not in result


def test_dijkstra_invalid_weight_raises():
    graph = {
        "A": {"B": 1},
        "B": {"A": 1, "C": 0},
        "C": {"B": 0},
    }

    with pytest.raises(ValueError):
        dijkstra_distances(graph, "A")


# =========================================================
# shortest_path tests
# =========================================================

def test_shortest_path_main_route():
    graph = sample_graph()

    path = shortest_path(graph, "Gate", "First Aid")

    assert path[0] == "Gate"
    assert path[-1] == "First Aid"
    assert "Main Stage" in path


def test_shortest_path_same_node():
    graph = sample_graph()

    assert shortest_path(graph, "Gate", "Gate") == ["Gate"]


def test_shortest_path_missing_nodes():
    graph = sample_graph()

    assert shortest_path(graph, "X", "Gate") == []
    assert shortest_path(graph, "Gate", "X") == []


def test_shortest_path_unreachable():
    graph = {
        "A": {"B": 1},
        "B": {"A": 1},
        "C": {"D": 1},
        "D": {"C": 1},
    }

    assert shortest_path(graph, "A", "D") == []