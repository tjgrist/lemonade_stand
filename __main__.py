from vendor import Vendor 
from weather import Weather 
from customer import Customer 
from supplies import Supplies 

vendor = Vendor()
today = Weather()
customer = Customer()





vendor.make_supplies_list()

#game flow:
#should have a main loop through all customers
week = 0
while week < 7:
	#show weather
	print("Weather:",today.get_temp(),"and",today.get_cloudiness())
	print("weather score: ",today.weather_score)

	#buy ingredients
	vendor.buy_lemons()
	vendor.buy_sugar()
	vendor.buy_ice()
	vendor.buy_cups()
	vendor.make_supplies_list()
	#make lemonade recipe


	#sell and earn
	print("Earned: ",customer.buy(vendor.price, today.weather_score))


	bob = Customer()
	print(bob.chance)
	mary = Customer()
	print(mary.chance)
	week += 1