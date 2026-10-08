"""Backward-compatible imports for checkpoints using the former target-feature module path."""

from anemoi.models.layers.target_features import CompositeTargetFeature
from anemoi.models.layers.target_features import CoordinatesFeature
from anemoi.models.layers.target_features import DecodingTargetFeature
from anemoi.models.layers.target_features import EncodedDataFeature
from anemoi.models.layers.target_features import InputForcingsFeature
from anemoi.models.layers.target_features import PrognosticsFeature
from anemoi.models.layers.target_features import TargetForcingsFeature
from anemoi.models.layers.target_features import TrainableParametersFeature
from anemoi.models.layers.target_features import create_decoding_target_features

__all__ = [
    "CompositeTargetFeature",
    "CoordinatesFeature",
    "DecodingTargetFeature",
    "EncodedDataFeature",
    "InputForcingsFeature",
    "PrognosticsFeature",
    "TargetForcingsFeature",
    "TrainableParametersFeature",
    "create_decoding_target_features",
]
