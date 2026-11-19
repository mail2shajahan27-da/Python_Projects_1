print('=================================')
print('         TASK MANAGER APP    ')
print('=================================')

Options = {
    1: "Add Task", 
    2: "View Tasks", 
    3: "Exit"
    }

# Selection = int(input("Select an Option :"))

for key, value in Options.items():
    print(f"{key}. {value}")

try:
    Selection = int(input("Select an Option: "))

except ValueError:
    print("Error: Please enter a valid option")

else:
    if Selection in Options:
        print(f"You have selected: {Options[Selection]}")
    else:
       print("invalid option")

