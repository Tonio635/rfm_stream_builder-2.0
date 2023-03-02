"""
// Name        : Rfm.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : La classe Rfm modella oggetti di tipo Rfm.
                 RFM è un modello utilizzato per analizzare il valore del cliente.
                 Con questa tecnica non facciamo altro che classificare gli acquirenti, usando come criterio lo storico
                 delle transazioni: quando (recency), quante volte (frequency) e quanto (monetary) hanno acquistato
                 nell’arco temporale considerato.
"""


class Rfm:
    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - Recency: quanto tempo è trascorso dall'ultima attività o transazione;
            - Frequency: con quale frequenza un cliente ha effettuato transazioni o interagito;
            - Monetary: questo fattore riflette quanto un cliente ha speso.
    """
    def __init__(self, recency, frequency, monetary):
        self.__recency = recency
        self.__frequency = frequency
        self.__monetary = monetary

    """
        Metodo getter attributo Recency.
        Return di un tipo int.
    """
    def getRecency(self):
        return self.__recency

    """
        Metodo getter attributo Frequency.
        Return di un tipo int.
    """
    def getFrequency(self):
        return self.__frequency

    """
        Metodo getter attributo Monetary.
        Return di un tipo float.
    """
    def getMonetary(self):
        return self.__monetary

    """
        Override del metodo __str__.
        Return di un tipo string
    """
    def __str__(self):
        return " ".join([str(self.getRecency()), str(self.getFrequency()), str(self.getMonetary())])

    """
        Override del metodo __repr__.
        Permette di stampare il contenuto.
        Return di un tipo string
    """
    def __repr__(self):
        return " ".join([str(self.getRecency()), str(self.getFrequency()), str(self.getMonetary())])
