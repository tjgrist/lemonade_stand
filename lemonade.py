

class Lemonade:

	def __init__(self):
		self.default_recipe = 10
		self.price = 0
		self.drinks = 0
		self.pitchers = 0 


	def make_lemonade(self,lemons,sugar,ice,cups):
		glasses = int((lemons + sugar + ice)/5)
		print("Glasses of lemonade:",glasses)
		print("Cups available:",cups)
		extra_lemonade =  glasses - cups
		print("Extra lemonades:",extra_lemonade)
		self.drinks = glasses - extra_lemonade
		if glasses > cups:
			print("Number of lemonades you can make today: {}\n".format(cups))
		else: 
			print("Number of lemonades you can make today: {}\n".format(glasses))


	def subtract_drink(self):
		self.drinks -= 1


	def get_lemonades(self):
		while self.drinks > 0:
			print("\nLemonades available: ",self.drinks)
			return True
		else:
			return False


	def get_status(self):
		print("You sold out!")

	def sold_lemonade(self):
		sold = self.drinks
		print("Lemonades sold today:",sold)