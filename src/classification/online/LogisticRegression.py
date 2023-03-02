"""
// Name        : LogisticRegression.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe concreta LogisticRegression che implementa i metodi:
                    - learn_many(x: pd.DataFrame, y: pd.Series);
                    - predict_many(x: pd.DataFrame);
                    - predict_one(x: pd.Series).
                 Eredita da OnlineClassifierInterface
"""

import pandas as pd

from river import linear_model, preprocessing, optim
from src.classification.online.OnlineClassifierInterface import OnlineClassifierInterface


class LogisticRegression(OnlineClassifierInterface):
    """
        Richiama il costruttore di linear_model.LogisticRegression()
    """
    def __init__(self):
        """
            Utilizzo di Logistic Regression con parametri e scaler.
        """
        #self.__model = preprocessing.StandardScaler() | linear_model.LogisticRegression(l2=0.0001, initializer=optim.initializers.Constant(3.14))
        #self.__model = preprocessing.StandardScaler() | linear_model.LogisticRegression()
        self.__model = linear_model.LogisticRegression()

    """
        Metodo learn che prende in input:
        - un pandas.Dataframe;
        - una pandas.Series.
        Richiama il learn_many di LogisticRegression.
    """
    def learn(self, x: pd.DataFrame, y: pd.Series):
        """
            Aggiorna lo scaler.
        """
        #self.__model.predict_many(x)
        self.__model = self.__model.learn_many(x, y)
        return self

    """
        Metodo predict_many che prende in input:
        - un Dataframe;
        Restituisce una pandas.Series.
        Richiama il predict_many di LogisticRegression.
    """
    def predict_many(self, x: pd.DataFrame) -> pd.Series:
        return self.__model.predict_many(x)

    """
        Metodo predict_one che prende in input:
        - una pandas.Series.
        Restituisce una valore booleano.
    """
    def predict_one(self, x: pd.Series) -> bool:
        return self.__model.predict_one(x)
