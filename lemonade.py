
class Lemonade:

	def __init__(self):
		self.default_recipe = 10
		self.price = 0
		self.drinks = 0
		self.pitchers = 0 


	def make_lemonade(self,lemons,sugar,ice,cups):
		pitchers = int((lemons + sugar + ice)/5)
		extra =  pitchers - cups
		self.drinks = pitchers - extra
		print("Number of lemonades you can make:",self.drinks)


	def subtract_drink(self):
		self.drinks -= 1

	def sold_lemonade(self):
		sold = self.drinks
		print("Lemonades sold today:",sold)

	def get_lemonades(self):
		print("Lemonades available: ",self.drinks)