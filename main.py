from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card Project")
window.config(background=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(background=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
canvas.create_image(410, 273, image=card_front_image)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="French")
language_word = canvas.create_text(400, 273, font=("Ariel", 60, "bold"), text="trouve")
canvas.grid(column=1, row=1, padx=50, pady=50)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0)
right_button.grid(column=2, row=2, padx=50, pady=50)

wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0)
wrong_button.grid(column=0, row=2, padx=50, pady=50)

window.mainloop()
