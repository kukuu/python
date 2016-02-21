number = input("What phone number would you like to dial? ")

number = str(number)

if not '0845' in number:
	print("You will NOT be charged for this call.")
else:
    print("You will be charged for this call.")