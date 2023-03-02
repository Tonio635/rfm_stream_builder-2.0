"""
// Name        : OfflineClassifierInterface.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Interfaccia OfflineClassifierInterface per permettere alle classi OfflinePerceptron,
                 OfflineLogisticRegression, OfflineRandomForest e OfflineDecisionTree di implementare i metodi
                 sottostanti.
"""

import numpy as np


class OfflineClassifierInterface:
    """
        Metodo learn che prende in input:
        - x: un ndarray contenente le features;
        - y: un ndarray contenente le variabili target.
    """
    def learn(self, x: np.ndarray, y: np.ndarray):
        pass

    """
        Metodo predict che prende in input:
        - x: un ndarray contenente le features.
        Restituisce un ndarray
    """
    def predict(self, x: np.ndarray) -> np.ndarray:
        pass
