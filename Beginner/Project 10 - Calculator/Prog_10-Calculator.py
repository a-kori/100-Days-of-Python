import operations
import resources

status_string = "Welcome to the Pythonista calculator!"
result = first_num = second_num = 0.0
calculate = {
    "+" : operations.add,
    "-" : operations.subtract, 
    "*" : operations.multiply,
    "/" : operations.divide
}
new_calculation = True

while(True):
    # Display logo and status string on a new screen
    resources.clear()
    print(resources.calculator_logo)
    print(status_string)

    # Define the first number
    if new_calculation:
        first_num = resources.collectFirstNumber()
    else: 
        first_num = result

    # Define the operation and the second number, execute calculation
    operation, second_num = resources.collectNext(calculate)
    result = calculate[operation](first_num, second_num)

    # Evaluate the result
    if type(result) != float: 
        status_string = f"{result}\nCurrent first number: {first_num}"
        result = first_num
        new_calculation = False
        continue
    else :
        print(f"\n{first_num} {operation} {second_num} = {result}")
    
    # Define the next action
    new_calculation = resources.shouldStartNewCalc(result)
    if new_calculation == True :
        status_string = ""
    elif new_calculation == False :
        status_string = f"Current first number: {result}"
    else :
        break

resources.clear()
print(resources.calculator_logo)
print("\nGoodbye!\n")