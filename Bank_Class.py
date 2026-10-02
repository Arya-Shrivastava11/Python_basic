class Account:
    bankName='RBI'
    def __init__(self):
        self.holderName=''
        self.balance=0
        self.accountno=0
        self.bool_answer=''
    def accept(self):
        self.holderName=input("Enter Holder's name:")
        self.accountno=int(input("Enter respective account no.:"))
        self.balance=float(input("Enter respective Balance:"))
    def deposit(self):
        deposit=float(input("Enter deposited amount:"))
        self.balance=deposit+self.balance
    def bool_withdrawal(self):
        withdrawal=float(input("Enter amount to be withdrawn:"))
        if self.balance>=withdrawal:
            self.bool_answer="True"
            self.balance=self.balance-withdrawal
        else:
            self.bool_answer="False"
    def display(self):
        print(self.holderName)
        print(self.accountno)
        print(self.bool_answer)
        print(self.balance)
        


obj=Account()
obj.accept()
obj.deposit()
obj.bool_withdrawal()
obj.display()
print(obj.bankName)