import sys

def dosage_calculate(weight, strength, dose):                                       #Define the dosage calculator function
    if weight < 10 or weight > 100:
        print("Weight value invalid!\nInput the weight again!")
        sys.exit()
    if strength not in (120, 250):
        print("Strength value invalid!\nInput the strength again!")                       #Check if the inputted values are valid; If not, escape the programme
        sys.exit()
    return weight * dose / strength * 5

#Now we give an example to show how to use the function 
weight = 80
strength = 120
dose = 15                                                                           #Define the dose of drug (in mg/kg)
person_dosage = dosage_calculate(weight = weight, strength = strength, dose = dose) #Calculate the dosage for the given individual
print(f"The volumn of the drug is {person_dosage:.2f} ml.")                         #Print the result