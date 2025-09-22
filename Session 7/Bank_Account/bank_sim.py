import psycopg2

print("Welcome to the Bank Simulator")

choice = input("Are you a new user? (y/n): ")

if choice.lower() == 'y':
    name = input("Name: ")
    if(name):
        pass1 = input("Enter password: ")
        pass2 = input("Confirm password: ")
        if pass1 == pass2:
            conn = psycopg2.connect(
                    host= "localhost",
                    database= "bank_db",
                    user= "postgres",
                    password= "satyam"
                )
            cur = conn.cursor()
            cur.execute("INSERT INTO accounts (name, password, balance) VALUES (%s,%s,%s) RETURNING account_id",
                        (name, pass1, 0.00))
            account_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            print(f"Account created! Your account ID is {account_id}")
            print("Please login now.")
        else:
            print("Passwords do not match. Exiting.")
            exit()
    else:
        print("Enter valid username")


else:
    class BankAccount:
        def __init__(self, account_id, password):
            self.account_id = account_id
            self.password = password
            self.conn = psycopg2.connect(
                host= "localhost",
                database= "bank_db",
                user= "postgres",
                password= "satyam"
            )
            self.cur = self.conn.cursor()
        
            self.cur.execute("SELECT account_id, balance, password from accounts WHERE account_id = %s", (self.account_id,))
            result = self.cur.fetchone()
            if result:
                self.account_id, self.balance, stored_password = result
                if stored_password != password:
                    print("Wrong password")
                    self.close()
                    exit()
                print(f"Logged in")
                
            else:
                print("User not found.")
                # new_account = input("Do you want to create a new account (y/n): ")
                # if new_account == "y":
                #     pass1 = input("Enter new password: ")
                #     pass2 = input("confirm password: ")
                #     self.name = input("Name of account to be created: ")
                #     if pass1 == pass2:
                #         password = pass1
                #         self.cur.execute("INSERT INTO accounts (name, password, balance) VALUES(%s, %s, %s) RETURNING account_id", (self.name, self.password, 0.00))
                #         self.account_id = self.cur.fetchone()[0]
                #         self.balance = 0.00
                #         self.conn.commit()
                #         print(f"New account created for {self.name}")
                #     else:
                #         print("Password do not match")
                #         self.close()
                #         exit()
                # else:
                    # self.close()
                    # exit()
                self.close()
                exit()
            
        def deposit(self, amount):
            if amount <= 0:
                print("Invalid amount entered, it should be a positive number")
            else:
                
                self.balance = float(self.balance) + amount
                self.cur.execute("UPDATE accounts SET balance = %s WHERE account_id= %s", (self.balance, self.account_id))
                self.conn.commit()
                print(f"Deposited {amount:.2f}. Current Balance: {self.balance:.2f}")
        
        def withdraw(self, amount):
            if amount <= 0:
                print("Invalid withdrawal, Withdrawal must be a positive amount.")
            if amount > self.balance:
                print(f"Insufficient Balance. Current Balance: {self.balance:.2f}")
            else:
                self.balance = float(self.balance) - amount
                self.cur.execute("UPDATE accounts SET balance = %s WHERE account_id = %s", (self.balance, self.account_id))
                self.conn.commit()
                print(f"Withdrew {amount:.2f}, Remaining Current Balance: {self.balance:.2f}")
            
        def check_balance(self):
            print(f"Current balance: {self.balance:.2f}")
        
        def close(self):
            self.cur.close()
            self.conn.close()
        



    print("Welcome to the Bank Simulator")
    account_id = input("Enter your Account ID: ")
    password = input("Enter your Password: ")

    account = BankAccount(account_id, password)

    while True:
        print("\n Choose action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Goodbye!")
            account.close()
            break
        else:
            print("Invalid choice. Try again.")