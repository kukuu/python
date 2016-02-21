#import sys
name = input("Please enter your name: ")
name=str(name)
gender = input("Please enter your gender. 'f' for female or 'm' for male: ")
#gender = 'f'
if gender == 'm':
    print('Hi Mr ' + name + ' we have shaving blades reduced this week')
elif gender =='f':
    print('Hi Mrs ' + name + ' we have cosmetics currently on sale')





#stopn it from skipping to address

address = input("Please enter your address: ")
address = str(address)
if address != '':
	print('Hi ' +name+  ' thanks for your address')

email = input("Please enter your email address: ")
email=str(email)

# Use split email at @ or use crude below
#while not '@' AND  not '.'  in email :


while not '@' in email:
    email = input("Please enter valid email: ")

if '@' in email:
    print('Hi ' +name+ ' thanks for sending your details:')




#elif gender and address and email:
	##print('Thank you for sending your details')
	
else:
    print ('hmmm!')


#if not email in  '@' and not email in '.':
	#print('Please enter a valid email address')

#elif email == '':
   # print('Please enter an email address')

    #exit sys










