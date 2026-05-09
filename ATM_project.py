class ATM():
    def __init__(self):
        self.pin = None
        self.balance = 0
        

    def menu(self):
        while  True:
        
            user_input = input("""
            How would you like to process!
            Enter 1 to create Pin.
            Enter 2 to Deposite.                  
            Enter 3 to Withdraw.
            Enter 4 to Check balance.
            Enter 5 to Exit.....
            --------------->""") 
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposite()
            elif user_input == "3":
                self.withdraw()
            
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exit")
                break
            
            else:
                print("Invalid Option")

    def create_pin(self):
        self.pin = input("Enter your new PIN Code.")
        print("PIN set Successfully!")

    def deposite(self):
        if self.pin is None:
            print("Please create Pin First")
            return
        temp = input("Enter your pin code")
        if temp == self.pin:
            amount = int(input("Enter amount to deposite"))
            if amount<=0:
                print("Please Enter valid Amount")
                return
            self.balance = self.balance + amount
            print("Deposite Successfull")
        else:
            print("Invalid Pin")

    def withdraw(self):
        if self.pin is None:
            print("Please create Pin First")
            return
        temp = input("Enter your pin code")
        if temp== self.pin:
            amount  = int(input("Enter amount to withdraw"))
            if amount<=0:
                print("Please Enter valid amount")
                return
            if self.balance>=amount:
                self.balance = self.balance - amount
                print("Withdraw Succesfull")
            else:
                print("Insufficent Balance!")
        else:
            print("Invalid Pin")
    def check_balance(self):
        if self.pin is None:
            print("Please create Pin First")
            return
        temp = input("Enter your pin code")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
ubl = ATM ()
ubl.menu()
