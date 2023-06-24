"""
// Name        : OfflineClassifierEnum.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
// Description : Classe per l'enumerazione.
"""

from enum import Enum, unique


@unique
class OfflineClassifierEnum(Enum):
    OfflineLogisticRegression = 1
    OfflinePerceptron = 2
    OfflineRandomForest = 3
    OfflineDecisionTree = 4
    OfflineXGBoost = 5
