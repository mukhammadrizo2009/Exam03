class Student:
    def __init__(self , name: str , age: int , course: int ):
        """_summary_

        Args:
            name (str): _description_
            age (int): _description_
            course (int): _description_
        """
        self.name = name
        self.age = age
        self.course = course
        
    def introduse(self):
        print(f"My name is {self.name}, I am {self.age} years old, styding in {self.course} course!")
        

s = Student("Ali" , 20 , 2)
s.introduse()