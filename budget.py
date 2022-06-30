class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    """
    The deposit function will take an amount 
    description of function
    """
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
    else:
      print("Insufficient funds")

  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def get_balance(self):
    total = 0
    for trans in self.ledger:
      total += trans["amount"]
    return total

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + category.name)