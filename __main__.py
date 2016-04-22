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
	play_time = today.get_play_duration()
	weekdays = today.get_weekday_list(play_time)
	while day < play_time:
		cash.show_status()
		today.get_forecast()		
		vendor.show_list_buy(supplies, cash, vendor)
		cash.show_status()		
		lemonade.make_lemonade(supplies.lemons, supplies.sugar, supplies.ice, supplies.cups) 		
		vendor.set_price()
		customer.get_customers(vendor.price, cash, today.weather_score, supplies, vendor, lemonade)
		supplies.subtract_supplies(lemonade.sold_lemonade())
		cash.show_earnings()
		for each_day in weekdays:
			weekdays.remove(weekdays[0])
			print("Today is {}.".format(weekdays[0]))
			break
		day += 1
	print("\nGood selling!\n")


if __name__ == "__main__":
	main()
