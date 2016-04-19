from vendor import Vendor 
from weather import Weather 
from customer import Customer 
from money import Money 
from supplies import Supplies

vendor = Vendor()
today = Weather()
cash = Money()
supplies = Supplies()

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
		vendor.make_supplies_list(supplies)
		#show day's weather
		print("Weather:",today.get_temp(),"and",today.get_cloudiness())
		print("weather score: ",today.weather_score)

		#buy ingredients
		vendor.buy_lemons(cash,supplies)
		vendor.buy_sugar(cash,supplies)
		vendor.buy_ice(cash,supplies)
		vendor.buy_cups(cash,supplies)
		vendor.make_supplies_list(supplies)
		vendor.set_price()
		#make lemonade recipe *could worry about this later and leave default

		#sell and earn 
		#each customer's purchase should subtract ingredients and add money
		jon.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		ned.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		loris.buy(vendor.price, cash, today.weather_score,supplies, vendor)
		arya.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		denaerys.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		rob.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		dracon.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		greyworm.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		jamie.buy(vendor.price, cash, today.weather_score, supplies, vendor)
		joffrey .buy(vendor.price, cash, today.weather_score, supplies, vendor)
		reek.buy(vendor.price, cash, today.weather_score, supplies, vendor)

		print("\nLet's see how you did today.\nCash in hand:",cash.dollars)
		print("\nTotal profits: ${}\n".format(supplies.get_profits(cash.dollars)))

		week += 1

main()