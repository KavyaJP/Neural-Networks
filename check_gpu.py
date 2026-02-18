import os

# Backend must be set BEFORE importing keras
os.environ["KERAS_BACKEND"] = "torch"

import keras
import torch

print(
    f"--- Environment: Keras {keras.__version__} | Backend: {keras.backend.backend()} ---"
)

# Verify hardware visibility
cuda_ready = torch.cuda.is_available()
print(f"CUDA Available: {cuda_ready}")

if cuda_ready:
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Device Count: {torch.cuda.device_count()}")

    print("\n--- Running MatMul Stress Test ---")
    try:
        # Forcing a large operation to ensure the 1650 Ti is actually engaged
        with keras.device("cuda"):
            x = keras.random.normal((5000, 5000))
            y = keras.random.normal((5000, 5000))
            z = keras.ops.matmul(x, y)

            print(f"Tensor Move Success: {z.device}")
            print("GPU Compute: OK")
    except Exception as e:
        print(f"Compute Failed: {e}")
else:
    print("\n[!] GPU not found. Check drivers or CUDA installation.")
