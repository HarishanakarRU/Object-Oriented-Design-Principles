class Order:
    current = []
    is_placed = False

    def __init__(self, name : str):
        self.name = name

    def add_item(self, item):
        if self.is_placed: 
            print("You cannot modify this order!") 
            return
        self.current.append(item)
        print(f"Item added to order: {item}")


    def repeat_order(self):
        print(f"Order placed: your order is {self.current}")

    def remove_item(self, item):
        if item in self.current:
            self.current.remove(item)
            print(f"Item removed from order: {item}")
        else:
            print("Item not in your order")
    
    def place(self):
        self.repeat_order()
        self.is_placed = True
        # send to kitchen

my_order = Order("Harish")
my_order.add_item("Apple")
my_order.add_item("Pancakes")
my_order.add_item("Sandwich")
my_order.add_item("Chicken Nuggets")
my_order.remove_item("Pancakes")
my_order.place()
my_order.add_item("Pancakes")