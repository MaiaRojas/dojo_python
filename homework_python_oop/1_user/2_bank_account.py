# Homework
import stat


class BankAccount:
  # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
  accounts = []
  def __init__(self, int_rate = 0, balance = 0): 
    self.int_rate = int_rate
    self.balance = balance
    BankAccount.accounts.append(self)

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance += amount
    else:
      print("Insufficient Funds")
    return self

  def show_info_account(self):
    print(f'Balance:  {self.balance}')

  def yield_interest(self):
    if self.balance > 0:
      self.balance = self.balance * (1 + self.int_rate)
    else:
      print("No interests given")
    return self

  @classmethod
  def print_all_acounts(cls):
    for account in cls.accounts:
      print(f'Balance: {account.balance}')


# ***************
# Driver Code
# ***************

savings = BankAccount(.05,2000)
checking = BankAccount(.02,8000)

print("*"*50)

savings.deposit(10).deposit(20).deposit(40).yield_interest().show_info_account()
checking.deposit(800).deposit(800).withdraw(200).withdraw(50).withdraw(100).withdraw(60).yield_interest().show_info_account()

#Bonus
BankAccount.print_all_acounts()