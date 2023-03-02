"""
// Name        : Perceptron.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe concreta Perceptron che implementa i metodi:
                    - learn_many(x: pd.DataFrame, y: pd.Series);
                    - predict_many(x: pd.DataFrame);
                    - predict_one(x: pd.Series).
                 Eredita da OnlineClassifierInterface.
"""

import pandas as pd

from river import linear_model, optim, preprocessing
from src.classification.online.OnlineClassifierInterface import OnlineClassifierInterface


class Perceptron(OnlineClassifierInterface):
    """
        Richiama il costruttore di linear_model.Perceptron()
    """
    def __init__(self):
        """
            Utilizzo di Perceptron con parametri e scaler.
        """
        #self.__model = linear_model.Perceptron(l2=0.0001, initializer=optim.initializers.Constant(3.14))
        #self.__model = preprocessing.StandardScaler() | linear_model.Perceptron()
        self.__model = linear_model.Perceptron()
    """
        Metodo learn che prende in input:
        - un pandas.Dataframe;
        - una pandas.Series.
        Richiama il learn_many di Perceptron.
    """
    def learn(self, x: pd.DataFrame, y: pd.Series):
        """
            Aggiorna lo scaler
        """
        #self.__model.predict_many(x)
        self.__model = self.__model.learn_many(x, y)
        return self

    """
        Metodo predict_many che prende in input:
        - un Dataframe;
        Restituisce una pandas.Series.
        Richiama il predict_many di Perceptron.
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
