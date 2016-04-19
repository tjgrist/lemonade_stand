from supplies import Supplies 
from lemons import Lemons 
from sugar import Sugar
from ice import Ice 
from cups import Cups


lemons = Lemons()
sugar = Sugar()
ice = Ice()
cups = Cups()

class Vendor:

	def __init__(self):
		self.available_supplies = []
		self.recipe = 0

		self.price = 0


	def buy_lemons(self,cash,supplies):
		print("\nBuy some lemons! You can buy 10 at $1, 25 at $2, or 60 at $5.")
		lemons_quantity = int(input("Enter how many lemons you need: "))
		#add try/except
		if lemons_quantity == 10:
			cash.subtract_money(lemons.price_10)
			supplies.add_lemons(lemons_quantity)
		elif lemons_quantity == 25:
			cash.subtract_money(lemons.price_25)
			supplies.add_lemons(lemons_quantity)
		elif lemons_quantity == 60:
			cash.subtract_money(lemons.price_60)
			supplies.add_lemons(lemons_quantity)
		print("qua:",supplies.lemons)


	def buy_sugar(self,cash,supplies):
		print("\nBuy some sugar! You can buy 10 cups at $1, 25 at $2, or 60 at $5.")
		sugar_quantity = int(input("Enter how much sugar you need: "))
		#add try/except
		if sugar_quantity == 10:
			cash.subtract_money(sugar.price_10)
			supplies.add_sugar(sugar_quantity)
		elif sugar_quantity == 25:
			cash.subtract_money(sugar.price_25)
			supplies.add_sugar(sugar_quantity)
		elif sugar_quantity == 60:
			cash.subtract_money(sugar.price_60)
			supplies.add_sugar(sugar_quantity)
		print("qua:",supplies.sugar)


	def buy_ice(self,cash,supplies):
		print("\nBuy some ice! You can buy 100 cubes at $1, 250 at $2, or 500 at $5.")
		ice_quantity = int(input("Enter how many cubes you need: "))
		#add try/except
		if ice_quantity == 100:
			cash.subtract_money(ice.price_100)
			supplies.add_ice(ice_quantity)
		elif ice_quantity == 250:
			cash.subtract_money(ice.price_250)
			supplies.add_ice(ice_quantity)
		elif ice_quantity == 500:
			cash.subtract_money(ice.price_500)
			supplies.add_ice(ice_quantity)
		print("qua:",supplies.ice)


	def buy_cups(self,cash,supplies):
		print("\nYou can buy 10 at $1, 25 at $2, or 60 at $5 cups at time.")
		cups_quantity = int(input("Enter how many you need: "))
		#add try/except
		if cups_quantity == 10:
			cash.subtract_money(cups.price_10)
			supplies.add_cups(cups_quantity)
		elif cups_quantity == 25:
			cash.subtract_money(cups.price_25)
			supplies.add_cups(cups_quantity)
		elif cups_quantity == 60:
			cash.subtract_money(cups.price_60)
			supplies.add_cups(cups_quantity)
		print("qua:",supplies.cups)


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

	def make_supplies_list(self,supplies):
		lemons = supplies.lemons
		sugar = supplies.sugar
		ice = supplies.ice
		cups = supplies.cups
		supplies.show_supplies_list(lemons,sugar,ice,cups)
		
def sell(self,price):
		price = price 

	def buy_more(self):
		answer = input("Would you like to buy more ingredients? ")
		if answer == "yes":
			ingredient = input("Which ingredient")


	# def change_price(self):

	# def change_recipe(self):

	
