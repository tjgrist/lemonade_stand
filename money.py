class Money:

	def __init__(self):
		self.dollars = 20

	def add_money(self,dollars):
		self.dollars += dollars
		print("Cash:",self.dollars)

	def subtract_money(self,dollars):
		self.dollars -= dollars
		print("Cash:",self.dollars)
