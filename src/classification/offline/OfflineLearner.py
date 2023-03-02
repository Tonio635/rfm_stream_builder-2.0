"""
// Name        : OfflineLearner.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe OfflineLearner .
"""

import importlib
import os
import pickle
import pandas as pd

from enum import Enum
from src.classification.PickleLoader import PickleLoader


class OfflineLearner:
    """
        Metodo costruttore:
            - classifierName: di tipo Enum, opzionale, prende l'enumeratore del classificatore che si vuole istanziare;
            - fromPickle: di tipo str, opzionale, per caricare un modello giò trainato.
    """
    def __init__(self, classifierName: Enum = None, fromPickle: str = None):
        # Se non nullo
        if fromPickle:
            # Prova ad aprire il fromPickle e a caricare il modello
            try:
                with open(fromPickle, "rb") as f:
                    self.__model = pickle.load(f)
            # Altrimenti eccezione: File non trovato!
            except FileNotFoundError as fnf:
                print(fnf)
        # Se fromPickle è nullo e classifierName non lo è
        elif classifierName:
            try:
                module = importlib.import_module(f'src.classification.offline.{classifierName.name}')
                class_ = getattr(module, str(classifierName.name))
                self.__model = class_()
            except TypeError:
                raise ValueError("Classificatore non disponibile")

    """
        Metodo che effettua il train del modello. 
        Prende in input un oggetto loader di classe PickleLoader e addestra il modello puntato da quel loader.
    """
    def train(self, loader: PickleLoader):
        full_df = pd.DataFrame()
        for df in loader:
            full_df = pd.concat([full_df, df])
        X = full_df.iloc[:, 0:-1]
        y = full_df.iloc[:, -1]
        self.__model = self.__model.learn(X.to_numpy(), y.to_numpy())

    """
        Metodo che effettua le predizioni.
        Prende in input un oggetto loader di classe PickleLoader e restituisce una pandas.Series di labels.
    """
    def predict(self, loader: PickleLoader):
        full_df = pd.DataFrame()
        for df in loader:
            full_df = pd.concat([full_df, df])
        X = full_df.iloc[:, 0:-1]
        return self.__model.predict(X.to_numpy())

    """
        Metodo per la validazione. Effettua il predict della relativa classe su cui vine chiamato.
        Prende in input un oggetto loader di classe Pickle Loader e restituisce un pandas.DataFrame costituito dalle
        label originarie (target) e le label predette (y_test). Il df metterà  a confronto le label predette con quelle
        originarie.
    """
    def test(self, loader: PickleLoader):
        full_df = pd.DataFrame()
        for df in loader:
            full_df = pd.concat([full_df, df])
        X = full_df.iloc[:, 0:-1]
        y_test = full_df.iloc[:, -1].to_numpy()
        predicted_labels = self.__model.predict(X.to_numpy())
        return [y_test, predicted_labels]

    """
        Metodo per serializzare il modello, preso in input un folderPath. 
        Formato: NomeAlgoritmo__YYYY-MM-DD__HH-MM
    """
    def toPickle(self, folderPath: str, filename: str = None):
        file_path = os.path.join(folderPath, filename)
        try:
            with open(file_path, "wb") as f:
                # "wb" argument opens the file in binary mode
                pickle.dump(self.__model, f)
        except FileNotFoundError:
            os.mkdir(folderPath)
            with open(file_path, 'wb') as f:
                # Inserisci file nel pickle
                pickle.dump(self.__model, f)
