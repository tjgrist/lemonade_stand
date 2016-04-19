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
		if weather_score + price >= 100:
			print(self.customer_says(),"Yum!")
			cash.add_money(price)
			print("Cash in hand:",cash.dollars)

		elif weather_score >= 90:
			print(self.customer_says(),"Refreshing!")
			cash.add_money(price)
			print("Cash in hand:",cash.dollars)

		elif weather_score >= 80: 
			print(self.customer_says(),"Good Lemonade")
			cash.add_money(price)
			print("Cash in hand:",cash.dollars)

		elif weather_score >= 70:
			print(self.customer_says(),"Too cold but tasty.")
			cash.add_money(price)
			print("Cash in hand:",cash.dollars)

		elif weather_score >= 60: 
			print(self.customer_says(),"Chilly, but pretty good.")	
			cash.add_money(price)
			print("Cash in hand:",cash.dollars)

		else:
			print(self.customer_says(),"Not buying today.")
			print("Cash in hand:",cash.dollars)

	def get_num_customers(self):
		print()
		if weather_score >= 90:
			print()

	def customer_says(self):
		print("\nCustomer says:")

