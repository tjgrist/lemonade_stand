from random import randint

class Weather: 
	
	def __init__(self):
		self.current_weather = None
	
	def get_day(self):
		mon = 1
		tues = 2
		wed = 3
		thur = 4
		fri = 5
		sat = 6
		sun = 7

	def get_temp(self):
		return randint(60,100)

	def get_cloudiness(self):
		cloudiness = randint(1,3)
		if cloudiness == 1:
			print("It's sunny.")
			return "sunny"
		elif cloudiness == 2:
			print("It's overcast.")
			return "overcast"
		else:
			print("It's rainy")
			return "rainy"



today = Weather()




