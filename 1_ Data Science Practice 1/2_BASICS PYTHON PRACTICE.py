#PATIENTS MANAGEMENT SYSTEM

print ("PATIENT MANAGEMENT SYSTEM")

data= {}

def data_entry():
    mr = int(input("Enter MR No.: "))
    name = str(input("Enter patient name: "))
    age = int(input("Enter patient's age: "))
    weight = float(input("Enter Patient's weight in kgs: "))
    data.append ({"mr": mr, "name": name, "age": age, "weight": weight})
    print (f"The data of patient {name} has been saved.")

def data_search():
    