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
	weekdays = today.get_weekday_list()
	day = 0
	while day < 7:
		cash.show_status()
		today.get_forecast()		
		vendor.show_list_buy(supplies, cash, vendor)
		cash.show_status()		
		lemonade.make_lemonade(supplies.lemons, supplies.sugar, supplies.ice, supplies.cups) 		
		vendor.set_price()
		customer.get_customers(vendor.price, cash, today.weather_score, supplies, vendor, lemonade)
		supplies.subtract_supplies(lemonade.sold_lemonade())
		cash.show_earnings()
		day += 1
		for each_day in weekdays:
			print("It's a new day! Today is {}.".format(weekdays[+1]))
			weekdays.remove(weekdays[0])
			break
	print("\nGood selling!\n")


if __name__ == "__main__":
	main()

