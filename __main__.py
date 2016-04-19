from vendor import Vendor 
from weather import Weather 
from customer import Customer 
from money import Money 

vendor = Vendor()
today = Weather()
cash = Money()

#customers:
jon = Customer()
ned = Customer()
loris = Customer()
arya = Customer()
denaerys = Customer()
rob = Customer()
dracon = Customer()
greyworm = Customer()
jamie = Customer()
joffrey = Customer()
reek = Customer()


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
		#make lemonade recipe *could worry about this later and leave default

		#sell and earn 
		#each customer's purchase should subtract ingredients and add money
		jon.buy(vendor.price,cash,today.weather_score)
		ned.buy(vendor.price,cash,today.weather_score)
		loris.buy(vendor.price,cash,today.weather_score)
		arya.buy(vendor.price,cash,today.weather_score)
		denaerys.buy(vendor.price,cash,today.weather_score)
		rob.buy(vendor.price,cash,today.weather_score)
		dracon.buy(vendor.price,cash,today.weather_score)
		greyworm.buy(vendor.price,cash,today.weather_score)
		jamie.buy(vendor.price,cash,today.weather_score)
		joffrey .buy(vendor.price,cash,today.weather_score)
		reek.buy(vendor.price,cash,today.weather_score)

		print("\nLet's see how you did today. Cash in hand:",cash.dollars)

		week += 1

main()