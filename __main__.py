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
customer = Customer()

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
		vendor.make_supplies_list(supplies)
		print("\nToday's forecast:",today.get_temp(),"and",today.get_cloudiness())
		print("Weather score: ",today.weather_score)

		vendor.buy_stuff(cash,supplies,vendor)
		vendor.make_supplies_list(supplies)
		
		lemonade.make_lemonade(supplies.lemons,supplies.sugar,supplies.ice,supplies.cups)#How much lemonade I can make 
		
		# while supplies.check_supplies():
		# 	break
		# else: vendor.buy_stuff(cash,supplies)
		vendor.set_price()

		#make lemonade recipe *could worry about this later and leave default

		#sell and earn 
		#make this a customer flow function

		customer.get_customers(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)

		
		supplies.subtract_supplies(lemonade.drinks)

		print("\nLet's see how you did today.\nCash in hand: ${}".format(cash.dollars))
		print("\nTotal profits: ${}\n".format(supplies.get_profits(cash.dollars)))

		day += 1

main()

#To do tmrw: make sure supply flow works well/is realistic.
#subtract lemonade "drinks" made from the day, and subtract ice.
#make it possible to buy more ingredients if you don't have enough to sell... -- maybe not necessary.