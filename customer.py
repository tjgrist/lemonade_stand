from lemonade import Lemonade
from random import randint 
from vendor import Vendor
from money import Money 

class Customer:

	def __init__(self):
		self.chance = randint(1,100)
		#if weather is bad self.chance -= 20



	def buy(self,price,cash,weather_score):
		print("lemonade cost: ",price)
		randomize = randint(1,10)
		if weather_score + price >= 100:
			print("Yum!")
			cash.add_money(price)
			print("cash:",cash.dollars)
		if weather_score >= 90:
			print("Refreshing!")
			cash.add_money(price)
			print("cash:",cash.dollars)
		else:
			print("Not buying today.")

	def get_num_customers(self):
		print()


