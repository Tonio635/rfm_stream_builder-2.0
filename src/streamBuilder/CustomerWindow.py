import datetime as dt
from Day import Day

"""
// Name        : CustomerWindow.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : La classe CustomerWindow modella la finestra temporale di un singolo cliente, conservando
                 le giornate in cui ha acquistato in una lista a dimensione fissa, la data dell'ultimo acquisto e 
                 l'informazione sul cliente.
"""


class CustomerWindow:

    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - customer: K_Member, di tipo str;
            - dim: dimensione della CustomerWindow, di tipo intero.  
        Viene inoltre inizializzato l'attributo privato lastReceipt che mantiene la data dell'ultimo acquisto.
    """
    def __init__(self, customer: str, dim: int):
        self.__lastReceipt: dt.datetime = None
        self.__K_Member = customer
        self.__dim = dim
        self.__dayList = [None] * dim

    """
        Metodo getter K_Member.
        Return di un tipo int.
    """
    def getKMember(self):
        return self.__K_Member

    """
        Metodo getter lastReceipt.
        Return di un tipo datetime.
    """
    def getLastReceipt(self):
        return self.__lastReceipt

    """
        Metodo getter dayList. 
        Return di un tipo lista (di giorni della finestra temporale).
    """
    def getListOfDays(self):
        return self.__dayList

    """
        Metodo che inserisce un giorno all'interno della finestra
        aggiornando la data di ultimo acquisto.
    """
    def setDay(self, day: Day, lastReceiptTime: dt.datetime):
        self.__dayList[-1] = day
        self.__lastReceipt = lastReceiptTime

    """
        Metodo che 'shifta' la finestra rimuovendo il giorno più vecchio e aggiungendo un oggetto None alla fine.
    """
    def deleteFurthestDay(self):
        self.__dayList.pop(0)
        self.__dayList.append(None)

    """
        Metodo che verifica se l'utente non ha acquistato nemmeno un giorno nella finestra temporale.
    """
    def isEmpty(self):
        return self.__dayList == [None] * len(self.__dayList)

    """
        Override del metodo __str__.
        Return di un tipo string.
    """
    def __str__(self):
        return "\n".join(
            [f'Customer: {self.__K_Member}', f'Last Purchase: {self.__lastReceipt}', f'Days: {self.__dayList}\n']
        )

    """
        Override del metodo __repr__.
        Return di un tipo string.
    """
    def __repr__(self):
        return "\n".join(
            [f'Customer: {self.__K_Member}', f'Last Purchase: {self.__lastReceipt}', f'Days: {self.__dayList}\n']
        )
