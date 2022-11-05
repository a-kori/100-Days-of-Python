import time
import os
clear = lambda : os.system('cls')

logo = '''
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_| 
'''

def print_error_message(error : str, wait_time = 3):
    '''Informs the user about an error. The message is displayed for wait_time seconds (or 3 by default).'''

    clear()
    print(logo)

    print(f"{error}\n\nTry again in {wait_time} seconds.")
    time.sleep(wait_time)

def print_info_message(info : str, new_screen = True):
    '''Displays the info message on the console till the user enter any key.'''

    if new_screen:
        clear()
        print(logo)

    print("\n" + info)

def trigger_continuation():
    '''Makes the user trigger the continuation of the program themselves.'''
    input("\nEnter any key to continue. ")