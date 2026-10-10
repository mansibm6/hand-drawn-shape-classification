"""Reusable experiment functions extracted from Shape Classifier.ipynb."""

from __future__ import annotations


def build_model_cell_10():
    """Build the original architecture without training or accessing data."""
    import tensorflow as tf

    return tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 3)),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dense(3, activation="softmax"),
        ]
    )
