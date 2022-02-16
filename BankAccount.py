class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "Bank of Dojo"
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        self.balance = round(self.balance, 2)
        print("Balance is {}.".format(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.int_rate/self.balance
        return self

banker_1 = BankAccount(.50, 500)
banker_2 = BankAccount(.50, 1250)

banker_1.deposit(50).deposit(100).deposit(250).yield_interest()

banker_2.deposit(50).deposit(150).withdraw(20).withdraw(45).withdraw(50).withdraw(200).yield_interest()

banker_1.display_account_info()
banker_2.display_account_info()
