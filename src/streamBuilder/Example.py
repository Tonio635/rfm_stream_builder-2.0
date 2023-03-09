"""
// Name        : Example.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe che modella gli esempi. È formata da una descrizione il quale è lista di Rfm
"""

from Rfm import Rfm
import datetime as dt
import statistics as st
from typing import Union

class Example:
    # Attributi privati:
    # __desc; descrizione dell'esempio - lista di oggetti di classe Rfm
    # labelTimeStamp: sarà di tipo datetime e verrà riempita con il momento dell'etichettatura
    # __max: il valore massimo di ogni valore di recency, frequency e monetary
    # __min: il valore minimo di ogni valore di recency, frequency e monetary
    # __mean: il valore medio di ogni valore di recency, frequency e monetary
    # __standardDeviation: la deviazione standard di ogni valore di recency, frequency e monetary

    __desc: list[Rfm]
    __max: dict[str, Union[int, float]]
    __min: dict[str, Union[int, float]]
    __mean: dict[str, float]
    __standardDeviation: dict[str, float]


    """
        Costruttore: setta il parametro labelTimeStamp e inizializza la lista desc come lista vuota.
    """
    def __init__(self, generationTimeStamp):
        self.__generationTimeStamp = generationTimeStamp
        self.__labelTimeStamp = None
        self.__desc = []
        self.__max = {}
        self.__min = {}
        self.__mean = {}
        self.__standardDeviation = {}
    
    """
        Metodo getter StartTimeStamp.
        Return di un tipo datetime.
    """
    def getGenerationTimeStamp(self):
        return self.__generationTimeStamp

    """
        Metodo setter per generationTimeSTamp
    """
    def setGenerationTimeStamp(self, timestamp):
        self.__generationTimeStamp = timestamp
    
    """
        Metodo add che aggiunge un Rfm alla lista di RFM.
    """
    def addRfm(self, desc: Rfm):
        self.__desc.append(desc)

        recency = list(map(lambda obj: obj.getRecency(), self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency(), self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary(), self.__desc))
        
        '''
        recency = list(map(lambda obj: obj.getRecency() if obj.getRecency() != -1 else None, self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency() if obj.getRecency() != -1 else None, self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary() if obj.getRecency() != -1 else None, self.__desc))

        recency = list(filter(lambda obj: obj is not None, recency))
        frequency = list(filter(lambda obj: obj is not None, frequency))
        monetary = list(filter(lambda obj: obj is not None, monetary))

        rfmSize = len(recency)
        '''

        #if rfmSize >= 1:
        self.__max['recency'] = max(recency)
        self.__max['frequency'] = max(frequency)
        self.__max['monetary'] = max(monetary)

        self.__min['recency'] = min(recency)
        self.__min['frequency'] = min(frequency)
        self.__min['monetary'] = min(monetary)

        self.__mean['recency'] = st.mean(recency)
        self.__mean['frequency'] = st.mean(frequency)
        self.__mean['monetary'] = st.mean(monetary)

        #if rfmSize >= 2:
        if len(self.__desc) >= 2:
            self.__standardDeviation['recency'] = st.stdev(recency)
            self.__standardDeviation['frequency'] = st.stdev(frequency)
            self.__standardDeviation['monetary'] = st.stdev(monetary)


    """
        Metodo per eliminare l'Rfm in ultima posizione nella lista e inserirne uno passato in input.
    """
    def replaceLastRfm(self, desc: Rfm):
        self.__desc.pop(-1)
        self.__desc.append(desc)

    """
        Metodo getter per desc.
        Return di un tipo lista, la lista di Rfm.
    """
    def getDesc(self):
        return self.__desc

    """
        Metodo getter per labelTimeStamp.
        Return di un tipo datetime.
    """
    def getLabelTimestamp(self):
        return self.__labelTimeStamp

    """
        Metodo setter per labelTimeStamp.
    """
    def setLabelTimestamp(self, timestamp: dt.datetime):
        self.__labelTimeStamp = timestamp

    """
           Metodo che effettua la copia. 
    """
    def copy(self):
        ex = Example(None)
        ex.__desc = self.__desc.copy()
        ex.__generationTimeStamp = self.__generationTimeStamp
        ex.__labelTimeStamp = self.__labelTimeStamp
        return ex
