

class Lemonade:

	def __init__(self):
		self.starting_drinks = 0
		self.drinks = 0
		

	def make_lemonade(self,lemons,sugar,ice,cups):
		glasses = (lemons + sugar + ice)/5
		extra_lemonade =  glasses - cups
		self.drinks = glasses - extra_lemonade
		self.starting_drinks = self.drinks
		self.show_available_lemonades(glasses,cups)


	def show_available_lemonades(self,glasses,cups):
		print("\nYou have enough ingredients for {} glasses of lemonade, and you have {} cups.".format(glasses,cups))
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


	def show_status(self):
		print("You sold out!")


	def sold_lemonade(self):
		sold = self.starting_drinks - self.drinks
		print("_____________________________________________")
		print("\nYou sold: {} lemonades today.".format(sold))
		return sold
