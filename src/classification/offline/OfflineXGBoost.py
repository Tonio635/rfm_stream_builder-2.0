import numpy as np

from xgboost import XGBClassifier
from src.classification.offline.OfflineClassifierInterface import OfflineClassifierInterface

class OfflineXGBoost(OfflineClassifierInterface):
    """
        Richiama il costruttore di XGBClassifier
    """
    def __init__(self):
        self.__model = XGBClassifier(random_state = 42)
    
    """
        Metodo learn che prende in input:
        - x: un ndarray contenente le features;
        - y: un ndarray contenente le variabili target.
        richiama il fit di XGBoost
    """
    def learn(self, x: np.ndarray, y: np.ndarray):
        self.__model.set_params(scale_pos_weight=sum(y == 0) / sum(y == 1))
        self.__model = self.__model.fit(x, y)
        return self

    """
        Metodo predict che prende in input:
        - x: un ndarray contenente le features.
        Restituisce un ndarray
    """
    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.__model.predict(x)
