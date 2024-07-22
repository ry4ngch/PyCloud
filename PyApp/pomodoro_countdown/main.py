from tkinter import *
from tkinter import simpledialog
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
REPS = 0

# ---------------------------- LAUNCH CUSTOM DIALOG ---------------------#
def set_timer():
    global WORK_MIN
    custom_work_min = simpledialog.askinteger("Custom Timer", "Set Custom Work Duration in Minutes",
                                 parent=window)
    if custom_work_min is not None:
        WORK_MIN = custom_work_min

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    # 8th times
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="Break", fg=RED)
    # 2nd, 4th, 6th time
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="Break", fg=PINK)
    # 1st time
    else:
        count_down(WORK_MIN*60)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec if count_sec >= 10 else '0'+str(count_sec)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check_mark.config(text="✔")
        else:
            check_mark.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0, bd=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
start_btn = Button(text="Start", highlightthickness=0, bd=0, highlightbackground=YELLOW, fg="black", command=start_timer)
reset_btn = Button(text="Reset", highlightthickness=0, bd=0, highlightbackground=YELLOW, fg="black", command=reset_timer)
custom_btn = Button(text="Set Custom", highlightthickness=0, bd=0, highlightbackground=YELLOW, fg="black", command=set_timer)
check_mark = Label(fg=GREEN, bg=YELLOW)

label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2, sticky="EW")
check_mark.grid(row=3, column=1)
custom_btn.grid(row=3, column=2, sticky="EW")



window.mainloop()
