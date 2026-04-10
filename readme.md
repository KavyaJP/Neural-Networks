# Neural Network Playground

_Personal playground for prototyping neural networks on different type of data — comparing deep learning against XGBoost/LightGBM & Traditional Machine Learning Models on real classification & regression problems._

## Table of Contents

- [Neural Network Playground](#neural-network-playground)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Projects](#projects)
  - [Outputs](#outputs)
    - [Customer Churn Classification](#customer-churn-classification)
    - [Walmart Sales Prediction](#walmart-sales-prediction)
    - [California Housing Price Prediction](#california-housing-price-prediction)
    - [Car Price Prediction](#car-price-prediction)
    - [Heart Disease Classification](#heart-disease-classification)
    - [MNIST Classification](#mnist-classification)
    - [Dog and Cat Classification](#dog-and-cat-classification)
    - [DIFAR-10 Classification](#difar-10-classification)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
    - [Install Python](#install-python)
    - [Clone the repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Optional: Add GPU Support](#optional-add-gpu-support)
      - [Verify GPU Support](#verify-gpu-support)
  - [Core Focus Areas](#core-focus-areas)
  - [Roadmap](#roadmap)
  - [License](#license)

## Overview

A growing collection of neural network experiments focused on solving real-world regression and classification problems using modern deep learning frameworks.

This repository serves as my experimentation space — a place to prototype architectures, compare models, analyze performance, and continuously refine my understanding of neural networks on structured datasets.

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/KavyaJP/Neural-Networks)

## Projects

| Project            | Type                            | Project File                             | Dataset                                                        |
| ------------------ | ------------------------------- | ---------------------------------------- | -------------------------------------------------------------- |
| Loan Approval      | Binary Classification           | [File](tabular/loan_approval.ipynb)      | [data](data/loan_data.csv)                                     |
| Customer Churn     | Binary Classification           | [File](tabular/customer_churn.ipynb)     | [data](data/churn.csv)                                         |
| Walmart            | Regression                      | [File](tabular/walmart.ipynb)            | [data](data/Walmart.csv)                                       |
| California Housing | Regression                      | [File](tabular/california_housing.ipynb) | [data](data/housing.csv)                                       |
| Car Price          | Regression                      | [File](tabular/car_price.ipynb)          | [data](data/car_price_prediction.csv)                          |
| Heart Disease      | Binary Classification           | [File](tabular/heart_disease.ipynb)      | [data](https://zenodo.org/records/15364962)                    |
| MNIST              | Image Multiclass Classification | [File](cnn/mnist.ipynb)                  | Built-in (`keras.datasets.mnist`)                              |
| Cat and Dog        | Image Binary Classification     | [File](cnn/cat_and_dog.ipynb)            | [data](https://www.kaggle.com/datasets/tongpython/cat-and-dog) |
| CIFAR-10           | Image Multiclass Classification | [File](cnn/cifar.ipynb)                  | [data](https://www.kaggle.com/competitions/cifar-10/data)      |

**Quick Note**: _As the projects keeps going further and further, my own code gets better and better, so if you want to learn from it then I recommend checking out the latest Projects done by me, the list is already in oldest to latest order._

## Outputs

### Customer Churn Classification

![Customer Churn Training and Validation loss & Recall](screenshots/churn.png)

### Walmart Sales Prediction

![Walmart Training and Validation loss & RMSE](screenshots/walmart.png)

### California Housing Price Prediction

![California Housing Training and Validation loss & RMSE](screenshots/california_housing.png)

### Car Price Prediction

![Car Price Training and Validation loss & RMSE](screenshots/car_price.png)

### Heart Disease Classification

![Heart Disease Training and Validation loss & Recall](screenshots/heart_disease.png)

### MNIST Classification

![MNIST CNN Training and Validation loss & Accuracy](screenshots/mnist.png)

### Dog and Cat Classification

![Dog and Cat CNN Training and Validation loss & Accuray](screenshots/cat_and_dog.png)

### DIFAR-10 Classification

![CIFAR-10 CNN Training and Validation loss & Accuray](screenshots/cifar.png)

## Tech Stack

- Python 3.12
- Data Analysis
  - Pandas & NumPy
  - Matplotlib & Seaborn
- Machine Learning & Preprocessing
  - Scikit-learn
- Boosting
  - XGBoost
  - LightGBM
- Deep Learning
  - Keras (Torch backend)
  - PyTorch

## Installation

### Install Python

All projects were developed using **Python 3.12.0**.  
Download it from: [Here](https://www.python.org/downloads/release/python-3120/)

### Clone the repository

```bash
git clone https://github.com/KavyaJP/Neural-Networks.git
cd Neural-Networks
```

### Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

But you might want to make a venv if you are on Linux:

```bash
python3 -m venv venv
source venv/bin/activate
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

## Core Focus Areas

- Designing and training feedforward neural networks
- Comparing deep learning with traditional ML and boosting models
- Building structured preprocessing pipelines
- Evaluating model performance with proper metrics
- Experimenting with GPU-accelerated training

## Roadmap

- Multi-class classification problems
- Deeper and regularized architectures
- Hyperparameter tuning workflows
- Tabular deep learning vs boosting vs traditional ML benchmarks

## License

This repository is licensed under [MIT License](LICENSE), i.e. you are free to do anything with the available code.
