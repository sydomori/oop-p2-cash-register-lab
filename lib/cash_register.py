#!/usr/bin/env python3

class CashRegister:
  def __init__(self,total, discount, items, previous_transactions):
    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transactions = []
  
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if not isinstance(value, int) or not (0 <= value <= 100):
      raise TypeError("Not valid discount")
    self._discount = value

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.items.extend([item] * quantity)
    self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})
    
  def apply_discount(self):
   if not self.discount:
    print("There is no discount to apply.")
    return
   self.total -= self.total * self.discount / 100

   last = self.previous_transactions.pop()
   self.total -= last["price"] * last["quantity"]
   for _ in range(last["quantity"]):
    self.items.remove(last["item"])



    
