uk_size = input('What is your UK shoe size?')
uk_size = int(uk_size)

def is_less_than_five(x):
	return x < 5

shoe_map = {
	is_less_than_five: 'more than 5', 
	lambda x: x >5 : 'less than 5',
}

for option, outcome in shoe_map.items():
	if option(uk_size):
		print(outcome)