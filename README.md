# Aetheris • AI-Powered Tool for Bird Migration Monitoring System 🕊

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![TensorFlow 2.18](https://img.shields.io/badge/TensorFlow-2.18-orange)](https://www.tensorflow.org/)

**Automated species identification for camera trap networks**  
*A deep learning solution to transform wilderness monitoring through real-time bird classification and migration pattern analysis* 
***
![изображение](https://github.com/user-attachments/assets/b99a7577-b503-486a-b332-12ccc0655101)
***
## 🌍 Why It Matters  
Climate change has disrupted 57% of known bird migration routes ([National Audubon Society](https://www.audubon.org/)). This system empowers environmental agencies to:  
- **Detect early warning signs** of ecosystem imbalance through species presence/absence  
- **Track unplanned route deviations** caused by extreme weather events  
- **Quantify conservation impact** by monitoring endangered species recovery  
- **Automate 200+ species identification** from camera traps with **75.7% field accuracy** 

## 🌟 Key Features
- **200 Bird Species Classification** trained on the CUB-200-2011 dataset
- **Advanced Data Augmentation** to address class imbalance
- Three model architectures:
  - Baseline CNN
  - CNN with Dropout Regularization
  - **EfficientNetB0** Transfer Learning (75.7% test accuracy)
- Comprehensive visualizations:
  - Class distribution analysis
  - Training/validation metrics
  - Confusion matrices

## 📦 Installation
1. Clone repository:
```bash
git clone https://github.com/berberberk/bird-species-classification-py.git
cd bird-species-classification-py
```
1. Install dependencies with Poetry:
```bash
poetry install
```

## 📂 Project Structure
```bash
bird-species-classification/
├── models/                                   # Trained models
│   ├── baseline_model.keras
│   ├── dropout_model.keras
│   └── enet_model.keras
├── notebooks/                                # Jupyter notebooks
│   ├── bird-species-classification.ipynb
│   └── bird-species-classification-v25.ipynb
├── src/                                      # Source code
│   ├── data/                                 # Dataset loading/augmentation
│   ├── models/                               # Model architectures
│   ├── plots/                                # Visualization utilities
│   └── web/                                  # Web interface
├── pyproject.toml                            # Poetry dependencies
├── poetry.lock                               # Poetry lock
└── reproducibility.py                        # Seed configuration
```
