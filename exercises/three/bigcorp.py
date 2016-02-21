#import sys
name = input("Please enter your name: ")
name=str(name)
gender = 'f'
if gender == 'm':
    print('Hi Mr ' + name + ' we have shaving blades reduced this week')
if gender =='f':
    print('Hi Mrs ' + name + ' we have cosmetics currently on sale')

address = input("Please enter your address: ")
address = str(address)
if address != '':
	print('Hi ' +name+  ' thanks for your address')

email = input("Please enter your email address: ")
email=str(email)

if   not '@' in email :
	print('Please enter valid email')
	
else:
print ('yeah')


#if not email in  '@' and not email in '.':
	#print('Please enter a valid email address')

#elif email == '':
   # print('Please enter an email address')

    #exit sys










