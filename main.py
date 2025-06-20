from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount

s1 = SavingsAccount("testerName1", 3000, 1000, "123456", "111000", 0.05)
s2 = SavingsAccount("testerName2", 2000, 500, "654321", "111000", 0.03)

c1 = CheckingAccount("testerName3", 1500, 200, "112233", "111000", 500)
c2 = CheckingAccount("testerName4", 1000, 100, "332211", "111000", 300)

s1.add_interest()
s1.print_customer_information()
print()

s2.deposit(500)
s2.add_interest()
s2.print_customer_information()
print()

c1.transfer(400)
c1.print_customer_information()
print()

c2.transfer(400)
c2.print_customer_information()
