class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Suma depusă trebuie să fie pozitivă.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Suma retrasă trebuie să fie pozitivă.")
        if amount > self.balance:
            return False # Fonduri insuficiente
        self.balance -= amount
        return True