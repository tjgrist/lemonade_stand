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
		self.recipe = 0
		self.price = 0


	def buy_supplies(self,cash,supplies,vendor):
		if supplies.check_supplies(vendor,cash,supplies) == True:
			pass
		else: 
			print("\nYou need some things!")
			self.buy_lemons(cash,supplies)
			self.buy_sugar(cash,supplies)
			self.buy_ice(cash,supplies)
			self.buy_cups(cash,supplies)

		
	def make_supplies_list(self,supplies):
		supplies.show_supplies_list(supplies.lemons, supplies.sugar, supplies.ice, supplies.cups)


	def get_list_buy(self,supplies,cash,vendor):
		self.make_supplies_list(supplies)
		self.buy_supplies(cash,supplies,vendor)
		self.make_supplies_list(supplies)


	def set_price(self):
		print("You can set your price anywhere from $1-4")
		price = input("What shall the price be today? $")
		try: 
			new_price = float(price)
			self.price = new_price
		except:
			print("Try entering a numeric value.")
			self.set_price()


	def buy_lemons(self,cash,supplies):
		print("\nBuy some lemons! You can buy 10 @ $2, 25 @ $4, or 60 @ $7.")
		lemons_quantity = input("Enter how many lemons you need: ")
		try:
			amount = int(lemons_quantity)
			if amount == 10:
				cash.subtract_money(lemons.price_10)
				supplies.add_lemons(amount)
			elif amount == 25:
				cash.subtract_money(lemons.price_25)
				supplies.add_lemons(amount)
			elif amount == 60:
				cash.subtract_money(lemons.price_60)
				supplies.add_lemons(amount)
		except:
			print("\nOops. Try entering a numeric value.")
			self.buy_lemons(cash,supplies)
		

	def buy_sugar(self,cash,supplies):
		print("\nBuy some sugar! You can buy 10 cups @ $2, 25 @ $4, or 60 @ $7.")
		sugar_quantity = input("Enter how much sugar you need: ")
		try: 
			amount = int(sugar_quantity)
			if amount == 10:
				cash.subtract_money(sugar.price_10)
				supplies.add_sugar(amount)
			elif amount == 25:
				cash.subtract_money(sugar.price_25)
				supplies.add_sugar(amount)
			elif amount == 60:
				cash.subtract_money(sugar.price_60)
				supplies.add_sugar(amount)
		except:
			print("\nOops. Try entering a numeric value.")
			self.buy_sugar(cash,supplies)
		

	def buy_ice(self,cash,supplies):
		print("\nBuy some ice! You can buy 100 cubes @ $2, 250 @ $4, or 500 @ $7.")
		ice_quantity = input("Enter how many cubes you need: ")
		try: 
			amount = int(ice_quantity)
			if amount == 100:
				cash.subtract_money(ice.price_100)
				supplies.add_ice(amount)
			elif amount == 250:
				cash.subtract_money(ice.price_250)
				supplies.add_ice(amount)
			elif amount == 500:
				cash.subtract_money(ice.price_500)
				supplies.add_ice(amount)
		except:
			print("\nOops. Try entering a numeric value.")
			self.buy_ice(cash,supplies)
	

	def buy_cups(self,cash,supplies):
		print("\nYou can buy 10 @ $2, 25 @ $4, or 60 @ $7 cups at time.")
		cups_quantity = input("Enter how many you need: ")
		try:
			amount = int(cups_quantity)
			if amount == 10:
				cash.subtract_money(cups.price_10)
				supplies.add_cups(amount)
			elif amount == 25:
				cash.subtract_money(cups.price_25)
				supplies.add_cups(amount)
			elif amount == 60:
				cash.subtract_money(cups.price_60)
				supplies.add_cups(amount)
		except:
			print("\nOops. Try entering a numeric value.")
			self.buy_cups(cash,supplies)


	def craft_lemonade(self):
			default_recipe = 10
			print("The default recipe is 5 lemons/pitcher, 5 cups sugar/pitcher, and 10 ice cubes/pitcher.")
			alter = input("Would you like to change it? ").lower().replace(" ","")
			if alter == "yes":
				self.recipe = change_recipe()
			else:
				self.recipe = default_recipe


	










































	# def change_recipe(self):

	
