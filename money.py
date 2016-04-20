

class Money:


	def __init__(self):
		self.dollars = 25

	
	def get_earnings(self):
		print("\nCash in hand: ${}".format(self.dollars))
		print("\n*TOTAL profits*: ${}\n".format(self.get_profits(self.dollars)))
		print("Good luck tomorrow.")
		print("___________________________________________________________\n")
	


	def get_status(self):
		print("\nCash in hand: ${}".format(self.dollars))


	def get_profits(self,cash):
		return cash - 25


	def add_money(self,dollars):
		self.dollars += dollars


	def subtract_money(self,dollars):
		self.dollars -= dollars