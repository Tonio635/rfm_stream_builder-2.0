class CategoryMapping:

    def __init__(self, products):
        self.__products = products

    def getProductCategories(self, KProduct):
        return self.__products[KProduct]

    def getDistinctCategories(self):
        categories = set()
        
        for category_list in self.__products.values():
            for category in category_list:
                categories.add(category)

        return list(categories)