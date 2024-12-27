#PATIENTS MANAGEMENT SYSTEM

print ("PATIENT MANAGEMENT SYSTEM")

data= []

def data_entry():
    mr = int(input("Enter MR No.: "))
    name = str(input("Enter patient name: "))
    age = int(input("Enter patient's age: "))
    weight = float(input("Enter Patient's weight in kgs: "))
    data.append ({"mr": mr, "name": name, "age": age, "weight": weight})
    print (f"The data of patient {name} has been saved.")

def data_search():
    mr = int(input("Enter MR No.: "))
    for patient in data:
        if patient["mr"] == mr:
            print (f"The details are as follow: \n" 
                   f"MR No. : {patient["mr"]} \n" 
                   f"Name: {patient["name"]} \n"
                   f"Age: {patient["age"]} yrs \n" 
                   f"Weight: {patient["weight"]}kgs \n")
            return
        else:
            print ("Record not found!")

def full_data():
    for patient in data:
        print (data)

while True:
    print ("1. Add New")
    print ("2. Search Database")
    print ("3. View Database")
    print ("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data_entry()
    elif choice == "2":
        data_search()
    elif choice == "3":
        full_data()
    elif choice == "4":
        break
    else:
        print ("Invalid Choice!")

