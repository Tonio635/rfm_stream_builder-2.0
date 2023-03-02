"""
// Name        : ClassifierEnum.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe per l'enumerazione.
"""

from enum import Enum, unique


@unique
class ClassifierEnum(Enum):
    AdaptiveRandomForestClassifier = 1
    HoeffdingAdaptiveTreeClassifier = 2
    HoeffdingTreeClassifier = 3
    Perceptron = 4
    LogisticRegression = 5
