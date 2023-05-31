from tkinter import *
import random
import pandas

try:
    wordFile = pandas.read_csv("data/words_to_learn.csv", index_col=False)
except FileNotFoundError:
    wordFile = pandas.read_csv("data/french_words.csv", index_col=False)



window = Tk()
BACKGROUND_COLOR = "#B1DDC6"

print(wordFile)
try:
    random_choice = (random.randint(0, len(wordFile) - 1))
except ValueError:
    wordFile = pandas.read_csv("data/french_words.csv", index_col=False)

new_random_choice = 0
words_to_learn = {
    "French": [],
    "English": []
}


# def missed_words():
#     text = canvas.itemcget(language_word, "text")
#     result = wordFile.loc[wordFile["French"] == text, "English"]
#     words_to_learn["French"].append(text)
#     words_to_learn["English"].append(''.join(result))
#     print(words_to_learn["English"], words_to_learn["French"])
#     df = pandas.DataFrame.from_dict(words_to_learn)
#     df.to_csv("data/words_to_learn.csv", index=False)


def correct_words():
    global wordFile
    text = canvas.itemcget(language_word, "text")

    # Check if text is present in the 'French' column
    if text in wordFile["French"].tolist():
        wordFile = wordFile[wordFile['French'] != text]  # Remove rows where 'French' column matches the text
        # print(wordFile)
    # Check if text is present in the 'English' column
    elif text in wordFile["English"].tolist():
        wordFile = wordFile[wordFile['English'] != text]  # Remove rows where 'English' column matches the text
        # print(wordFile)
    else:
        return

    wordFile.to_csv("data/words_to_learn.csv", index=False)


def card_reset():
    window.after_cancel(timer)


def card_flip():
    card_reset()
    english_wordList = wordFile["English"].tolist()
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")

    if len(english_wordList) > 0:
        try:
            canvas.itemconfig(language_word, text=english_wordList[0], fill="white")
        except IndexError:
            canvas.itemconfig(language_word, text="You've learnt all the words", fill="white", font=("Ariel", 20, "bold"))
    else:
        canvas.itemconfig(language_word, text="You've learnt all the words", fill="white", font=("Ariel", 20, "bold"))

    window.after(3000, card_flip)


timer = window.after(3000, card_flip)


# Generating the words.
def next_card():
    global new_random_choice
    french_wordList = [word for word in wordFile["French"]]
    canvas.itemconfig(language, text="French", fill="black")

    # Generate a new random choice within the valid range
    try:
        new_random_choice = random.randint(0, len(french_wordList) - 1)
        canvas.itemconfig(language_word, text=french_wordList[new_random_choice], fill="black")

    except IndexError:
        canvas.itemconfig(language_word, text="Tu as appris tous les mots", fill="black",font=("Ariel",20,"bold"))

    except ValueError:
        canvas.itemconfig(language_word, text="Tu as appris tous les mots", fill="black",font=("Ariel",20,"bold"))



def missed_button_commands():
    next_card()
    # missed_words()


def correct_button_commands():
    # correct_words()
    correct_words()
    next_card()


window.title("Flash Card Project")
window.config(background=BACKGROUND_COLOR)

canvas = Canvas(background=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
canvas.grid(column=1, row=1, padx=50, pady=50)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(410, 273, image=card_front_image)

language = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
try:
    language_word = canvas.create_text(400, 273, font=("Arial", 60, "bold"), text=wordFile["French"][0])
except IndexError:
    language_word = canvas.create_text(400, 273, font=("Arial", 20, "bold"), text="Tu as appris tous les mots",)
except ValueError:
    language_word = canvas.create_text(400, 273, font=("Arial", 20, "bold"), text="Tu as appris tous les mots",)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=correct_button_commands)
right_button.grid(column=2, row=2, padx=50, pady=50)

wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=missed_button_commands)
wrong_button.grid(column=0, row=2, padx=50, pady=50)

window.mainloop()
