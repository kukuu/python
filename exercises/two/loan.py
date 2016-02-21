loan = 100
repayment = 20
interest = 10
month = 1

while loan >= 0:
	print ('Loan in month ' + str(month) + ': ' + str(loan))

	month = month + 1
	loan = (loan - repayment) + ((loan - repayment) / 100 * interest)

if loan >= 0:
	print ('Loan has been repaid.')