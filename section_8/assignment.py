# 17.12.23. Sergii Logosha sergiilogosha@gmail.com
# Last modified: 21.12.23

class CashRegister:

    def __init__(self, cashier):
        self.cashier = cashier
        self.purchase = {}
        self.products = {}
        self._subtotal = 0
        self._tax = 0
        self._total = 0

    def add_update_product(self, product):
        self.products[product['name']] = product

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]
        else:
            print("Product does not exist")

    def add_product_to_purchase(self, product):
        if product not in self.purchase:
            self.purchase[product] = self.products[product]
            self.purchase[product]['quantity'] = 1
        else:
            self.purchase[product]['quantity'] += 1

    def add_product_quantity(self, product, quantity=1):
        if product in self.purchase:
            self.purchase[product]['quantity'] = quantity
        else:
            print("Product is not in the basket")

    def change_product_quantity(self, product, quantity):
        if product in self.purchase:
            self.purchase[product]['quantity'] += quantity
        else:
            print("Product is not in the basket")

    def get_list_of_purchases(self):
        for product in self.purchase:
            print(f'{product} - quantity: {self.purchase[product]["quantity"]}')

    def remove_product_from_purchase(self, product):
        if product in self.purchase:
            del self.purchase[product]

    def change_product_price(self, product, price):
        if product in self.purchase:
            self.purchase[product]['price'] = price
        else:
            print("Product is not in the basket")

    def get_subtotal(self):
        for product_info in self.purchase.values():
            self._subtotal += product_info['price'] * product_info['quantity']
        print(f'The subtotal is: {self._subtotal}')
        return self._subtotal

    def get_5_perc_tax(self):
        self._tax = round(self._subtotal * 0.05, 2)
        print(f'The tax is {self._tax}')
        return self._tax

    def get_total(self):
        self._total = round(self._subtotal + self._tax, 2)
        print(f'The total is: {self._total}')
        return self._total

    def clear_purchase(self):
        self.purchase = {}
        self._subtotal = 0
        self._tax = 0
        self._total = 0


cash_register = CashRegister('Sergii')

cash_register.add_update_product({"name": "Pizza", "price": 10.34})
cash_register.add_update_product({"name": "Apple", "price": 2.13})
cash_register.add_update_product({"name": "Candy", "price": 5.54})
cash_register.add_update_product({"name": "Meat", "price": 18.25})
cash_register.add_update_product({"name": "Milk", "price": 12.64})
cash_register.add_update_product({"name": "Sugar", "price": 8.78})

cash_register.add_product_to_purchase('Pizza')
cash_register.change_product_quantity('Pizza', 5)
cash_register.add_product_to_purchase('Meat')
cash_register.add_product_to_purchase('Milk')
cash_register.remove_product_from_purchase('Meat')
cash_register.change_product_price('Pizza', 8.00)
cash_register.get_list_of_purchases()
cash_register.get_subtotal()
cash_register.get_5_perc_tax()
cash_register.get_total()
cash_register.clear_purchase()

