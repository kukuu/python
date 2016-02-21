#A mobile phone company bills clients on a certain plan differently depending on #whether they have dialed a number containing 0845 or not. Write a program that asks #the user which number they’d like to dial and answers whether it is ‘free’ or ‘paid’. #Use mobile.py

#Write a validation to preceeed this and also imports sys. see notes

phoneNum = input("Please enter a phone number: ")
phoneNum =str(phoneNum)


while not '0845' in phoneNum:
    phoneNum = input("Hi your number is not valid. It must begin with 0845. Note, you are dialling a premium number: ")

if '0845' in phoneNum:
    print('Thanks for contacting. Wonder!')

#if  not '0845' in phoneNum :
	#print('Hi your number is not valid. It must begin with 0845. Note, you are dialling a premium number:')

