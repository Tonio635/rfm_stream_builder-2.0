"""
// Name        : OfflineDecisionTree.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe concreta OfflineDecisionTree che implementa i metodi:
                    - learn(x: pd.DataFrame, y: pd.Series);
                    - predict(x: pd.DataFrame);
                 Eredita da OfflineClassifierInterface
"""
import numpy as np


from sklearn import tree
from src.classification.offline.OfflineClassifierInterface import OfflineClassifierInterface


class OfflineDecisionTree(OfflineClassifierInterface):
    """
        Richiama il costruttore di linear_model.DecisionTree()
    """
    def __init__(self):
        self.__model = tree.DecisionTreeClassifier()

    """
        Metodo learn che prende in input:
        - x: un ndarray contenente le features;
        - y: un ndarray contenente le variabili target.
        Richiama il fit di DecisionTree
    """
    def learn(self, x: np.ndarray, y: np.ndarray):
        self.__model = self.__model.fit(x, y)
        return self

    """
        Metodo predict che prende in input:
        - x: un ndarray contenente le features.
        Restituisce un ndarray
    """
    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.__model.predict(x)
