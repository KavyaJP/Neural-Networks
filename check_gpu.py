import os

# 1. Force Keras to use PyTorch before importing it
os.environ["KERAS_BACKEND"] = "torch"

import keras
import torch  # We import this just to verify the device count logic underneath

print("--- Keras Configuration ---")
print(f"Keras Backend: {keras.backend.backend()}")
print(f"Keras Version: {keras.__version__}")

# Check GPU availability through the backend engine
print(f"\n--- GPU Check (via {keras.backend.backend()}) ---")
print("CUDA available:", torch.cuda.is_available())
print("Device count:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("Device name:", torch.cuda.get_device_name(0))

print("\n--- Performance Test ---")
try:
    # 2. Use the Keras context manager to force operations onto the GPU
    # This is the Keras equivalent of device="cuda"
    with keras.device("cuda"):
        print("Allocating tensors on GPU...")
        # keras.random.normal is the agnostic equivalent of torch.randn
        x = keras.random.normal((5000, 5000))
        y = keras.random.normal((5000, 5000))

        print("Computing matmul...")
        # keras.ops.matmul is the agnostic equivalent of x @ y
        z = keras.ops.matmul(x, y)

        # Verify the tensor actually lives on the GPU
        # specific to torch backend, we can check .device
        print(f"Result device: {z.device}")

    print("Success")

except Exception as e:
    print(f"Error: {e}")
