import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

with open(PROJECT_PATH + "/Input/Letters/starting_letter.txt") as darft:
    invitation = darft.read()

with open(PROJECT_PATH + "/Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip()
        
        letter = open(PROJECT_PATH + f"/Output/ReadyToSend/letter_for_{name}.txt", "w")
        letter.write(invitation.replace("[name]", name))
        letter.close()
