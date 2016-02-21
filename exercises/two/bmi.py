weight = input('What is your weight in kg?')
height = input('What is your height in m?')

weight = float(weight)
height = float(height)

bmi = weight / (height * height)
print ('Your BMI is: ' + str(bmi))

if bmi <= 15:
	print ('Very severely underweight')
elif 40 > bmi > 15:
	print ('You are in between being underweight and obese')
elif bmi >= 40:
	print ('You are obese')