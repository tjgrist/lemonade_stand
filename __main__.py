from vendor import Vendor 
from weather import Weather 
from customer import Customer 

vendor = Vendor()
today = Weather()
customer = Customer()

print("temp: ",today.get_temp(),today.get_cloudiness())
print("Earned: ",customer.buy(vendor.set_price(),today.get_temp(),today.get_cloudiness()))