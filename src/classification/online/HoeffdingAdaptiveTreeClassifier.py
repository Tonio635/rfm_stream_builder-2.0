"""
// Name        : HoeffdingAdaptiveTreeClassifier.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe concreta HoeffdingAdaptiveTreeClassifier che implementa i metodi:
                    - learn_many(x: pd.DataFrame, y: pd.Series);
                    - predict_many(x: pd.DataFrame);
                    - predict_one(x: pd.Series).
                 Eredita da OnlineClassifierInterface.
"""

import pandas as pd

from river import tree, stream, drift
from src.classification.online.OnlineClassifierInterface import OnlineClassifierInterface


class HoeffdingAdaptiveTreeClassifier(OnlineClassifierInterface):
    """
        Richiama il costruttore di tree.HoeffdingAdaptiveTreeClassifier()
    """
    def __init__(self):
        """
            Utilizzo di AdaptiveRandomForest con parametri.
        """
        # self.__model = tree.HoeffdingAdaptiveTreeClassifier(drift_detector=drift.ADWIN(delta=50), drift_window_threshold=2000, grace_period= 1000)
        self.__model = tree.HoeffdingAdaptiveTreeClassifier(drift_detector=drift.ADWIN(delta=50))

    """
        Metodo learn che prende in input:
        - un pandas.Dataframe;
        - una pandas.Series.
        Richiama il learn_one di HoeffdingAdaptiveTreeClassifier.
    """
    def learn(self, x: pd.DataFrame, y: pd.Series):
        for xi, yi in stream.iter_pandas(x, y):
            self.__model.learn_one(xi, yi)
        return self

    """
        Metodo predict_many che prende in input:
        - un Dataframe;
        Restituisce una pandas.Series.
        Richiama il predict_one di HoeffdingAdaptiveTreeClassifier.
    """
    def predict_many(self, x: pd.DataFrame) -> pd.Series:
        labels = []
        for xi in stream.iter_pandas(x):
            label = self.__model.predict_one(xi[0])
            labels.append(label)
        return pd.Series(labels)

    """
        Metodo predict_one che prende in input:
        - una pandas.Series.
        Restituisce una valore booleano.
    """
    def predict_one(self, x: pd.Series) -> bool:
        return self.__model.predict_one(x.to_dict())
