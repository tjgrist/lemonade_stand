from lemonade import Lemonade
from random import randint 
from vendor import Vendor
from money import Money 
from supplies import Supplies
from weather import Weather

class Customer:

	def __init__(self):
		self.chance = randint(1,100)


	def get_customers(self,price,cash,weather_score,supplies,vendor,lemonade):
		customers_out = 0
		
		if weather_score >= 85:
			while customers_out < 20:
				customer = Customer()
				customer.buy(price, cash, weather_score, supplies, vendor, lemonade)
				customers_out += 1

		elif weather_score >= 70:
			while customers_out < 15:
				customer = Customer()
				customer.buy(price, cash, weather_score, supplies, vendor, lemonade)
				customers_out += 1

		elif weather_score >= 60:
			while customers_out < 10:
				customer = Customer()
				customer.buy(price, cash, weather_score, supplies, vendor, lemonade)
				customers_out += 1
	
	def buy(self,price,cash,weather_score,supplies,vendor,lemonade):

		if supplies.check_supplies(vendor,cash,supplies) == True:

			if weather_score >= 100 and self.chance >= 10 and price <= 4:
				self.customer_says()
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			elif weather_score >= 90 and self.chance >= 20 and price <= 3:
				self.customer_says()
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			elif weather_score >= 80 and self.chance >= 30 and price <= 2: 
				self.customer_says()
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			elif weather_score >= 70 and self.chance >= 40 and price <=2:
				self.customer_says()
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			elif weather_score >= 60 and self.chance >= 50 and price <=1: 
				self.customer_says()
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			elif weather_score >= 40 and self.chance >= 50 and price <= 1:
				print("Customer says:\n'It's too cold, but the sugar warms me up.'"	)
				cash.add_money(price)
				lemonade.subtract_drink()
				lemonade.get_lemonades()

			else:
				print("Customer says:\n'Not buying today.'")
				print("\nCash in hand:",cash.dollars)

		else: 
			print("\nYou're out of some ingredients!")
			vendor.make_supplies_list(supplies)

	def customer_says(self):
		response = randint(1,5)
		if response == 1:
			response = "'Yum!'"
		elif response == 2:
			response = "'Refreshing!'"
		elif response == 3:
			response = "'Good Lemonade.'"
		elif response == 4:
			response = "'Too cold but tasty.'"
		elif response == 5:
			response = "'Yummy lemonade.'"	
		print("\nYou got a customer! They say:",response)

