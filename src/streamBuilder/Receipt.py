"""
// Name        : Receipt.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : La classe Receipt modella la singola entry della tabella Receipt del DB.
                 Essa contiene tutti i campi della tabella Receipt come attributi e relativi metodi get e set.
"""


class Receipt:

    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - K_Receipt: id della receipt, di tipo str;
            - K_Member: id del cliente, di tipo str;
            - Quantity: quantità del prodotto acquistato, di tipo int;
            - Q_Amount: prezzo totale, di tipo float;
            - Q_Discount_Amount: sconto totale, di tipo int, al momento non trattato;
            - T_Receipt: Data e orario dell'acquisto.
    """
    def __init__(self, K_Receipt, K_Member, Quantity, Q_Amount, Q_Discount_Amount, T_Receipt):
        self.__K_Receipt = K_Receipt
        self.__K_Member = K_Member
        self.__Quantity = Quantity
        self.__Q_Amount = Q_Amount
        self.__Q_Discount_Amount = Q_Discount_Amount
        self.__T_Receipt = T_Receipt

    """
        Metodo getter attributo K_Receipt.
        Return di un tipo str.
    """
    def getKReceipt(self):
        return self.__K_Receipt

    """
        Metodo getter attributo K_Member.
        Return di un tipo str.
    """
    def getKMember(self):
        return self.__K_Member

    """
        Metodo getter attributo Quantity.
        Return di un tipo int.
    """
    def getQuantity(self):
        return self.__Quantity

    """
        Metodo getter attributo Q_Amount.
        Return di un tipo float.
    """
    def getQAmount(self):
        return self.__Q_Amount

    """
        Metodo getter attributo Q_Discount_Amount.
        Return di un tipo int.
    """
    def getQDiscountAmount(self):
        return self.__Q_Discount_Amount

    """
        Metodo getter attributo T_Receipt.
        Return di un tipo datetime.
    """
    def getTReceipt(self):
        return self.__T_Receipt
