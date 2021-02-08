from tkinter import *

# --------------------------- CONSTANTS --------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # Total minutes
SHORT_BREAK_MIN = 5  # Total minutes
LONG_BREAK_MIN = 20  # Total minutes
reps = 0
timer = None

# --------------------------- TIMER RESET --------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(count_timer, text=f"{WORK_MIN}:00")
    global reps
    reps = 0

# --------------------------- TIMER MECHANISM --------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60  # minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # minutes to seconds

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# --------------------------- BRING WINDOW TO TOP --------------------------- #

def window_to_top():
    window.attributes("-topmost", 1)
    window.attributes("-topmost", 0)

# --------------------------- COUNTDOWN MECHANISM --------------------------- #

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(count_timer, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        window_to_top()
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"
        check_marks.config(text=marks)

# --------------------------- UI SETUP --------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
    font=(FONT_NAME, 45, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="support_files\\tomato.png")
canvas.create_image(102, 112, image=tomato_img)
count_timer = canvas.create_text(102, 140, text=f"{WORK_MIN}:00",
    fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", bg=YELLOW, font=(None,10,"bold"),
    highlightthickness=0, padx=10, pady=5, command=start_timer)
start_button.grid(row=3, column=0, pady=10)
reset_button = Button(text="Reset", bg=YELLOW, font=(None,10,"bold"),
    highlightthickness=0, padx=10, pady=5, command=reset_timer)
reset_button.grid(row=3, column=2, pady=10)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(15))
check_marks.grid(row=4, column=1, pady=10)

window.mainloop()
