'''
pseudocode:
Input weight (in kg);
Input height (in m);
Calculate the BMI value using the formula: BMI = weight (in kg)/(square of height (in m));
Determine the BMI value:
if BMI < 18.5:
    print: Your BMI is [The value of calculated BMI]. You are underweight.
else if 18.5<=BMI<=30:
    print: Your BMI is [The value of calculated BMI]. You have a normal weight.
else if BMI>30:
    print: Your BMI is [The value of calculated BMI]. You are obese.
'''

weight = float(input("Your weight is (in kg):"))                #input the value of an individual's weight
height = float(input("Your height is (in m):"))                 #input the value of an individual's height
BMI = weight/(height)**2                                        #calculate the value of BMI
print(f"Your BMI is {BMI:.2f}.")                                    #output the BMI value
if BMI < 18.5:                                                  #determine the weight category
    print("You are underweight.")
elif BMI >= 18.5 and BMI <=30:
    print("You have a normal weight.")
else:
    print("You are obese.")