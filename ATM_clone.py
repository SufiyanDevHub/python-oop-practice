class ATM():
    def __init__(self):
        self.pin = ""
        self.balance=0
        self.menu()


    def menu(self):
         while True:
      
            user_input=input("""  
        How would you like to proceed.
        1.Enter 1 to create pin.
        2. Enter 2 to deposite
        3. Enter 3 to withdraw
        4. Enter 4 to Check balance
        5. Enter 5 to exit.
                      
        """)
    
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposite()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input == "5":
                print("Exit")
                break
            else:
                print("Invalid option")

    def create_pin(self):
        self.pin = input("Enter your new pin")
        print("Pin set successfully")

    def deposite(self):
         if self.pin == "":
            
             print("Please create PIN first")
             return

        temp= input("Enter your pin code")
        if temp==self.pin:
            amount= int(input("Enter amount to deposit"))
            self.balance=self.balance+amount
            print("Deposit Successful")

        else:
            print("Invalid Input!")

    def withdraw(self):
        if self.pin == "":
            
            print("Please create PIN first")
            return
        temp= input("Enter your pin code")
        if temp==self.pin:
            amount=int(input("Enter amount to withdraw"))

            if self.balance>=amount:
                self.balance=self.balance-amount
                pritn("Withdraw successful")
            else:
                print("Insufficent balance")

            

        else:
            print("Invalid pin!")

    def check_balance(self):
        if self.pin == "":
            
            print("Please create PIN first")
            return
        temp = input("Enter your pin code")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid pin!")


mcb= ATM()

mcb.menu()
