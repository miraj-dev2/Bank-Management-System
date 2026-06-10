
class Account:
    def __init__(self,name,acc_no,acc_type,balance=0):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
        self.transactions=[]
    def deposit(self,amount):
        self.balance+=amount
        print(f"You deposited {amount}tk")
        print(f"Total balance is {self.get_balance()}tk")
        self.transactions.append({"type": "Deposit", "amount": amount})
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"You withdraw {amount}tk")
            print(f"Total balance is {self.get_balance()}tk")
            self.transactions.append({"type": "withdraw", "amount": amount})
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.balance
    def show_transaction(self):
        for i in self.transactions:
            print(f"type:{i['type']} : amount:{i['amount']}")
        

class Bank:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        name=input("Enter your name:").capitalize()
        acc_no=input("Enter your account no:")
        acc_type=input("Enter your acc_type:")
        if acc_type.lower() == "savings":
            new_acc = SavingsAccount(name, acc_no, acc_type)
        elif acc_type.lower() == "current":
            new_acc = CurrentAccount(name, acc_no, acc_type)
        else:
            print("Invalid account type. Choose Savings or Current")
            return
        
        self.accounts.append(new_acc)
        print("Account created successfully")
    def find_account(self, acc_no):
        for num in self.accounts:
            if num.acc_no == acc_no:
                return num
        return None
    def search_acc(self):
        acc_no=input("Enter your account number:")
        account=self.find_account(acc_no)
        if account is not None:
            print(f"name: {account.name}")
            print(f"account no: {account.acc_no}")
            print(f"account type: {account.acc_type}")
            print("Account found")
        else:
            print("Account not found")
        
    def delete_acc(self):
        acc_no=input("Enter your account number:")
        account=self.find_account(acc_no)
        if account is not None:
            self.accounts.remove(account)
            print("Account deleted")
        else:
            print("Account not found")
    def show_accounts(self):
        for i in self.accounts:
            print(f"name: {i.name}")
            print(f"account no: {i.acc_no}")
            print(f"account type: {i.acc_type}")
            print(".................................")
    def transfer(self):
        sender_accno=input("Enter your account number: ")
        sender = self.find_account(sender_accno)
        receiver_accno=input("Enter receiver account number: ")
        receiver=self.find_account(receiver_accno)
        t_amount=int(input("Enter the amount you want to transfer: "))
       
        if sender is not None and receiver is not None:
            
            if sender.balance >= t_amount:
                sender.withdraw(t_amount)
                print("__________________________")
                receiver.deposit(t_amount)
                print("Transaction Successful")
            else:
                print("Insufficient balance for transfer")
        else:
            print("Account not found")
class SavingsAccount(Account):
    def __init__(self, name, acc_no, acc_type, balance=0):
        super().__init__(name, acc_no, acc_type, balance)
        self.min_balance = 500
    def withdraw(self, amount):
        if self.balance - amount<self.min_balance:
            print("Cannot withdraw, minimum balance must be maintained")
        else:
            return super().withdraw(amount)
class CurrentAccount(Account):
    def __init__(self, name, acc_no, acc_type, balance=0):
        super().__init__(name, acc_no, acc_type, balance)
        self.overdraft_balance=1000
    def withdraw(self, amount):
        
        if self.balance+self.overdraft_balance>=amount:
            super().withdraw(amount)
            print("Withdraw successful")
        else:
            print("Overdraft limit exceeded")

class App:
    system= """
------Bank Management System---------
1.Create account
2.Search account
3.Delete account
4.Show all accounts
5.Deposit
6.Withdraw
7.Transfer
8.Show transactions
9.Exit
-------------------------------------"""
    def __init__(self):
        self.bank=Bank()
    def do_deposit(self):
        acc_no = input("Enter account number: ")
        account = self.bank.find_account(acc_no)
        if account is not None:
            amount = int(input("Enter amount: "))
            account.deposit(amount)
        else:
            print("Account not found")
    def do_withdraw(self):
        acc_no = input("Enter account number: ")
        account = self.bank.find_account(acc_no)
        if account is not None:
            amount = int(input("Enter amount: "))
            account.withdraw(amount)
        else:
            print("Account not found")
    def do_show_transaction(self):
        acc_no = input("Enter account number: ")
        account = self.bank.find_account(acc_no)
        if account is not None:
            account.show_transaction()
        else:
            print("Account not found")
            
    def run(self):
        actions={
            1: self.bank.create_account,
            2: self.bank.search_acc,
            3: self.bank.delete_acc,
            4: self.bank.show_accounts,
            5: self.do_deposit,
            6: self.do_withdraw,
            7: self.bank.transfer,
            8: self.do_show_transaction
        } 
        while True:
            print(self.system)
            choice=int(input("Enter choice (1-9): "))
            if choice==9:
                print("Goodbye!")
                break
            elif choice in actions:
                actions[choice]()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__== "__main__":
    App().run()