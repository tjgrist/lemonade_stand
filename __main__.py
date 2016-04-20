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


def main():
	day = 0
	while day < 7:
		cash.get_status()
		
		today.get_forecast()
		
		vendor.make_supplies_list(supplies)
		vendor.buy_stuff(cash,supplies,vendor)
		vendor.make_supplies_list(supplies)

		cash.get_status()
		
		lemonade.make_lemonade(supplies.lemons,supplies.sugar,supplies.ice,supplies.cups) 
		
		vendor.set_price()

		#sell and earn:
		customer.get_customers(vendor.price, cash, today.weather_score, supplies, vendor,lemonade)

		supplies.subtract_supplies(lemonade.drinks)

		cash.get_earnings()

		day += 1

main()

#To do tmrw: make sure supply flow works well/is realistic.
#subtract lemonade "drinks" made from the day, and subtract ice.
#make it possible to buy more ingredients if you don't have enough to sell...maybe not necessary.
#make lemonade recipe *could worry about this later and leave default