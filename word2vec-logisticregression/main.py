import inspect
import random
import re
from os import listdir
from os.path import isfile, join

import dill
import nltk
import numpy as np
import spacy
from gensim.models import Word2Vec
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

nlp = spacy.load("en_core_web_sm")

files = [join("../data/fr", f) for f in listdir("../data/fr")]
objects = []
for file in files:
    with open(file, "rb+") as f:
        objects.append(dill.load(f))
# print(objects[0][0])
# print(objects[0][0].keys())
tuples = []
for obj in objects:
    for poem in obj:
        # print(poem["Année de naissance"])
        if poem["Année de naissance"] == "Inconnue":
            continue
        siecle = int(poem["Année de naissance"]) // 100 + 1
        tuples.append((poem["Texte"], siecle))


def prendre_1290(liste):
    """
    Test function just cause otherwise we only have 19th century poems
    """
    result = []
    premier = 0
    deuxieme = 0
    for text, siecle in liste:
        if siecle == 18 and premier < 1290:
            premier += 1
            result.append((text, siecle))
        elif siecle == 19 and deuxieme < 1290:
            deuxieme += 1
            result.append((text, siecle))
    return result


tuples = prendre_1290(tuples)
print(len(tuples))

stats = dict()
for text, siecle in tuples:
    if siecle not in stats.keys():
        stats[siecle] = 1
    else:
        stats[siecle] += 1
print(stats)
# exit()


def preprocess(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if token.is_alpha and not token.is_stop]


tokenized_tuples = [(preprocess(poem), year) for poem, year in tuples]
w2v_model = Word2Vec(
    sentences=[text for text, year in tokenized_tuples],
    vector_size=100,
    window=5,
    min_count=2,
    workers=4,
)


def poem_to_vec(tokens, model):
    vectors = [model.wv[token] for token in tokens if token in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)


X = np.array([poem_to_vec(tokens, w2v_model) for tokens, _ in tokenized_tuples])
labels = [year for _, year in tokenized_tuples]

print(len(X))


X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.1, random_state=42
)

clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
