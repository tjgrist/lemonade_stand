from lemonade import Lemonade
from random import randint 
from vendor import Vendor
from money import Money 
from supplies import Supplies

class Customer:

	def __init__(self):
		self.chance = randint(1,100)
		#if weather is bad self.chance -= 20


	def buy(self,price,cash,weather_score,supplies,vendor,lemonade):
		print("lemonade cost: $",price)
		print("Customer chance:",self.chance)

		if supplies.check_supplies(vendor) == True:

			if weather_score >= 100 and self.chance >= 10 and price <= 3:
				print(self.customer_says(),"Yum!")
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			elif weather_score >= 90 and self.chance >= 20 and price <= 2:
				print(self.customer_says(),"Refreshing!")
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			elif weather_score >= 80 and self.chance >= 30 and price <= 2: 
				print(self.customer_says(),"Good Lemonade")
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			elif weather_score >= 70 and self.chance >= 40 and price <=1:
				print(self.customer_says(),"Too cold but tasty.")
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			elif weather_score >= 60 and self.chance >= 50 and price <=1: 
				print(self.customer_says(),"Chilly, but pretty good.")	
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			elif weather_score >= 50 and self.chance >= 40 and price <= 1:
				print(self.customer_says(),"It's too cold, but the sugar warms me up.")	
				cash.add_money(price)
				lemonade.subtract_drink()
				print("lemonade available: ",lemonade.drinks)

			else:
				print(self.customer_says(),"Not buying today.")
				print("Cash in hand:",cash.dollars)

		else: 
			print("\nYou're out of some ingredients!")
			vendor.make_supplies_list(supplies)

	def get_customers(self):
		print()
		if weather_score >= 90:
			print()

	def customer_says(self):
		print("\nCustomer says:")

