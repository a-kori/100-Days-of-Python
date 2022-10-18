print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

number_of_guests = int(input("How many peole will split the bill? "))
while(number_of_guests <= 0) :
    print("The number of guests should be a positive number.")
    number_of_guests = int(input("Please, re-enter, how many people will split the bill: "))

split_bill = total_bill * (1 + tip_percentage/100) / number_of_guests
print("Each person should pay: ${:.2f}".format(split_bill))