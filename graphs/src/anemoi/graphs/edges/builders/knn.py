"""Backward-compatible imports for checkpoints using the former KNN module path."""

from anemoi.graphs.edges.builders.euclidean.knn import BaseKNNEdges
from anemoi.graphs.edges.builders.euclidean.knn import KNNEdges
from anemoi.graphs.edges.builders.euclidean.knn import MutualKNNEdges
from anemoi.graphs.edges.builders.euclidean.knn import ReversedKNNEdges

__all__ = ["BaseKNNEdges", "KNNEdges", "MutualKNNEdges", "ReversedKNNEdges"]
