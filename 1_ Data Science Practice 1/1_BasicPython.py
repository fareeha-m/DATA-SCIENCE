print ("The Calculator for Pediatric dose of Paracetamol")
print()

dose = 5 #mg/kg/dose
weight = float(input("Enter the weight in kilograms of your patient: ")) #float for weight in decimals

cal = dose*weight

print (f"The dose of your patient having weigh {weight}kg(s) is {cal}mg/dose")

