def calculate_bmi(height, weight):
    # print("Height = " + str(height))
    # print("Weight = " + str(weight))

    bmi = weight / (height * height)
    result = 0

    # print("BMI is: " + str(bmi))
    if bmi < 18.5:
        # print("Under Weight")
        result = -1
    elif bmi >= 18.5 and bmi <= 25.0:
        # print("Normal Weight")
        result = 0
    else:
        # print("Over Weight")
        result = 1
    return result

print(calculate_bmi(weight=57, height=1.73))