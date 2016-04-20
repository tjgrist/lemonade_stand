

class Lemonade:

	def __init__(self):
		self.default_recipe = 10
		self.price = 0
		self.drinks = 0
		self.pitchers = 0 
		self.starting_drinks = 0


	def make_lemonade(self,lemons,sugar,ice,cups):
		glasses = int((lemons + sugar + ice)/5)
		print("You have enough ingredients for {} glasses of lemonade, and you have {} cups.".format(glasses,cups))
		extra_lemonade =  glasses - cups
		self.drinks = glasses - extra_lemonade
		self.starting_drinks = self.drinks
		if glasses > cups:
			print("\nBecause you have {} cups, you can make that many lemonades today.\n".format(cups))
		else: 
			print("\nYou can make {} lemonades today.\n".format(glasses))


	def subtract_drink(self):
		self.drinks -= 1


	def get_lemonades(self):
		while self.drinks > 0:
			print("\nLemonades available to sell: ",self.drinks)
			return True
		else:
			return False


	def get_status(self):
		print("You sold out!")


	def sold_lemonade(self):
		sold = self.starting_drinks - self.drinks
		print("_______________________________________________________")
		print("\nYou sold: {} lemonades today.".format(sold))
		return sold