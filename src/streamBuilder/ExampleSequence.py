"""
// Name        : ExampleSequence.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
// Description : Classe che modella la sequenza di esempi. È formata da un unico attributo: la lista di Examples.
"""

from Example import Example
import datetime as dt


class ExampleSequence:
    __examples: list[Example]

    """ 
        Metodo costruttore. Inizializza la lista di esempi come lista vuota.
        examples è una collezione di esempi che verranno mantenuti nell'Example Sequence.
    """
    def __init__(self):
        self.__examples = []

    """
        Metodo append per inserire nuovi esempi alla lista di esempi.
    """
    def appendExample(self, ex: Example):
        self.__examples.append(ex)

    """
        Metodo setter per il labelTimeStamp degli examples in ExampleSequence
    """
    def setLabelTimestamp(self, timestamp: dt.datetime):
        for example in self.__examples:
            example.setLabelTimestamp(timestamp)

    """
        Metodo record per etichettare e mettere nello stream gli esempi.
        Riceve in input un'etichetta booleana (T o F), il codice cliente (provvisorio) e la lista su cui
        scriverò la row.
    """

    def record(self, label: bool, toFill: list, traditionalRFM: int, aggregates: int,
               productRFM: int, productAggregates: int):
        for example in self.__examples:
            row = []
            
            if traditionalRFM == 1:
                desc = example.getDesc()
                for rfm in desc:
                    recency = rfm.getRecency()
                    frequency = rfm.getFrequency()
                    monetary = rfm.getMonetary()
                    row += [recency, frequency, monetary]
                
            if aggregates == 1:
                maximum = example.getMax()
                minimum = example.getMin()
                mean = example.getMean()
                standardDeviation = example.getStandardDeviation()
                row += [maximum.getRecency(), maximum.getFrequency(), maximum.getMonetary()]
                row += [minimum.getRecency(), minimum.getFrequency(), minimum.getMonetary()]
                row += [mean.getRecency(), mean.getFrequency(), mean.getMonetary()]
                row += [standardDeviation.getRecency(), standardDeviation.getFrequency(), standardDeviation.getMonetary()]
            
            if productRFM == 1 or productAggregates == 1:
                prodRfm = example.getProductRfm()
                minimum = example.getProductsMin()
                maximum = example.getProductsMax()
                mean = example.getProductsMean()
                standardDeviation = example.getProductsStandardDeviation()
                
                for i in range(len(prodRfm)):
                    if productRFM == 1:
                        for j in range(len(prodRfm[i])):
                            row += [prodRfm[i][j].getRecency(), prodRfm[i][j].getFrequency(), prodRfm[i][j].getMonetary()]
                    if productAggregates == 1:
                        row += [maximum[i].getRecency(), maximum[i].getFrequency(), maximum[i].getMonetary()]
                        row += [minimum[i].getRecency(), minimum[i].getFrequency(), minimum[i].getMonetary()]
                        row += [mean[i].getRecency(), mean[i].getFrequency(), mean[i].getMonetary()]
                        row += [standardDeviation[i].getRecency(), standardDeviation[i].getFrequency(), standardDeviation[i].getMonetary()]
            
            row += [example.getLabelTimestamp(), label]
            toFill.append(row)