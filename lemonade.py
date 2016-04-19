

class Lemonade:

	def __init__(self):
		self.default_recipe = 12
		self.price = 0
		self.drinks = 0

	def make_lemonade(self,lemons,sugar,ice,cups):
		pitchers = int((lemons + sugar + ice)/4)
		extra =  pitchers - cups
		self.drinks = pitchers - extra
		print("Number of lemonades you can make:",self.drinks)