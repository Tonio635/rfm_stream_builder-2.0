"""
// Name        : Example.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe che modella gli esempi. È formata da una descrizione il quale è lista di Rfm
"""

from Rfm import Rfm
import datetime as dt


class Example:
    # Attributi privati:
    # __desc; descrizione dell'esempio - lista di oggetti di classe Rfm
    # labelTimeStamp: sarà di tipo datetime e verrà riempita con il momento dell'etichettatura
    __desc: list[Rfm]

    """
        Costruttore: setta il parametro labelTimeStamp e inizializza la lista desc come lista vuota.
    """
    def __init__(self, generationTimeStamp):
        self.__generationTimeStamp = generationTimeStamp
        self.__labelTimeStamp = None
        self.__desc = []

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
