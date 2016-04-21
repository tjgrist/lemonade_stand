

class Supplies:

	def __init__(self):
		self.lemons = 0
		self.sugar = 0
		self.ice = 0
		self.cups = 0
		self.price_10 = 2
		self.price_25 = 4
		self.price_60 = 7


	def show_supplies_list(self):
		print("\nYou have:")
		print("Lemons: ",self.lemons)
		print("Sugar: {} cups".format(self.sugar))
		print("Cups: ",self.cups)
		print("Ice: {} cubes".format(self.ice))
		

	def subtract_supplies(self,lemonades_sold):
		self.lemons -= lemonades_sold*0.4
		self.sugar -= lemonades_sold*0.4
		self.cups -= lemonades_sold
		self.ice -= self.ice
		print("\nBut you're ice melted! Be sure to get some more.")


	def add_item(self,num,item):
		if num <= 10:
			if item == "lemons":
				self.lemons += num
			if item == "sugar":
				self.sugar += num
			if item == "cups":
				self.cups += num
			if item <= "ice":
				self.ice += num*10	
		elif num <= 25:
			if item == "lemons":
				self.lemons += num
			if item == "sugar":
				self.sugar += num
			if item == "cups":
				self.cups += num
			if item <= "ice":
				self.ice += num*10
		elif num <= 60:
			if item == "lemons":
				self.lemons += num
			if item == "sugar":
				self.sugar += num
			if item == "cups":
				self.cups += num
			if item <= "ice":
				self.ice += num*10
