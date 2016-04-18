class Vendor:

	def __init__(self):
		self.available_supplies = []


	def buy_lemons(self):
		print("You can buy 10, 25, or 60 lemons at a time.")
		lemons_quantity = int(input("Enter how many lemons you need: "))
		#add try/except
		return lemons_quantity

	def buy_sugar(self):
		print("You can buy 10, 25, or 60 cups of sugar at a time.")
		sugar_quantity = int(input("Enter how much sugar you need: "))
		#add try/except
		return sugar_quantity

	def buy_ice(self):
		print("You can buy 100, 250, or 500 ice cubes at time.")
		ice_quantity = int(input("Enter how many cubes you need: "))
		#add try/except
		return ice_quantity

	def buy_cups(self):
		print("You can buy 10, 25, or 60 lemons at time.")
		cups_quantity = int(input("Enter how many you need: "))
		#add try/except
		return cups_quantity

	def make_lemonade(self):
		default_recipe = 12
		print("The default recipe is 4 lemons/pitcher, 4 cups sugar/pitcher, and 4 ice cubes/pitcher.")
		alter = input("Would you like to change it? ").lower().replace(" ","")
		if alter == "yes":
			return change_recipe()
		else:
			return default_recipe

	def set_price(self):
		print("You can set your price anywhere between 1 and 5 dollars.")
		price = int(input("What shall the price be today? "))
		#try/except for int
		return price

	def sell(self,price):
		price = price 
		
	# def change_price(self):

	# def change_recipe():
