class Flyer:
     def __init__(self , name: str):
         """_summary_

         Args:
             name (str): _description_
         """
         
         self.name = name
         
     def fly(self):
         print(f"{self.name} is flying")

class Swimmer:
    def __init__(self , name: str):
        """_summary_

        Args:
            name (str): _description_
        """
        
        self.name = name
        
    def swim(self):
        print(f"{self.name} is swimming")


class Duck(Flyer , Swimmer):
    pass

duck = Duck("Duck")
duck.fly()
duck.swim()