"""
// Name        : Receipt.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
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
            - T_Receipt: Data e orario dell'acquisto;
            - lines: Receipt lines che formano la ricevuta.
    """
    def __init__(self, K_Receipt, K_Member, Quantity, Q_Amount, Q_Discount_Amount, T_Receipt, lines):
        self.__K_Receipt = K_Receipt
        self.__K_Member = K_Member
        self.__Quantity = Quantity
        self.__Q_Amount = Q_Amount
        self.__Q_Discount_Amount = Q_Discount_Amount
        self.__T_Receipt = T_Receipt
        self.__lines = lines

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
    
    """
        Metodo getter attributo lines.
        Return di un tipo lista di ReceiptLine.
    """
    def getLines(self):
        return self.__lines
    
    """
        Metodo finalizzato ad ottenere un dizionario delle categorie della ricevuta con il corrispettivo QAmount.
        Return di un dizionario.
    """
    def getInfoCategories(self, categories):
        # creazione di un dizionario per mantenere la somma delle qamount per ogni categoria
        categories_count = {}

        for line in self.__lines:
            categories_list = line.getCategories()
            q_amount = line.getQAmount()
            for category in categories_list:
                categories_count.setdefault(category, 0)
                categories_count[category] += q_amount

        info_categories = {category: categories_count.get(category, 0) for category in categories}

        return info_categories
