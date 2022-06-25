class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    """
    The deposit function will take an amount 
    description of function
    """
    self.ledger.append({"amount": -amount, "description": description})

  def withdraw(self, amount, description=""):
    return None

  def chech_funds(self, amount):