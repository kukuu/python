
#A loan repayment plan consists of a balance and monthly interest and repayments.

#The loan amount in question is £100. Repayments are made at £20. Interest is charged monthly at %10.

#Write a program that prints to screen the remaining balance after every month.

import random
loan = 100
repayment = 20
interest=1.1

while loan >= 0:
    loan =(loan-repayment)*interest
print("loan has been paid of")


