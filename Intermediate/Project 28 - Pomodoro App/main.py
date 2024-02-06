from tkinter import *
import os, math, time

IMAGE_PATH = os.path.dirname(os.path.abspath(__file__)) + r"\tomato.png"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#808080"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

def start():
    '''Launches a focus period or a break with predefined duration depending on the current 
    value of the repetition counter and/or updates the headline, step counter and timer/checkmarks. '''
    global reps

    # Disable start button during session
    start_button["state"] = "disabled"

    # Adjust headline and timer / checkmarks
    if reps == 8:
        headline.config(text="Done!")
        steps.config(text="")
        checkmarks.config(text=checkmarks.cget("text") + "✔")
        return
    
    steps.config(text=f"Step {reps + 1}/8")
    if reps % 2 == 0:
        headline.config(text="Focus", fg=GREEN)
        canvas.itemconfig(timer_label, text="{:02d}".format(WORK_MIN) + ":00")
        count_down(WORK_MIN)
    elif reps == 7:
        headline.config(text="Break", fg=RED)
        canvas.itemconfig(timer_label, text="{:02d}".format(LONG_BREAK_MIN) + ":00")
        count_down(LONG_BREAK_MIN)
    else:
        headline.config(text="Break", fg=PINK)
        canvas.itemconfig(timer_label, text="{:02d}".format(SHORT_BREAK_MIN) + ":00")
        count_down(SHORT_BREAK_MIN)


def count_down(count_secs: int):
    '''Converts given number of seconds into the minutes:seconds format and starts the countdown in the timer.
    On completion, updates the repetition counter and calls start to continue.'''
    global reps, timer
    
    # Change the timer
    minutes = "{:02d}".format(math.floor(count_secs / 60))
    seconds = "{:02d}".format(count_secs % 60)
    canvas.itemconfig(timer_label, text=f"{minutes}:{seconds}")

    # Count down or increase repetition counter
    if count_secs > 0:
        timer = window.after(1000, count_down, count_secs - 1)
        reset_button["state"] = "normal"
    else:
        reps += 1
        start()


def reset():
    '''Sends a stop signal to running countdown function, resets the 
    repetition counter, headline and timer, enables the start button.'''
    global reps, timer
    window.after_cancel(timer)

    reps = 0
    start_button["state"] = "normal"
    headline.config(text="Focus", fg=GREEN)
    steps.config(text="Step 1/8")
    canvas.itemconfig(timer_label, text="{:02d}".format(WORK_MIN) + ":00")


# Configure window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Add headline
headline = Label(text="Focus", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold"))
headline.grid(column=1, row=0)

# Add image and timer label
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=IMAGE_PATH) # to prevent garbage collection
canvas.create_image(100, 112, image=img)
timer_label = canvas.create_text(100, 130, 
                           text="{:02d}".format(WORK_MIN) + ":00", 
                           fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add step counter
steps = Label(text="Step 1/8", fg=GREY, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
steps.config(padx=50, pady=10)
steps.grid(column=1, row=3)

# Add checkmarks
checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmarks.config(padx=50, pady=10)
checkmarks.grid(column=1, row=4)

# Add buttons
start_button = Button(text="Start", 
                      font=(FONT_NAME, 10, "bold"), 
                      highlightthickness=0, 
                      command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", state="disabled",
                      font=(FONT_NAME, 10, "bold"), 
                      highlightthickness=0, 
                      command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
