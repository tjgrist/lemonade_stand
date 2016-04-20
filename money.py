
class Money:

	def __init__(self):
		self.dollars = 25

	
	def get_earnings(self):
		print("\n...Let's see how you did today...")
		print("\nCash in hand: ${}".format(self.dollars))
		print("Total profits: ${}\n".format(self.get_profits(self.dollars)))
		print("___________________________________________________________\n")
		print("...The next day is here! Good luck.")


	def get_status(self):
		print("\nCash in hand: ${}".format(self.dollars))


	def get_profits(self,cash):
		return cash - 25


	def add_money(self,dollars):
		self.dollars += dollars


	def subtract_money(self,dollars):
		self.dollars -= dollars