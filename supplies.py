class Supplies:

	def __init__(self):
		self.lemons = 0
		self.sugar = 0
		self.ice = 0
		self.cups = 0

	def show_supplies_list(self,lemons,sugar,ice,cups):
		print("\nYou have:")
		print("Lemons: ",self.lemons)
		print("Sugar: ",self.sugar)
		print("Ice: ",self.ice)
		print("Cups: ",self.cups)

	def check_supplies(self):
		if self.lemons > 0 and self.sugar > 0 and self.ice > 0 and self.cups > 0:
			return True
		else:
			print("You don't have enough ingredients!")
			return False

	def get_profits(self,cash):
		return cash - 20

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

