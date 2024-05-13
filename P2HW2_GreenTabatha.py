#Tabatha Green
#3/8/2024
#P2HW2
#Psuedocode


sum1 = float(input("Enter grade for Module 1: "))
sum2 = float(input("Enter grade for Module 2: "))
sum3 = float(input("Enter grade for Module 3: ")) 
sum4 = float(input("Enter grade for Module 4: "))
sum5 = float(input("Enter grade for Module 5: "))
sum6 = float(input("Enter grade for Module 6: "))

low = min(sum1, sum2, sum3, sum4, sum5, sum6)
high = max(sum1, sum2, sum3, sum4, sum5, sum6)
total = sum1+sum2+sum3+sum4+sum5+sum6
average = total/6


print ("\n------Results------")
print (f"Lowest Grade: {low:.2f}", )
print (f"Highest Grade: {high:.2f}" )
print (f"Sum of Grades: {total:.2f}")
print (f"Average: {average:.2f}")
print ("--------------------")
