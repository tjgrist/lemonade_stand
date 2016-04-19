from vendor import Vendor 
from weather import Weather 
from customer import Customer 
from money import Money 
from supplies import Supplies
from lemonade import Lemonade 

vendor = Vendor()
today = Weather()
cash = Money()
supplies = Supplies()
lemonade = Lemonade()

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
	day = 0
	while day < 7:
		#show supplies
		vendor.make_supplies_list(supplies)
		#show day's weather
		print("\nToday's forecast:",today.get_temp(),"and",today.get_cloudiness())
		print("weather score: ",today.weather_score)

		#buy ingredients -- make this one function vendor.buy_stuff(cash,supplies)
		#vendor.buy_stuff(cash,supplies,vendor)
		vendor.buy_lemons(cash,supplies)
		vendor.buy_sugar(cash,supplies)
		vendor.buy_ice(cash,supplies)
		vendor.buy_cups(cash,supplies)

		vendor.make_supplies_list(supplies)
		
		lemonade.make_lemonade(supplies.lemons,supplies.sugar,supplies.ice,supplies.cups)#How much lemonade I can make 
		
		# while supplies.check_supplies():
		# 	break
		# else: vendor.buy_stuff(cash,supplies)
		vendor.set_price()

		#make lemonade recipe *could worry about this later and leave default

		#sell and earn 
		#make this a customer flow function
		jon.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		ned.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		loris.buy(vendor.price, cash, today.weather_score,supplies, vendor,lemonade)
		arya.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		denaerys.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		rob.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		dracon.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		greyworm.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		jamie.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		joffrey .buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)
		reek.buy(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)

		
		supplies.subtract_supplies(lemonade.drinks)

		print("\nLet's see how you did today.\nCash in hand: ${}".format(cash.dollars))
		print("\nTotal profits: ${}\n".format(supplies.get_profits(cash.dollars)))

		day += 1

main()

#To do tmrw: make sure supply flow works well/is realistic.
#subtract lemonade "drinks" made from the day, and subtract ice.f