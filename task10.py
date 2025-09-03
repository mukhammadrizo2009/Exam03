class Person:
    def __init__(self , name: str , age: int , work: str):
        """_summary_

        Args:
            name (str): _description_
            age (int): _description_
            work (str): _description_
        """
        
        self.name = name
        self.age = age
        self.work = work
        
    def get_info(self):
        print(f"{self.name}, {self.age} years old, works at {self.work}!")
        
        
class Employee(Person):
    def __init__(self, name, age, work):
        super().__init__(name, age, work)
    
        
e = Employee("Hasan", 25, "Google")
e.get_info()