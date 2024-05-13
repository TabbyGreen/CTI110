#Tabatha Green
#2/29/2023
#P2HW1
#Travel Expenses


print ("This program calculates and displays travel expenses")
print ()
budg = int(input("Enter your Budget: "))
print ()
destin = input("Enter you Travel Destination: ")
print ()
gas = float(input("How much do you think you will spend on gas? "))
print ()
hotel = float(input("Approximately, how much will you need for accodation/hotel? "))
print ()
food = float(input("Last, how much do you need for food? "))

expenses = gas+hotel+food

balance = budg-expenses

print ("\n------Travel Expeneses------")

print ("Location: ", destin)

print (f" Initial Budget: ${budg:.2f}")

print (f" Fuel: ${gas:.2f}")

print (f" Accomodation: ${hotel:.2f}")

print (f" Food: ${food:.2f}")

print ("----------------------------")

print (f" Remaining Balance: ${balance:.2f}")
