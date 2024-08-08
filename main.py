from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = ""
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global marks
    global reps
    window.after_cancel(timer)
    title["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title["text"] = "LONG BREAK"
        count_down(LONG_BREAK_MIN)
    if reps % 2 == 0:
        title["text"] = "SHORT BREAK"
        count_down(SHORT_BREAK_MIN)
    else:
        title["text"] = "WORK"
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 60:
        seconds = 00
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks

        if reps % 2 == 0:
            marks += "✔"

        marker["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# elements
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
marker = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))

start_button = Button(text="Start", padx=5, pady=5, highlightthickness=0, command=start_timer)
stop_button = Button(text="Reset", padx=5, pady=5, highlightthickness=0, command=reset_timer)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# positioning elements
title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
stop_button.grid(row=2, column=2)
marker.grid(row=3, column=1)

# call functions


window.mainloop()
