#Tabatha Green
#2/28/2024
#P2LAB1
#DRIVING COSTS-VARIABLES AND EXPRESSIONS

#get interger from user
mpg = float(input("Enter miles per gallon: "))

cost = float(input("Enter cost of gas per gallon: "))

#Calculate- cost to drive distances

sum_1 = 20/mpg
miles_20 = sum_1*cost

sum_2 = 75/mpg
miles_75 = sum_2*cost

sum_3 = 500/mpg
miles_500 = sum_3*cost

#Show all data
print ("\n------Travel Expenses------")

print ("Miles per gallon: ", mpg)

print ("Cost of gas per gallon: ", cost)
print ()

print (f" Cost to drive 20 miles is {miles_20:.2f}")
print ()

print (f" Cost to drive 75 miles is {miles_75:.2f}")
print ()

print (f" Cost to drive 500 miles is {miles_500:.2f}")

       
