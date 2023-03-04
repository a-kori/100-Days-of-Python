import os

# Save the project's absolute path as PROJECT_PATH
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Read the invitation draft from starting_letter.txt
with open(PROJECT_PATH + "/Input/Letters/starting_letter.txt") as darft:
    invitation = darft.read()

# For each name in invited_names.txt, create a new file and write
# the invitation in it, replacing [name] with each name accordingly
with open(PROJECT_PATH + "/Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip()
        
        letter = open(PROJECT_PATH + f"/Output/ReadyToSend/letter_for_{name}.txt", "w")
        letter.write(invitation.replace("[name]", name))
        letter.close()
