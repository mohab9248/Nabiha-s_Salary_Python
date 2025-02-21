

input("Hello Nabiha, Please Press Enter To Start")

print("Menu:")
print("1: To add a salary and a month")
print("2: To add Savings, Rent, Electricity")
print("3: To calculate the amount allocated to savings, rent, and electricity")
print("4: To calculate the total amount spent on savings, rent, and electricity combined")
print("5: To calculate the remainder of salary after these expenses")
print("6: To calculate the yearly spent on rent and electicity")
print("7: To quit")

menu = int(input("Enter an option: "))

percentages = []

while menu != 7:
    if menu == 1:
        salary = int(input("Please Enter your Salary: "))
        name = str(input("Please Enter the month: "))
        month = {
        "name": name,
        "salary":salary
        }
        

    elif menu == 2:
        savings = ""
        rent = ""
        electicity = ""

        dict = {
            'savings': savings,
            "rent": rent,
            "electricty":electicity  
            }
        for i in dict:
            dict[i] = int(input(f"Please Enter the percentage of your {i}: "))

    elif menu == 3:
        for j in dict:
            amount = dict[j]/100 * salary
            print(f"The amount allocated to {j} is {amount}")
   
    elif menu == 4:
        for u in dict:
            totalAmount = sum(dict.values())/100 * salary
        print(f"The total amount spent on savings, rent, and electricity is {totalAmount}")
    elif menu == 5:
        remainder = salary - totalAmount
        print(f"the remainder of your salary is {remainder}")
    
    elif menu == 6:
        yearlyAmount = totalAmount * 12
        print(f"the yearly amount spent on savings, rent, and electricity is {yearlyAmount}")
    
    menu = int(input("Enter an option: "))

print("Exit")