class Supplies:

	def __init__(self):
		self.lemons = 0
		self.sugar = 0
		self.ice = 0
		self.cups = 0
		self.supplies_list = []

	def show_supplies_list(self,lemons,sugar,ice,cups):
		self.lemons += lemons
		self.sugar += sugar
		self.ice += ice
		self.cups += cups
		print("Lemons: ",self.lemons)
		print("Sugar: ",self.sugar)
		print("Ice: ",self.ice)
		print("Cups: ",self.cups)