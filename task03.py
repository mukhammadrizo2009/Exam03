class Animal:
    def __init__(self , name: str ):
        """_summary_

        Args:
            name (str): _description_
            voise (str): _description_
        """
        self.name = name
        
class Dog(Animal):
    """_summary_

    Args:
        Animal (_type_): _description_
    """
    
    def bark(self):
        """_summary_
        """
        print("Woof! Woof!")
        
d = Dog("Rex")
print(d.name)
d.bark()