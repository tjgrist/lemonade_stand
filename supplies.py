

class Supplies:

	def __init__(self):
		self.lemons = 0
		self.sugar = 0
		self.ice = 0
		self.cups = 0
		self.price_10 = 2
		self.price_25 = 4
		self.price_60 = 7


	def show_supplies_list(self,lemons,sugar,ice,cups):
		print("\nYou have:")
		print("Lemons: ",self.lemons)
		print("Sugar: {} cups".format(self.sugar))
		print("Ice: {} cubes".format(self.ice))
		print("Cups: ",self.cups)


	def subtract_supplies(self,lemonades_sold):
		
		self.lemons -= lemonades_sold*0.5
		self.sugar -= lemonades_sold*0.5
		self.cups -= lemonades_sold
		self.ice -= self.ice
		print("\nBut you're ice melted! Be sure to get some more.")
		
			
	def add_lemons(self,num):
		if num == 10:
			self.lemons += 10
		elif num == 25:
			self.lemons += 25
		elif num == 60:
			self.lemons += 60


	def add_sugar(self,num):
		if num == 10:
			self.sugar += 10
		elif num == 25:
			self.sugar += 25
		elif num == 60:
			self.sugar += 60


	def add_ice(self,num):
		if num == 100:
			self.ice += 100
		elif num == 250:
			self.ice += 250
		elif num == 500:
			self.ice += 500


	def add_cups(self,num):
		if num == 10:
			self.cups += 10
		elif num == 25:
			self.cups += 25
		elif num == 60:
			self.cups += 60





