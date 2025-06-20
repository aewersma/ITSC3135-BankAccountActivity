class BankAccount:
    title_of_bank = "Bank McBankface"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
        else:
            print("Cannot withdrawal, remaining balance would be below minimum.\n")

    def print_customer_information(self):
        print("Bank:", BankAccount.title_of_bank)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
