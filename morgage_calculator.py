
initial_house_value = 1000000
house_value = initial_house_value
down_payment = initial_house_value * 0.2
principle = initial_house_value - down_payment

delimiter = '\t'
print('year' 
	+ delimiter + 'payment' 
	+ delimiter + 'contributed_to_principle' 
	+ delimiter + 'principle' 
	+ delimiter + 'total_out_of_pocket' 
	+ delimiter + 'house_value'
	+ delimiter + 'profit')

for x in range(30):
	year = x+1

	# Assume every cost is increased by 3% per year.
	insurance = initial_house_value * 0.0022 * 1.03
	property_tax = initial_house_value * 0.012 * 1.03
	hoa = 350 * 12 * 1.03
	# Interest set to 3%
	interest = principle * 0.03

	# Monthly payment times 12 months.
	payment = 4965*12
	contributed_to_principle = payment - insurance - property_tax - hoa - interest
	# Prinicple means the remaining of the principle. 
	principle = principle - contributed_to_principle

	total_out_of_pocket = 200000 + payment*year + principle
	# Assume house value is increased by 5% every year.
	house_value = house_value * 1.05

	# Selling fee is also 5%, 2.5 for seller agent and 2.5 for buyer agent.
	profit = house_value*0.95 - total_out_of_pocket

	print(str(year) 
		+ delimiter + str(payment) 
		+ delimiter + str(contributed_to_principle) 
		+ delimiter + str(principle) 
		+ delimiter + str(total_out_of_pocket) 
		+ delimiter +str(house_value)
		+ delimiter +str(profit))
