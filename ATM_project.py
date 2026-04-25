class ATM():

    def __init__(self):
        self.pin=""
        self.balance= 0
        self.menu()

    def menu(self):
        user_input= input(""" 
        Hello! How would you like to proceed...

        1. Enter 1 to create PIN.
        2. Enter 2 to deposite.
        3. Enter 3 to withdraw.
        4. Enter 4 to check balance.
        5. Enter 5 to exit...
        :
        """)

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposite()
        elif user_input=="3":
            self.winthdraw()
        elif user_input=="4":
            self.check_balance
        else:
            print("Exit")


    def create_pin(self):
        self.pin = input("Enter your new pin")
        print("Pin set successfully!")

    def deposite(self):
        temp = input("Enter your pin")
        if temp== self.pin:
            amount = int(input("Enter amount to deposite"))
            self.balance= self.balance + amount
            print("Deposite Successfull")

        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp==self.pin():
            amount= int(input("Enter amount to withdraw"))
            if self.balance>amount:
                self.balance= self.balance-amount

                print("withdraw Successfull")

            else:
                print("Insufficent balance!")

        else:
            print("Invalid Pin")

    def check_balance(self):
        temp= input("Enter your Pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")


ubl = ATM()

ubl.menu()