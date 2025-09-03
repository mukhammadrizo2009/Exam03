class Car:
    
    def __init__(self , brand: str , model: str , year: int):
        """_summary_

        Args:
            brand (str): _description_
            model (str): _description_
            year (int): _description_
        """
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_info(self):
        """_summary_
        """
        print(f"{self.brand} {self.model} ({self.year})")
        
        
car = Car("BMW" , "X5" , 2020)
car.get_info()