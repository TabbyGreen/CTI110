#Tabatha Green
#4/9/2024
#PW4H2
#Looping-Salary

#calculate overtime, and gross pay
def cal_gross(pay_rate, hours_worked):
  
  reg_hours = 40
  ot_rate = 1.5

  ot_hours = max(0, hours_worked - reg_hours)
  ot_pay = ot_hours * pay_rate * ot_rate
  reg_pay = min(hours_worked, reg_hours) * pay_rate
  gross_pay = ot_pay + reg_pay

  return ot_pay, reg_pay, gross_pay

tot_ot_pay = tot_reg_pay = tot_gross_pay = num_person = 0
while True:
  person_name = input("Enter employee's name or 'done' to terminate: ")
  if person_name.lower() == "done":
    break   

  hours_worked = float(input("How many hours did employee work: "))
  pay_rate = float(input("What is employees pay rate: "))

  # Calculations salary for each employee
  ot_pay, reg_pay, gross_pay = cal_gross(pay_rate, hours_worked)

  # printing employee information
  print(f"\nEmployee Name: {person_name}")
  print ()
  print(f"Hours Worked: {hours_worked}")
  print(f"Pay Rate: ${pay_rate:.2f}") 
  print(f"Overtime Pay: ${ot_pay:.2f}")
  print(f"Regular Pay: ${reg_pay:.2f}")
  print(f"Gross Pay: ${gross_pay:.2f}")
  print ()

# Calculate for "done"
  tot_ot_pay += ot_pay
  tot_reg_pay += reg_pay
  tot_gross_pay += gross_pay
  num_person += 1

# printing summary after "done"
print ()
print(f"Total number of employees entered: {num_person}")
print(f"Total amount paid for overtime: ${tot_ot_pay:.2f}")
print(f"Total amount paid for regular hours: ${tot_reg_pay:.2f}")
print(f"Total amount paid in gross: ${tot_gross_pay:.2f}")
print ()

