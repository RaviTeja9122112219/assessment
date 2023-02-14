class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("{} deposited {}".format(self.name, amount))
        self.check_balance()

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("{} withdrew {}".format(self.name, amount))
        self.check_balance()

    def check_balance(self):
        print("{}'s current balance is {}".format(self.name, self.balance))

account = BankAccount("Raviteja", 0)
account.deposit(500)
account.withdrawal(200)
account.withdrawal(2000)
