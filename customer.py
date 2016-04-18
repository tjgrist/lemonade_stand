from lemonade import Lemonade
from random import randint 
from vendor import Vendor

class Customer:

	def __init__(self):
		self.impulse


	def buy(self,price,temp,cloudiness):
		#find more efficient way to do this
		randomize = randint(1,10)
		if price <= 1 and temp >= 90 and cloudiness == "sunny" and randomize >= 2:
			print("Yum!")
			return price
		if price <= 1 and temp >= 80 and cloudiness == "sunny" and randomize >= 3:
			print("Refreshing!")
			return price
		if price <= 1 and temp >= 70 and cloudiness == "sunny" and randomize >= 4:
			print("Good!")
			return price
		if price <= 1 and temp >= 60 and cloudiness == "sunny" and randomize >= 6:
			print("Chilly but good.")
			return price
		if price == 2 and temp is 90 and cloudiness == "sunny" and randomize >= 4:
			print("Good.")
			return price
		if price == 2 and temp >=
		else:
			print("Not buying today.")


