"""
// Name        : RfmR.py
// Author      : Antonio Giuseppe Doronzo
// Version     : 1.0
// Description : La classe RfmR modella oggetti di tipo RfmR.
                 RFM è un modello utilizzato per analizzare il valore del cliente.
                 Questa classe serve per utilizzare oggetti di tipo Rfm ma con tutti gli attributi reali.
"""


class RfmR:
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
        Return di un tipo float.
    """

    def getRecency(self):
        return self.__recency

    """
        Metodo getter attributo Frequency.
        Return di un tipo float.
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
