import os
clear = lambda: os.system('cls')

def get_value_from_user(prompt, allowed_values = []) :
    while True :
        value = input("\n" + prompt + "\n")
        if value == "" or value not in allowed_values != [] :
            print(f"'{value}' is not a acceptable answer. Try again.")
        else : 
            return value


encoder_logo = '''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 "Ybbd8"' "8bbdP"Y8  "Ybbd8"' "YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 "Ybbd8"' 88 88`YbbdP"'  88       88  "Ybbd8"' 88          
              88                                             
              88
'''