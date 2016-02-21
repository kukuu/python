import sys

name = input("What's your name? ")
address = input("What's your address? ")
email = input("What's your email? ")

name = str(name)
address = str(address)
email = str(email)

#import pdb; pdb.set_trace()
gender = input("Please enter your gender as either m or f ")

while not ( gender == 'f' or gender == 'm'):
	gender = input("Please enter your gender as either m or f ")
	# sys.exit()
	break

if gender == 'm':
	print("Hi Mr " + name + ", we have shaving blades reduced this week")
elif gender == 'f':
	print("Hi Ms " + name + ", we have cosmetics currently on sale")


if not '@' in email:
	email = input("Please input a valid email address: ")