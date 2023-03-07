'''Mini-project for practising list and dictionary comprehensions.'''
import os
import pandas
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Reading the csv file and converting the dataframe into a phonetic dictionary
alphabet_df = pandas.read_csv(PROJECT_PATH + "/nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (_, row) in alphabet_df.iterrows()}

# Asking the user for an input and creating corresponding lists of code words
text = input("Enter the text to be phonetically encoded: ").upper().split()
encodings = []

for word in text:
    code = [alphabet[letter] for letter in word if letter in alphabet]
    encodings.append(code)

# Displaying encodings on the console
print("Spell this text with the following codes:")
for code in encodings: 
    print(code)
print()
