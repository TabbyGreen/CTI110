#Tabatha Green
#3/27/2024
#P4HW1 Looping
#Get Grades

#User Input
sum1 = int(input("Enter score: "))
while sum1 < 0:
    print ("INVALID score entered!!!")
    print ("Score should be between 0 and 100")
    sum1 = int(input("Enter score: "))

sum2 = int(input("Enter score: "))
while sum2 < 0:
    print ("INVALID score entered!!!")
    print ("Score should be between 0 and 100")
    sum2 = int(input("Enter score: "))

sum3 = int(input("Enter score: ")) 
while sum3 < 0:
    print ("INVALID score entered!!!")
    print ("Score should be between 0 and 100")
    sum3 = int(input("Enter score: "))

sum4 = int(input("Enter score: "))
while sum4 < 0:
    print ("INVALID score entered!!!")
    print ("Score should be between 0 and 100")
    sum4 = int(input("Enter score: "))
    
sum5 = int(input("Enter score: "))
while sum5 < 0:
    print ("INVALID score entered!!!")
    print ("Score should be between 0 and 100")
    sum5 = int(input("Enter score: "))

#Math it out
low = min(sum1, sum2, sum3, sum4, sum5)
high = max(sum1, sum2, sum3, sum4, sum5)
total = sum1+sum2+sum3+sum4+sum5
average = total/5
#Output
print ("\n------Results------")
print (f"Lowest Grade: {low:.2f}", )
print (f"Highest Grade: {high:.2f}" )
print (" Modified List: ", sum1, sum2, sum3, sum4, sum5)
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
