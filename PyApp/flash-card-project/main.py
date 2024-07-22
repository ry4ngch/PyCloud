from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(float(canvas['width'])/2, float(canvas['height'])/2, image=card_front_img)
card_title = canvas.create_text(float(canvas['width'])/2, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(float(canvas['width'])/2, float(canvas['height'])/2, text="word", font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, bd=0, highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, bd=0, highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, command=is_known)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
