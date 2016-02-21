def bmi_calculate():
 
    weight, height = input("Enter weight and height seperated by a comma:")
    bmi_calculate = [(weight * 720) / (height * height)]
 
    for bmi_calculate in range (19,25):
        where = 'healthy'
        if bmi_calculate < 19:
            where = 'below'
        elif bmi_calculate > 25:
            where = 'high'
 
 
print ("your body mass index is:" , bmi_calculate)