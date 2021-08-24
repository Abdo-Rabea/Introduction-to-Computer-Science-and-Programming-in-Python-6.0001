annual_salary=float(input("Enter your annual salary: "))
k=annual_salary
total_cost=1000000
semi_annual_raise=.07
current_saving=0.0
low=0
high=10000
step=0

while abs(current_saving - .25*total_cost) >= 100:
    step+=1
    average=(low+high)/2
    annual_salary=k
    current_saving=0
    for num in range(1,37): 
        if num%6==0:
            annual_salary+=annual_salary*semi_annual_raise
        current_saving += current_saving*0.04/12 + (annual_salary/12)*average/10000.0
        
    if current_saving >.25*total_cost:
        high = average
    else:
        low = average
    if(high==low):
        print("It is not possible to pay the down payment in three years.")
        quit()

print("Best savings rate:", average/10000.0)
print("Steps in bisection search:",step)