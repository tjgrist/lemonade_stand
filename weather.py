from random import randint

class Weather: 
	
	def __init__(self):
		self.current_weather = None
		self.day = None
		self.weather_score = 0
	

	def get_temp(self):
		temp = randint(60,100)
		self.weather_score = temp
		return temp


	def get_cloudiness(self):
		cloudiness = randint(1,3)
		if cloudiness == 1:
			self.weather_score += 20
			return "sunny"
		elif cloudiness == 2:
			self.weather_score += 10
			return "overcast"
		else:
			self.weather_score -= 15
			return "rainy"


	def get_forecast(self):
		print("\nToday's forecast:",self.get_temp(),"and",self.get_cloudiness())
		print("Weather score: ",self.weather_score)


	def get_day(self):
		for days in range(7):
			self.day = "Monday"
			print(self.day) 
			break

