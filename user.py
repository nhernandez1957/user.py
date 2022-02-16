class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
# now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User: {}, Balance: {}.".format(self.name, self.account_balance))
        return self
    
    def transfer_money(self, receiver, amount):
        if self.account_balance < amount:
            print("{} cannot process this transaction.".format(self.name))
        else:
            self.account_balance -= amount
            receiver.account_balance += amount
            print("{} balance is {} and {} balance is {}.".format(self.name, self.account_balance, receiver.name, receiver.account_balance))
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
nick = User("Nick", "iambroke@gmail.com")

guido.make_deposit(100).make_deposit(200).make_deposit(100).make_deposit(50).make_withdrawal(45).display_user_balance()

monty.make_deposit(50).make_deposit(200).make_withdrawal(30).display_user_balance()

nick.make_deposit(20).make_withdrawal(5).make_withdrawal(10).make_withdrawal(10).display_user_balance()

guido.transfer_money(nick, 30)

