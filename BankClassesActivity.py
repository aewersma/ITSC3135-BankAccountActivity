class BankAccount:
    title_of_bank = "Bank McBankface"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
        else:
            print("Cannot withdrawal, remaining balance would be below minimum. \n")

    def print_customer_information(self):
        print("Bank:", BankAccount.title_of_bank)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)

account1 = BankAccount("TestAcc1", 1500, 1000)
account1.deposit(2000)
account1.withdraw(3000)
account1.print_customer_information()

account2 = BankAccount("TestAcc2", 4000, 500)
account2.deposit(1000)
account2.withdraw(5000)
account2.print_customer_information()
