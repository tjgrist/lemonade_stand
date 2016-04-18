from supplies import Supplies 
from lemons import Lemons 

cash = Money()
lemons = Lemons()

class Vendor:

	def __init__(self):
		self.available_supplies = []
		self.recipe = 0
		
		self.lemons_quantity = 0
		self.sugar_quantity = 0
		self.ice_quantity = 0
		self.cups_quantity = 0

		self.price = 0


	def buy_lemons(self):
		print("\nYou can buy 10, 25, or 60 lemons at a time.")
		lemons_quantity = int(input("Enter how many lemons you need: "))
		#add try/except
		if lemons_quantity == 10:
			cash.subtract_money(lemons.price_10)
		elif lemons_quantity == 25:
			cash.subtract_money(lemons.price_25)
		elif lemons_quantity == 60:
			cash.subtract_money(lemons.price_60)
		self.lemons_quantity += lemons_quantity

		
	def buy_sugar(self):
		print("\nYou can buy 10, 25, or 60 cups of sugar at a time.")
		sugar_quantity = int(input("Enter how much sugar you need: "))
		#add try/except
		self.sugar_quantity += sugar_quantity

	def buy_ice(self):
		print("\nYou can buy 100, 250, or 500 ice cubes at time.")
		ice_quantity = int(input("Enter how many cubes you need: "))
		#add try/except
		self.ice_quantity += ice_quantity

	def buy_cups(self):
		print("\nYou can buy 10, 25, or 60 cups at time.")
		cups_quantity = int(input("Enter how many you need: "))
		#add try/except
		self.cups_quantity += cups_quantity

	def make_lemonade(self):
		default_recipe = 12
		print("The default recipe is 4 lemons/pitcher, 4 cups sugar/pitcher, and 4 ice cubes/pitcher.")
		alter = input("Would you like to change it? ").lower().replace(" ","")
		if alter == "yes":
			self.recipe = change_recipe()
		else:
			self.recipe = default_recipe

	def set_price(self):
		print("You can set your price anywhere between 1 and 5 dollars.")
		price = int(input("What shall the price be today? "))
		#try/except for int
		self.price = price

	def sell(self,price):
		price = price 

	def buy_more(self):
		answer = input("Would you like to buy more ingredients? ")
		if answer == "yes":
			ingredient = input("Which ingredient")

	def make_supplies_list(self):
		supplies = Supplies()
		lemons = self.lemons_quantity
		sugar = self.sugar_quantity
		ice = self.ice_quantity
		cups = self.cups_quantity
		supplies.show_supplies_list(lemons,sugar,ice,cups)

	# def change_price(self):

	# def change_recipe(self):

	
