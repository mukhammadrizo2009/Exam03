class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def deposit(self, amount: int):
        self.__balance += amount

    def withdraw(self, amount: int):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Pulingiz yo'qku!")
            
    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())
