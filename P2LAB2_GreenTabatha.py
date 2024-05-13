#Tabatha Green
#2/28/2024
#P2LAB2
#TYPES

#get info from user
num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))



#Calculate the product

product = num1*num2*num3*num4

average = (num1+num2+num3+num4)/4

#Output with no decimals
print ("\n------Product and Average------")

print ("Number 1: ", num1)
print ("Number 2: ", num2)
print ("Number 3: ", num3)
print ("Number 4: ", num4)

print ()

print(f"The product of the numbers is {product:.0f}")
print ()
print(f"The average of the numbers is {average:.0f}")
print ()
#Output with 3 decimals

print ()
print(f"The product of the numbers is {product:.0f}")
print ()
print(f"The average of the numbers is {average:.3f}")
