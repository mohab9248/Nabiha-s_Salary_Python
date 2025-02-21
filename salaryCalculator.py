

input(f"Hello Nabiha, Please Press Enter To Start")

salary = int(input("Please Enter your Salary: "))
name = str(input("Please Enter the month: "))
list = []

month = {
    "name": name,
    "salary":salary
}

list.append(month)
percentages = []

for i in list:
    inputs = input(f"Please Enter the percentage of your {i}: ")
    percentages.append(int(inputs))

for j in range(len(percentages)):
    amount = percentages[j]/100 * salary
    print(f"The amount allocated to {list[j]} is {amount}")

for u in range(len(percentages)):
    totalAmount = sum(percentages)/100 * salary
    print(f"The total amount spent on savings, rent, and electricity is {totalAmount}")

remainder = salary - totalAmount
print(f"the remainder of your salary is {remainder}")

yearlyAmount = totalAmount * 12
print(f"the yearly amount spent on savings, rent, and electricity is {yearlyAmount}")