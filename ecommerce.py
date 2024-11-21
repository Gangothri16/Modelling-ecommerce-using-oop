class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
    
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You Saved: {}".format(self.you_save))

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty):
        super().__init__(name, price, deal_price, ratings)
        self.warranty = warranty
    
    def get_warranty(self):
        return self.warranty
    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} Months".format(self.warranty))

class Grocery(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date
    
    def get_expiry_date(self):
        return self.expiry_date
    
    def display_product_details(self):
        super().display_product_details()
        print("Expiry: {} days".format(self.expiry_date))

class Order:
    delivery_charges = {
        "Prime_Members": 0,
        "Non-Prime_Members": 50
    }
    
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_address = delivery_address
        self.delivery_speed = delivery_speed
    
    def add_items(self, product, quantity):
        self.items_in_cart.append((product, quantity))
    
    def display_order_details(self):
        print("----------- Products In Cart --------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("---------------------------")
        print("Delivery Speed: {}".format(self.delivery_speed))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Delivery Charges: {}".format(Order.delivery_charges[self.delivery_speed]))
    
    def get_delivery_charges(cls):
        return Order.delivery_charges
    
    def calculate_total_bill(self):
        total = 0
        for product, quantity in self.items_in_cart:
            total += product.deal_price * quantity
        total += Order.delivery_charges[self.delivery_speed]
        return total

# Example usage
milk = Grocery("Milk", 20, 15, 4, 5)
tv = ElectronicItem("TV", 30000, 25000, 5, 10)
o = Order("Prime_Members", "Hyderabad")
o.add_items(milk, 3)
o.add_items(tv, 1)
o.display_order_details()
print("Total Bill: {}".format(o.calculate_total_bill()))
