from random import randint


class Weather: 
	
	def __init__(self):
		self.weather_score = 0
	

	def get_temp(self):
		temp = randint(60,100)
		self.weather_score += temp
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


	def get_weekday_list(self,days):
		weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]*days
		return weekdays


	def get_play_duration(self):
		play_time = input("For how many weeks would you like to play? ")
		try:
			int(play_time)
			return int(play_time)*7
		except: 
			return self.get_play_duration()