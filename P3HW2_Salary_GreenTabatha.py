#Tabatha Green
#3/20/2024
#P3HW2
#Salary

#get info from user
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

#calculate
# Overtime
if hours > 40:
    over_time = (hours-40)
    reg_hour = (40)
    ot_pay =((over_time)*(1.5*rate))
    reg_pay =(hours*rate)
    gross =(ot_pay) + (reg_pay)

elif hours <= 40:
    over_time = (0)
    reg_hour = hours
    ot_pay = (0)
    reg_pay =(hours*rate)
    gross =(reg_pay)


#Print with formatting
print ("\n--------------------")

print ("Employee name: ", name)
print ()
print ("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay  Gross Pay")
print ("\n---------------------------------------------------------------------------")
print ()
print (f'{hours: <14.2f} {rate: <10.2f} {over_time: <13.2f} {ot_pay: <15.2f} {reg_hour: <12.2f} {gross: <9.2f}')
