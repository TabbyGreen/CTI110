#Tabatha Green
#2/16/2024
#P1HW2
#Learning Python

#get interger from user
budg = int(input("Enter your Budget: "))

destin = input("Enter you Travel Destination: ")

gas = float(input("How much do you think you will spend on gas?"))

hotel = float(input("Approximately, how much will you need for accodation/hotel?"))

food = float(input("Last, how much do you need for food?"))

expenses = gas+hotel+food

balance = budg-expenses


print ("\n------Travel Expeneses------")

print ("Location: ", destin)

print ("Initial Budget: ", budg)

print ("Fuel:", gas)
print ("Accomodation:", hotel)
print ("Food:", food)

print ("Remaining Balance:", balance)
