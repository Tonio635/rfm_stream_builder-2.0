"""
// Name        : ExampleDictionary.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe che modella la sequenza di esempi. È formata da un unico attributo: la lista di ExampleSequence
                 Ogni K_Member di Receipts è chiave nel dizionario dict <k, v> dove v: è di tipo ExampleSequence.
"""

from Example import Example
from ExampleSequence import ExampleSequence
import datetime as dt


class ExampleDictionary:

    """
        Metodo costruttore che inizializza un dizionario vuoto.
        examples{} conterrà tutte le ExampleSequence indicizzate dal K_Member opportuno.
    """
    def __init__(self):
        self.__examples = {}

    """
        Metodo getter per examples.
        Return di un dizionario.
    """
    def getDict(self):
        return self.__examples

    """
        Metodo che verifica l'esistenza della chiave passata come parametro nella lista delle chiavi.
    """
    def containsKey(self, customer: str):
        return True if customer in self.__examples.keys() else False

    """
        Metodo per inserire un esempio nell' ExampleSequence all'interno del dizionario con chiave customer.
    """
    def insertExample(self, customer: str, ex: Example):
        if customer not in self.__examples:
            exampleSeq = ExampleSequence()
            exampleSeq.appendExample(ex)
            self.__examples[customer] = exampleSeq
        else:
            self.__examples[customer].appendExample(ex)

    """
        Metodo per cancellare un item dal dizionario avente in input un customer.
        Utilizzo di del per rendere efficiente la cancellazione.
    """
    def delete(self, customer: str):
        del self.__examples[customer]

    """
        Metodo per etichettare gli esempi nel dizionario. Richiama record di ExampleSequence.
    """
    def recordLabeledExample(self, customer: str, label: bool, timestamp: dt.datetime, toFill: list):
        self.__examples[customer].setLabelTimestamp(timestamp)
        self.__examples[customer].record(label, toFill)
