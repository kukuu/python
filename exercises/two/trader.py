stock = input("How much is the stock price? ")

stock = float(stock)

if stock>0.005:
	print('buy')
elif 0.005 > stock > 0.001:
	print('hold')
else:
	print('sell')