#Tabatha Green
#3/27/2024
#P4LAB2
#Output Range with increment of 5

var1 = int(input("Enter the smallest integer: "))
var2 = int(input("Enter the largest integer: "))

while var1 >= var2:
    print ("Second integer can't be less than the first.")
    var1 = int(input("Enter the smallest integer: "))
    var2 = int(input("Enter the largest integer: "))

for var in range (var1, var2+1, 5):
    print (var)
