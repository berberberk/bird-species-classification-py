import os
import random
import numpy as np
import tensorflow as tf
from tensorflow import keras


def set_seed(seed: int = 42) -> int:

    # Set environment variables
    os.environ["PYTHONHASHSEED"] = str(seed)
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    os.environ["TF_DETERMINISTIC_OPS"] = "1"  # Enforce deterministic GPU ops (TF 2.8+)
    os.environ["TF_CUDNN_DETERMINISTIC"] = "1"  # Deterministic cuDNN algorithms
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

    # Seed everything else
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    tf.config.experimental.enable_op_determinism()
    keras.utils.set_random_seed(seed)
    return seed