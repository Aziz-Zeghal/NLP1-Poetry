# Poetry Analysis and Generation Project

This project explores various Natural Language Processing (NLP) techniques for poetry analysis and generation using the Poetree dataset, a multilingual poetry library.

# Table of Contents
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Exploratory methods](#exploratory-methods)
- [Classification Models](#classification-models)
  - [Traditional ML Models](#traditional-ml-models)
  - [Neural Network Models](#neural-network-models)
- [Generation Models](#generation-models)
- [Results](#results)

## Project Structure

```bash
.
├── EDA.ipynb # Exploratory Data Analysis
├── README.md # Project overview
├── classification/ # Classification models
├── generation/ # Poetry generation models and results
├── data_manipulation # Data merge method
├── classification_bench.ipynb # Comprehensive classification scores
├── class_bench.parquet # Benchmark results
├── report.pdf # Project report
└── data/ # Poetree dataset
  ├── en/
  ├── de/
  └── ... 

```

## Dataset
The Poetree library contains poems in multiple languages. We selected the German poems for classification, and english poems for generation.

For more information about the dataset, please refer to the `EDA.ipynb` and `report.pdf` files.

## Exploratory methods
Three exploratory methods were implemented:
- **Data Augmentation (classification)**: Line permutation for enhanced training
- **Data merge (generation)**: Translating German poems to English
- **Model combination**: Combining different models using bagging and stacking techniques

## Classification Models
We implemented and compared different classification approaches, all using TF-IDF or Word2Vec as vector representations:

### Traditional ML Models
- Logistic Regression (w/ TF-IDF/Word2Vec)
- Naive Bayes (w/ TF-IDF)
- Random Forest (w/ TF-IDF/Word2Vec)

### Neural Network Models
- Feedforward Neural Network (w/ TF-IDF/Word2Vec)
- Recurrent Neural Network (w/ TF-IDF/Word2Vec)
- RNN with Attention (w/ TF-IDF/Word2Vec)

## Generation Models
We explored different approaches for poetry generation:
- N-gram models
- Transformer-based models
- Multi-layer Perceptron

## Results
Detailed classification scores and benchmarks can be found in individual model results in their respective directories/

For **classification results**, there is a comprehensive comparison in `classification_bench.ipynb`.

For **generation results**, we provide a summary of the models and their performance in the `generation/` directory.