import sys
import random

warm = 20
temperature = random.randrange(5, 30)

while temperature <= warm:
	print(temperature)
	print('cold')

	run_again = input("Press a to run again.")
	if not a:
		sys.ext()
	else:
		temperature = random.randrange(5, 30)
