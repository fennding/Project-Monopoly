import tkinter as tk
from PIL import Image, ImageTk
from Classes import *

# Fenster definieren
root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=750, bg='white')

# Erstellt eine Instanz der Klasse AnswerUpdater
answer_updater = AnswerUpdater()

# Monopoly Bild einfügen 
def draw_board(canvas):
    img = Image.open("Images/Monopoly.jpeg")
    img = img.resize((700, 700))
    monopoly_board = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor="nw", image=monopoly_board)
    canvas.monopoly_board = monopoly_board
    

# Erstellt die Würfel 
def draw_dice(x, y, value, canvas):
    canvas.create_rectangle(x, y, x+50, y+50, fill="white", outline="black", width=2)
    if value == 1:
        canvas.create_oval(x+20, y+20, x+30, y+30, fill="black")
    elif value == 2:
        canvas.create_oval(x+10, y+10, x+20, y+20, fill="black")
        canvas.create_oval(x+30, y+30, x+40, y+40, fill="black")
    elif value == 3:
        canvas.create_oval(x+10, y+10, x+20, y+20, fill="black")
        canvas.create_oval(x+20, y+20, x+30, y+30, fill="black")
        canvas.create_oval(x+30, y+30, x+40, y+40, fill="black")
    elif value == 4:
        canvas.create_oval(x+10, y+10, x+20, y+20, fill="black")
        canvas.create_oval(x+30, y+10, x+40, y+20, fill="black")
        canvas.create_oval(x+10, y+30, x+20, y+40, fill="black")
        canvas.create_oval(x+30, y+30, x+40, y+40, fill="black")
    elif value == 5:
        canvas.create_oval(x+10, y+10, x+20, y+20, fill="black")
        canvas.create_oval(x+30, y+10, x+40, y+20, fill="black")
        canvas.create_oval(x+20, y+20, x+30, y+30, fill="black")
        canvas.create_oval(x+10, y+30, x+20, y+40, fill="black")
        canvas.create_oval(x+30, y+30, x+40, y+40, fill="black")
    elif value == 6:
        canvas.create_oval(x+10, y+10, x+20, y+20, fill="black")
        canvas.create_oval(x+30, y+10, x+40, y+20, fill="black")
        canvas.create_oval(x+10, y+20, x+20, y+30, fill="black")
        canvas.create_oval(x+30, y+20, x+40, y+30, fill="black")
        canvas.create_oval(x+10, y+30, x+20, y+40, fill="black")
        canvas.create_oval(x+30, y+30, x+40, y+40, fill="black")

#  Ruft die draw_dice Funktion auf und legt die position fest 
def show_dice(dice1, dice2, canvas):
    draw_dice( 5, 700, dice1, canvas)
    draw_dice( 55, 700, dice2, canvas)

# Wartet bis der Weiter Button gedrückt wurde
def waiting():
    button_waiter = ButtonWaiter(root)
    button_waiter.wait_for_button(next_button)
    # Öffnet das Hauptfenster der GUI und hält die Programmausführung aufrecht, bis das Fenster geschlossen wird
    root.mainloop()
    if button_waiter.button_pressed:
        continue_with_code(canvas)

# Funktion für den Weiter Button
def move_on(canvas):
    # kruz warten
    canvas.after(100)

def continue_with_code(canvas):
    move_on(canvas)

# Weiter Button
next_button = tk.Button(root, text="Weiter", command=move_on(canvas))




