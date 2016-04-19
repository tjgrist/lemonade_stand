# from supplies import Supplies 
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

	def buy_stuff(self,cash,supplies,vendor):
		if supplies.check_supplies(vendor,cash,supplies) == True:
			pass
		else: 
			print("\nYou're out of some ingredients!\n")
			# self.buy_stuff(cash, supplies, vendor)
			self.buy_lemons(cash,supplies)
			self.buy_sugar(cash,supplies)
			self.buy_ice(cash,supplies)
			self.buy_cups(cash,supplies)

		
	def buy_lemons(self,cash,supplies):
		print("\nBuy some lemons! You can buy 10 @ $2, 25 @ $4, or 60 @ $7.")
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

	def buy_sugar(self,cash,supplies):
		print("\nBuy some sugar! You can buy 10 cups @ $2, 25 @ $4, or 60 @ $7.")
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

	def buy_ice(self,cash,supplies):
		print("\nBuy some ice! You can buy 100 cubes @ $2, 250 @ $4, or 500 @ $7.")
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

	def buy_cups(self,cash,supplies):
		print("\nYou can buy 10 @ $2, 25 @ $4, or 60 @ $7 cups at time.")
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

	def set_price(self):
		print("You can set your price anywhere from $1-4")
		price = int(input("What shall the price be today? "))
		#try/except for int
		self.price = price

	def make_supplies_list(self,supplies):
		lem = supplies.lemons
		sug = supplies.sugar
		ice = supplies.ice
		cup = supplies.cups
		supplies.show_supplies_list(lem,sug,ice,cup)

	def sell(self,price):
		price = price 

	def craft_lemonade(self):
			default_recipe = 10
			print("The default recipe is 4 lemons/pitcher, 4 cups sugar/pitcher, and 4 ice cubes/pitcher.")
			alter = input("Would you like to change it? ").lower().replace(" ","")
			if alter == "yes":
				self.recipe = change_recipe()
			else:
				self.recipe = default_recipe

	def buy_more(self,cash,supplies):
		answer = input("Would you like to buy more ingredients? ").lower().replace(" ","")
		if answer == "yes":
			self.buy_lemons(cash,supplies)
			self.buy_sugar(cash,supplies)
			self.buy_ice(cash,supplies)
			self.buy_cups(cash,supplies)


	# def change_price(self):

	# def change_recipe(self):

	
