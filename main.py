from tkinter import *
import random
import pandas

window = Tk()
BACKGROUND_COLOR = "#B1DDC6"

random_choice = random.randint(0, 100)
new_random_choice = 0
wordFile = pandas.read_csv("data/french_words.csv")
french_wordList = [word for word in wordFile["French"]]
english_wordList = [word for word in wordFile["English"]]

words_to_learn = {
    "French": ["partie"],
    "English": ["part"]
}


def missed_words():
    # global words_to_learn
    text = canvas.itemcget(language_word, "text")
    result = wordFile.loc[wordFile["French"] == text, "English"]
    words_to_learn["French"].append(text)
    words_to_learn["English"].append(result.item())
    df = pandas.DataFrame.from_dict(words_to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)


def correct_words():
    text = canvas.itemcget(language_word, "text")
    if text in english_wordList:
        english_wordList.remove(text)
    elif text in french_wordList:
        french_wordList.remove(text)
    print(text)


def card_reset():
    window.after_cancel(timer)


def card_flip():
    card_reset()
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(language_word, text=english_wordList[0], fill="white")
    window.after(3000, card_flip)
    card_reset()
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(language_word, text=english_wordList[new_random_choice], fill="white")


timer = window.after(3000, card_flip)


# Generating the words.
def next_card():
    global new_random_choice
    canvas.itemconfig(language_word, text=french_wordList[random_choice])
    canvas.itemconfig(language, text="French", fill="black")
    random.seed()
    new_random_choice = random.randint(0, 101)
    canvas.itemconfig(language_word, text=french_wordList[new_random_choice], fill="black")


def missed_button_commands():
    next_card()
    missed_words()


def correct_button_commands():
    correct_words()
    next_card()


window.title("Flash Card Project")
window.config(background=BACKGROUND_COLOR)
canvas = Canvas(background=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(410, 273, image=card_front_image)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="French")
language_word = canvas.create_text(400, 273, font=("Ariel", 60, "bold"), text=french_wordList[0])
canvas.grid(column=1, row=1, padx=50, pady=50)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=correct_button_commands)
right_button.grid(column=2, row=2, padx=50, pady=50)

wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=missed_button_commands)
wrong_button.grid(column=0, row=2, padx=50, pady=50)

window.mainloop()
