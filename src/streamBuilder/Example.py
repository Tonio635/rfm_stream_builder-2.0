"""
// Name        : Example.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
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
        self.__products = []
    
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
        for product in self.__products:
            ex.__products.append(product.copy())
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
        Metodo add che aggiunge un Rfm per ogni categoria alla lista di RFM.
    """
    def addProductRfm(self, desc: list[Rfm]):
        if len(self.__products) == 0:
            self.__products = [[] for _ in desc]

        for i in range(len(desc)):
            self.__products[i].append(desc[i])
    
    """
        Metodo getter per products.
        Return di un tipo lista di liste, la lista di Rfm delle categorie.
    """
    def getProductRfm(self):
        return self.__products

    """
        Metodo per eliminare il product Rfm in ultima posizione nella lista e inserirne uno passato in input.
    """
    def replaceLastProductRfm(self, products: list[Rfm]):
        for i in range(len(products)):
            self.__products[i].pop(-1)
            self.__products[i].append(products[i])

    """
        Metodo per ottenere il massimo tra i valori degli RFM delle categorie dei vari periodi.
        Return di una lista di Rfm.
    """
    def getProductsMax(self):
        maximum = []
        for product in self.__products:
            recency = list(map(lambda obj: obj.getRecency(), product))
            frequency = list(map(lambda obj: obj.getFrequency(), product))
            monetary = list(map(lambda obj: obj.getMonetary(), product))

            recency = list(map(lambda obj: obj.getRecency()
                            if obj.getRecency() != -1 else None, product))
            frequency = list(map(lambda obj: obj.getFrequency()
                            if obj.getRecency() != -1 else None, product))
            monetary = list(map(lambda obj: obj.getMonetary()
                            if obj.getRecency() != -1 else None, product))

            recency = list(filter(lambda obj: obj is not None, recency))
            frequency = list(filter(lambda obj: obj is not None, frequency))
            monetary = list(filter(lambda obj: obj is not None, monetary))

            maxR = max(recency) if len(recency) > 0 else 0
            maxF = max(frequency) if len(frequency) > 0 else 0
            maxM = max(monetary) if len(monetary) > 0 else 0

            maximum.append(Rfm(maxR, maxF, maxM))

        return maximum
    
    """
        Metodo per ottenere il minimo tra i valori degli RFM delle categorie dei vari periodi.
        Return di una lista di Rfm.
    """
    def getProductsMin(self):
        minimum = []
        for product in self.__products:
            recency = list(map(lambda obj: obj.getRecency(), product))
            frequency = list(map(lambda obj: obj.getFrequency(), product))
            monetary = list(map(lambda obj: obj.getMonetary(), product))

            recency = list(map(lambda obj: obj.getRecency()
                               if obj.getRecency() != -1 else None, product))
            frequency = list(map(lambda obj: obj.getFrequency()
                                 if obj.getRecency() != -1 else None, product))
            monetary = list(map(lambda obj: obj.getMonetary()
                            if obj.getRecency() != -1 else None, product))

            recency = list(filter(lambda obj: obj is not None, recency))
            frequency = list(filter(lambda obj: obj is not None, frequency))
            monetary = list(filter(lambda obj: obj is not None, monetary))

            minR = min(recency) if len(recency) > 0 else 0
            minF = min(frequency) if len(frequency) > 0 else 0
            minM = min(monetary) if len(monetary) > 0 else 0

            minimum.append(Rfm(minR, minF, minM))

        return minimum

    """
        Metodo per ottenere la media tra i valori degli RFM delle categorie dei vari periodi.
        Return di una lista di RfmR.
    """
    def getProductsMean(self):
        means = []
        for product in self.__products:
            recency = list(map(lambda obj: obj.getRecency(), product))
            frequency = list(map(lambda obj: obj.getFrequency(), product))
            monetary = list(map(lambda obj: obj.getMonetary(), product))

            recency = list(map(lambda obj: obj.getRecency()
                               if obj.getRecency() != -1 else None, product))
            frequency = list(map(lambda obj: obj.getFrequency()
                                 if obj.getRecency() != -1 else None, product))
            monetary = list(map(lambda obj: obj.getMonetary()
                            if obj.getRecency() != -1 else None, product))

            recency = list(filter(lambda obj: obj is not None, recency))
            frequency = list(filter(lambda obj: obj is not None, frequency))
            monetary = list(filter(lambda obj: obj is not None, monetary))

            meanR = st.mean(recency) if len(recency) > 0 else 0
            meanF = st.mean(frequency) if len(frequency) > 0 else 0
            meanM = st.mean(monetary) if len(monetary) > 0 else 0

            means.append(Rfm(meanR, meanF, meanM))

        return means

    """
        Metodo per ottenere la deviazione standard tra i valori degli RFM delle categorie dei vari periodi.
        Return di una lista di RfmR.
    """
    def getProductsStandardDeviation(self):
        standardDeviations = []
        for product in self.__products:
            recency = list(map(lambda obj: obj.getRecency(), product))
            frequency = list(map(lambda obj: obj.getFrequency(), product))
            monetary = list(map(lambda obj: obj.getMonetary(), product))

            recency = list(map(lambda obj: obj.getRecency()
                        if obj.getRecency() != -1 else None, product))
            frequency = list(map(lambda obj: obj.getFrequency()
                            if obj.getRecency() != -1 else None, product))
            monetary = list(map(lambda obj: obj.getMonetary()
                            if obj.getRecency() != -1 else None, product))

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

            standardDeviations.append(RfmR(stdeviationR, stdeviationF, stdeviationM))

        return standardDeviations
