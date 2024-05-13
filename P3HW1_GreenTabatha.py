#Tabatha Green
#3/15/2024
#P3HW1
#Branching

#User Input
sum1 = float(input("Enter grade for Module 1: "))
sum2 = float(input("Enter grade for Module 2: "))
sum3 = float(input("Enter grade for Module 3: ")) 
sum4 = float(input("Enter grade for Module 4: "))
sum5 = float(input("Enter grade for Module 5: "))
sum6 = float(input("Enter grade for Module 6: "))

#Math it out
low = min(sum1, sum2, sum3, sum4, sum5, sum6)
high = max(sum1, sum2, sum3, sum4, sum5, sum6)
total = sum1+sum2+sum3+sum4+sum5+sum6
average = total/6


#Output
print ("\n------Results------")
print (f"Lowest Grade: {low:.2f}", )
print (f"Highest Grade: {high:.2f}" )
print (f"Sum of Grades: {total:.2f}")
print (f"Average: {average:.2f}")
print ("--------------------")
score = int(average)
if score >= 90:
    print ("Your grade is: A")
elif 80 <= score < 89:
    print ("Your grade is: B")
elif 70 <= score < 79:
    print ("Your grade is: C")
elif 60 <= score < 69:
    print ("Your grade is: D")
else:
    print ("Your grade is: F")
