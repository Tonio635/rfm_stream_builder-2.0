"""
// Name        : OfflineRandomForest.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
// Description : Classe concreta OfflineRandomForest che implementa i metodi:
                    - learn_many(x: pd.DataFrame, y: pd.Series);
                    - predict_many(x: pd.DataFrame);
                 Eredita da OfflineClassifierInterface
"""

import numpy as np

from sklearn import ensemble
from src.classification.offline.OfflineClassifierInterface import OfflineClassifierInterface


class OfflineRandomForest(OfflineClassifierInterface):
    """
        Richiama il costruttore di linear_model.RandomForestClassifier()
    """
    def __init__(self):
        self.__model = ensemble.RandomForestClassifier(random_state=42)

    """
        Metodo learn che prende in input:
        - x: un ndarray contenente le features;
        - y: un ndarray contenente le variabili target.
        richiama il fit di RandomForest
    """
    def learn(self, x: np.ndarray, y: np.ndarray):
        self.__model.set_params(class_weight={0: len(y)/(2 * sum(y == 0)), 1: len(y)/(2 * sum(y == 1))})
        self.__model = self.__model.fit(x, y)
        return self

    """
        Metodo predict che prende in input:
        - x: un ndarray contenente le features.
        Restituisce un ndarray
    """
    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.__model.predict(x)
