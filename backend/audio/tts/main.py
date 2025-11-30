import sys
import torch
import numpy as np


def main():
    print("--- TTS Environment Check ---")
    print(f"Python: {sys.version}")
    print(f"Torch Version: {torch.__version__}")
    print(f"Numpy Version: {np.__version__}")

    # Simple verification that dependencies are loaded
    x = torch.rand(3, 3)
    print(f"\nRandom Tensor:\n{x}")


if __name__ == "__main__":
    main()