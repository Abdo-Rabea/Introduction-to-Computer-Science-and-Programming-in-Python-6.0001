annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))

current_saving=0.0
current_saving = current_saving*0.04/12 + (annual_salary/12)*portion_saved
months=1
while current_saving < .25*total_cost:
    months+=1
    current_saving += current_saving*0.04/12 + (annual_salary/12)*portion_saved
print("Number of months:",months)