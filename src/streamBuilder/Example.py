"""
// Name        : Example.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe che modella gli esempi. È formata da una descrizione il quale è lista di Rfm
"""

from Rfm import Rfm
from RfmR import RfmR
import datetime as dt
import statistics as st

class Example:
    # Attributi privati:
    # __desc; descrizione dell'esempio - lista di oggetti di classe Rfm
    # labelTimeStamp: sarà di tipo datetime e verrà riempita con il momento dell'etichettatura


    """
        Costruttore: setta il parametro labelTimeStamp e inizializza la lista desc come lista vuota.
    """
    def __init__(self, generationTimeStamp):
        self.__generationTimeStamp = generationTimeStamp
        self.__labelTimeStamp = None
        self.__desc = []
        self.__infoCategories = []
        self.__numDistinctCategories = 0
    
    """
        Metodo getter StartTimeStamp.
        Return di un tipo datetime.
    """
    def getGenerationTimeStamp(self):
        return self.__generationTimeStamp

    """
        Metodo setter per generationTimeStamp
    """
    def setGenerationTimeStamp(self, timestamp):
        self.__generationTimeStamp = timestamp
    
    """
        Metodo add che aggiunge un Rfm alla lista di RFM.
    """
    def addRfm(self, desc: Rfm):
        self.__desc.append(desc)

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
        ex.__infoCategories = self.__infoCategories.copy()
        ex.__numDistinctCategories = self.__numDistinctCategories
        return ex

    """
        Metodo per ottenere il massimo tra i valori degli RFM dei vari periodi.
        Return di un tipo Rfm.
    """
    def getMax(self):
        recency = list(map(lambda obj: obj.getRecency(), self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency(), self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary(), self.__desc))

        recency = list(map(lambda obj: obj.getRecency()
                       if obj.getRecency() != -1 else None, self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency()
                         if obj.getRecency() != -1 else None, self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary()
                        if obj.getRecency() != -1 else None, self.__desc))

        recency = list(filter(lambda obj: obj is not None, recency))
        frequency = list(filter(lambda obj: obj is not None, frequency))
        monetary = list(filter(lambda obj: obj is not None, monetary))

        maxR = max(recency)
        maxF = max(frequency)
        maxM = max(monetary)

        maximum = Rfm(maxR, maxF, maxM)

        return maximum
    
    """
        Metodo per ottenere il minimo tra i valori degli RFM dei vari periodi.
        Return di un tipo Rfm.
    """
    def getMin(self):
        recency = list(map(lambda obj: obj.getRecency(), self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency(), self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary(), self.__desc))

        recency = list(map(lambda obj: obj.getRecency()
                       if obj.getRecency() != -1 else None, self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency()
                         if obj.getRecency() != -1 else None, self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary()
                        if obj.getRecency() != -1 else None, self.__desc))

        recency = list(filter(lambda obj: obj is not None, recency))
        frequency = list(filter(lambda obj: obj is not None, frequency))
        monetary = list(filter(lambda obj: obj is not None, monetary))

        minR = min(recency)
        minF = min(frequency)
        minM = min(monetary)

        minimum = Rfm(minR, minF, minM)

        return minimum
    
    """
        Metodo per ottenere la media tra i valori degli RFM dei vari periodi.
        Return di un tipo RfmR.
    """
    def getMean(self):
        recency = list(map(lambda obj: obj.getRecency(), self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency(), self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary(), self.__desc))

        recency = list(map(lambda obj: obj.getRecency()
                       if obj.getRecency() != -1 else None, self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency()
                         if obj.getRecency() != -1 else None, self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary()
                        if obj.getRecency() != -1 else None, self.__desc))

        recency = list(filter(lambda obj: obj is not None, recency))
        frequency = list(filter(lambda obj: obj is not None, frequency))
        monetary = list(filter(lambda obj: obj is not None, monetary))

        meanR = st.mean(recency)
        meanF = st.mean(frequency)
        meanM = st.mean(monetary)

        mean = RfmR(meanR, meanF, meanM)

        return mean
    
    """
        Metodo per ottenere la deviazione standard tra i valori degli RFM dei vari periodi.
        Return di un tipo RfmR.
    """
    def getStandardDeviation(self):
        recency = list(map(lambda obj: obj.getRecency(), self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency(), self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary(), self.__desc))

        recency = list(map(lambda obj: obj.getRecency()
                       if obj.getRecency() != -1 else None, self.__desc))
        frequency = list(map(lambda obj: obj.getFrequency()
                         if obj.getRecency() != -1 else None, self.__desc))
        monetary = list(map(lambda obj: obj.getMonetary()
                        if obj.getRecency() != -1 else None, self.__desc))

        recency = list(filter(lambda obj: obj is not None, recency))
        frequency = list(filter(lambda obj: obj is not None, frequency))
        monetary = list(filter(lambda obj: obj is not None, monetary))

        rfmSize = len(recency)

        if rfmSize > 1:
            stdeviationR = st.stdev(recency)
            stdeviationF = st.stdev(frequency)
            stdeviationM = st.stdev(monetary)
        else:
            stdeviationR = 0.0
            stdeviationF = 0.0
            stdeviationM = 0.0

        standardDeviation = RfmR(stdeviationR, stdeviationF, stdeviationM)

        return standardDeviation

    """
        Metodo getter per infoCategories.
        Return di una lista di int.
    """
    def getInfoCategories(self):
        return self.__infoCategories
    
    """
        Metodo setter per infoCategories.
    """
    def setInfoCategories(self, infoCategories):
        self.__infoCategories = infoCategories
    
    """
        Metodo getter per numDistinctCategories.
        Return di un tipo int.
    """
    def getNumDistinctCategories(self):
        return self.__numDistinctCategories
    
    """
        Metodo setter per numDistinctCategories.
    """
    def setNumDistinctCategories(self, numDistinctCategories):
        self.__numDistinctCategories = numDistinctCategories