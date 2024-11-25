class Bank_Account:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}, my current balance is {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw {amount}, My new balance is {self.balance}")
        else:
            print("Insufficient Balance")
account1=Bank_Account(123456789,1000)
account1.deposit(500)
account1.withdraw(200)