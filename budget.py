class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.__balance = 0.0

  def __str__(self):
    heading = self.category.center(30, "*") + "\n"
    ledger = ""
    for item in self.ledger:
      line_description = f"{item['description'] : <23} "
      line_amount = f"{item['amount'] :>7.2f} "
      ledger += f"{line_description[:23]}{line_amount[:7]}\n"
    total = f"Total: {self.__balance :.2f}"
    return heading + ledger + total

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.__balance += amount

  def withdraw(self, amount, description=''):
    if self.__balance - amount >= 0:
      self.ledger.append({"amount": -1 * amount, "description": description})
      self.__balance -= amount
      return True

    return False

  def get_balance(self):
    return self.__balance

  def transfer(self, amount, deposit_category):
    if self.withdraw(amount, f'Transfer to {deposit_category.category}'):
      deposit_category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False
    
    

  def check_funds(self, amount):
    if amount > self.__balance:
      return False
    return True


def create_spend_chart(categories):
  amount_spent = []
  for category in categories:
    amount = 0
    for item in category.ledger:
      if item['amount'] < 0:
        amount += abs(item['amount'])
    amount_spent.append(round(amount, 2))

  total_spent = round(sum(amount_spent), 2)
  percentage_spent = list(
      map(lambda amount: int((((amount / total_spent) * 10) // 1) * 10),
          amount_spent))

  heading = "Percentage spent by category\n"

  chart = ""
  for value in reversed(range(0, 101, 10)):
    chart += str(value).rjust(3) + '|'
    for percent in percentage_spent:
      if percent >= value:
        chart += " o "
      else:
        chart += "   "
    chart += " \n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.category, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(
      map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
    footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

  return (heading + chart + footer).rstrip("\n")
