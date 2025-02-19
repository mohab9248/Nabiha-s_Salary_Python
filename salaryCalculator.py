name = str(input("Please Enter Your Name: "))

input(f"Hello {name}, Please Press Enter To Start")
salary = int(input("please Enter your Salary: "))
month = str(input("please Enter the month: "))

list = ['Savings','Rent', 'Electricity']
percentages = []

for i in list:
    inputs = input(f"Please Enter the percentage of your {i}: ")
    percentages.append(int(inputs))

for j in range(len(percentages)):
    amount = percentages[j]//100 * salary
    print(f"The amount allocated to {list[j]} is {amount}")
