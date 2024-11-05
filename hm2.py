class Rectangle:
  def __init__(self, widht, height):
    self.widht = widht
    self.height = height
  def calulate_area(self):
   return self.widht * self.height
  def calculate_perimeter(self):
   return (self.widht + self.height) * 2

d = int(input())
e = int(input())
rectangle = Rectangle(d, e)
print(rectangle.calulate_area())
print(rectangle.calculate_perimeter())