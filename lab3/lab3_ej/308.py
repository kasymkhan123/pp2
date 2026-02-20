class Account :
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit (self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            return self.balance - amount
        else :
            return 'Insufficient Funds'

b, w = input().split()
ww = Account()
ww.deposit(int(b))
result = ww.withdraw(int(w))
print(result)

