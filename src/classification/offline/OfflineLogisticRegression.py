"""
// Name        : LogisticRegression.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe concreta LogisticRegression che implementa i metodi:
                    - learn_many(x: pd.DataFrame, y: pd.Series);
                    - predict_many(x: pd.DataFrame);
                    - predict_one(x: pd.Series).
                 Eredita da OfflineClassifierInterface
"""
import numpy as np

from sklearn import linear_model
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from src.classification.offline.OfflineClassifierInterface import OfflineClassifierInterface


class OfflineLogisticRegression(OfflineClassifierInterface):
    """
        Richiama il costruttore di linear_model.LogisticRegression()
    """
    def __init__(self):
        """
            Utilizzo di Logistic Regression con sklearn e uso di parametri e scaler attraverso il meccanismo Pipeline.
        """
        #self.__model = Pipeline([('scaler', MinMaxScaler()), ('svc', linear_model.LogisticRegression())])
        self.__model = linear_model.LogisticRegression()

    """
        Metodo learn che prende in input:
        - x: un ndarray contenente le features;
        - y: un ndarray contenente le variabili target.
        Richiama il fit di LogisticRegression
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
