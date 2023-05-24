from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Project")
window.config(background=BACKGROUND_COLOR)
canvas = Canvas(background=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(410, 273, image=card_front_image)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="French")
language_word = canvas.create_text(400, 273, font=("Ariel", 60, "bold"), text="trouve")
canvas.grid(column=1, row=1, padx=50, pady=50)

random_choice = random.randint(0, 101)
wordFile = pandas.read_csv("data/french_words.csv")
french_wordList = [word for word in wordFile["French"]]
english_wordList = [word for word in wordFile["English"]]


def card_reset():
    window.after_cancel(card_timer())


def card_flip():
    card_reset()
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(language_word, text=english_wordList[random_choice], fill="white")
    card_timer()


def card_timer():
    timer = window.after(3000, card_flip)
    return timer


card_timer()


# Generating the words.
def next_card():
    canvas.itemconfig(language_word, text=french_wordList[random_choice])

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=next_card)
right_button.grid(column=2, row=2, padx=50, pady=50)

wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2, padx=50, pady=50)

window.mainloop()
