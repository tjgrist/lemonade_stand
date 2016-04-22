

class Vendor:

	def __init__(self):
		self.recipe = 0
		self.price = 0


	def buy_supplies(self,cash,supplies):
		print("\nYou need some things!")
		for each in ["lemons","sugar","cups","ice"]:
			print("\nBuy some {}! You can buy 10 sets @ $2, 25 @ $4, or 60 @ $7.".format(each))
			quantity = input("Enter how many {} you need: ".format(each))
			try:
				quantity = int(quantity)
				if quantity <= 10: 
					cash.subtract_money(supplies.price_10)
					supplies.add_item(quantity,each)
				elif quantity <= 25:
					cash.subtract_money(supplies.price_25)
					supplies.add_item(quantity,each)
				elif quantity <= 60:
					cash.subtract_money(supplies.price_60)
					supplies.add_item(quantity,each)
			except:
				print("\nOops. Try entering a numeric value.")
				supplies.subtract_all_supplies()
				return self.buy_supplies(cash,supplies)


	def set_price(self):
		print("You can set your price anywhere from $1-4")
		price = input("What shall the price be today? $")
		try: 
			price = float(price)
			self.price = price
		except:
			print("Try entering a numeric value.")
			self.set_price()
		
	
	def show_list_buy(self,supplies,cash,vendor):
		supplies.show_supplies_list()
		self.buy_supplies(cash,supplies)
		supplies.show_supplies_list()

		
