#define the variables of commute time
#bus taking
a = 15                  #walk to the bus
b = 1*60+15             #bus journey
c = a+b                 #total length of time for bus commute
#driving
d = 1*60+30             #drive time
e = 5                   #walk to the car park
f = d+e                 #total length of time for driving commute
#compare between c with f
if c > f:
    print("Driving is quicker.")
elif c == f:
    print("The time for the two transport is the same.")
else:
    print("Taking bus is quicker.")

X = True
Y = False
W = X and Y
print("X: {:}".format(X))
print("Y: {:}".format(Y))
print("W (both X and Y) looks like: {:}".format(W))

'''
 Truth table for W:
X     | Y     | W
------------------------------------------------
True  | True  | True
True  | False | False
False | True  | False
False | False | False
'''