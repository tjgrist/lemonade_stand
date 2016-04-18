from lemonade import Lemonade
from random import randint 
from vendor import Vendor

class Customer:

	def __init__(self):
		self.chance = randint(1,100)
		#if weather is bad self.chance -= 20



	def buy(self,vendor,weather_score):
		#find more efficient way to do this
		price = vendor
		print("lemonade cost: ",price)
		randomize = randint(1,10)
		if weather_score + price >= 100:
			print("Yum!")
			return price
		if weather_score >= 90:
			print("Refreshing!")
			return price
		else:
			print("Not buying today.")

	def get_num_customers(self):
		print()


