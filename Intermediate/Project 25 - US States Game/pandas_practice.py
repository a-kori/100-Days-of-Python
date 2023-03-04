'''Another Pandas challenge from Day 25 of 100 Days of Code.'''
import os
import pandas
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Creating a dataframe from the squirrel_data.csv file
data = pandas.read_csv(PROJECT_PATH + "/squirrel_data.csv")

# Counting the number of grey, red and black squirrels
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Saving the calculation results in a dictionary and converting it to a csv file
squirrel_counts = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}
pandas.DataFrame(squirrel_counts).to_csv(PROJECT_PATH + "/squirrel_data_simplified.csv")
