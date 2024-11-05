class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
  def calculate_total_price(self):
    print("total price:", self.price * self.quantity)
  def display(self):
    print(f"name:{self.name} price:{self.price} quantity:{self.quantity}")

tea = Product("tea", 20, 5)
tea.display()
tea.calculate_total_price()