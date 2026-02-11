# Neural Network

This repository contains all the mini projects done by me in Neural Network

You can check the availability of your GPU using check_gpu.py

| Practical No. | Practical Name               | Practical File                             | Dataset                                  |
| ------------- | ---------------------------- | ------------------------------------------ | ---------------------------------------- |
| 0             | Car Price Prediction         | [Revision](revision.ipynb)                 | [data](dataset/car_price_prediction.csv) |
| 1             | Loan Approval Classification | [File](loan_approval_classification.ipynb) | [data](datasets/loan_data.csv)           |

## Installation

### Install Python

This project was developed using **Python 3.12.0**.  
Download it from:

👉 https://www.python.org/downloads/release/python-3120/

### Clone the repository

```bash
git clone https://github.com/KavyaJP/Neural-Networks.git
cd Neural-Networks
```

### Install Dependencies
then install the required library
```bash
pip install -r requirements.txt
```

### Optional: Add GPU Support
1. Go to [PyTorch - Get Started](https://pytorch.org/get-started/locally/)
2. Select
    - OS
    - Package: pip
    - Language: Python
    - Compute Platform:
      - CUDA (For NVidia GPU)
      - ROCm (For AMD GPU - only works on Linux, try using WSL for support on Windows)
3. Run the installation command provided on the website.

#### Verify GPU Support
After installing the CUDA-enabled version of PyTorch, run:
```bash
python check_gpu.py
``` 
If everything is configured correctly, it should detect your GPU.