# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class account:
    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance is:", self.get_balance())

    #creditmethod
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance is:", self.get_balance())

    # final balance
    def get_balance(self):
        return self.balance

acc1 = account(10000, 12345)
acc1.debit(500)
acc1.credit(900)
acc1.debit(4000)
acc1.credit(150000000)
acc1.debit(150000000)

