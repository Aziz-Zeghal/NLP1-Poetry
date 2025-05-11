# Poetry Analysis and Generation Project

This project explores various Natural Language Processing (NLP) techniques for poetry analysis and generation using the Poetree dataset, a multilingual poetry library.

## Project Structure

```
.
├── data/
│ ├── augmented/ # Data with line permutation
│ └── merged/ # Translated poems (German to English)
├── classification/ # Classification models and results
├── generation/ # Poetry generation models
└── classification_benchmark.md # Comprehensive classification scores
```

## Data Processing

- **Base Dataset**: Poetree library containing poems in multiple languages
- **Data Augmentation**:
  - Line permutation for enhanced training
  - Translation augmentation (German to English)

## Classification Models

We implemented and compared different classification approaches, all using TF-IDF or Word2Vec as vector representations:

### Traditional ML Models
- Logistic Regression (with TF-IDF/Word2Vec)
- Naive Bayes (with TF-IDF)
- Random Forest (with TF-IDF/Word2Vec)

### Neural Network Models
- Feedforward Neural Network (with TF-IDF/Word2Vec)
- Recurrent Neural Network (RNN with TF-IDF/Word2Vec)
- RNN with Attention (using TF-IDF/Word2Vec)

## Generation Models

We explored different approaches for poetry generation:
- N-gram models
- Transformer-based models
- Multi-layer Perceptron

## Results

Detailed classification scores and benchmarks can be found in:
- Individual model results in their respective directories
- Comprehensive comparison in `classification_benchmark.md`

Detailed generation results and examples can be found in the notebooks located in the `generation/` directory.