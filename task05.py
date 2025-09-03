class Shape:
    
    def area(self , radius: int):
        """_summary_

        Args:
            radius (int): _description_
        """
        pass

class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
        
class Rectangle(Shape):
    
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        
    def area(self):   
        return self.length * self.width
        
c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())