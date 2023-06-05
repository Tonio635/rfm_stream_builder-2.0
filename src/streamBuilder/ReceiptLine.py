"""
// Name        : ReceiptLine.py
// Author      : Antonio Giuseppe Doronzo
// Version     : 1.0
// Description : La classe ReceiptLine modella l'entry della tabella ReceiptLine del DB.
                 Essa contiene tutti i campi della tabella ReceiptLine come attributi e relativi metodi get.
                 Inoltre contiene l'ID della categoria della tabella Product a cui la tabella ReceiptLine fa riferimento.
"""


class ReceiptLine:

    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - categories: categorie del prodotto a cui fa riferimento la receiptline;
            - Quantity: quantità del prodotto acquistato, di tipo int;
            - Q_Amount: prezzo singolo, di tipo float;
            - Q_Discount_Amount: sconto singolo, di tipo int, al momento non trattato;
    """

    def __init__(self, categories, Quantity, Q_Amount, Q_Discount_Amount):
        self.__categories = categories
        self.__Quantity = Quantity
        self.__Q_Amount = Q_Amount
        self.__Q_Discount_Amount = Q_Discount_Amount

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
        Metodo getter attributo categories.
        Return di una lista di string.
    """
    def getCategories(self):
        return self.__categories
