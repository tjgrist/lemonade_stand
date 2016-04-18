from random import randint

class Weather: 
	
	def __init__(self):
		self.current_weather = None
	
	def get_day(self):
		monday = 1
		tuesday = 2
		wednesay = 3
		thursday = 4
		friday = 5
		saturday = 6
		sunday = 7

	def get_temp(self):
		return randint(60,100)

	def get_cloudiness(self):
		cloudiness = randint(1,3)
		if cloudiness == 1:
			return "sunny"
		elif cloudiness == 2:
			return "overcast"
		else:
			return "rainy"




