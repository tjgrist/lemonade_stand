from vendor import Vendor 
from weather import Weather 
from customer import Customer 
from money import Money 

vendor = Vendor()
today = Weather()
bob = Customer()
cash = Money()





#game flow:
#should have a main loop through all customers
def main():
	week = 0
	while week < 7:
		#show supplies
		vendor.make_supplies_list()
		#show day's weather
		print("Weather:",today.get_temp(),"and",today.get_cloudiness())
		print("weather score: ",today.weather_score)

		#buy ingredients
		vendor.buy_lemons()
		vendor.buy_sugar()
		vendor.buy_ice()
		vendor.buy_cups()
		vendor.make_supplies_list()
		vendor.set_price()
		#make lemonade recipe


		#sell and earn 
		#each customer's purchase should subtract ingredients and add money
		print("Earned: ",bob.buy(vendor.price, cash, today.weather_score))



		print(bob.chance)
		mary = Customer()
		print(mary.chance)
		week += 1

main()