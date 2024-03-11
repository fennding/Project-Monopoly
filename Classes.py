# Array für die Spieler 
players = []

# Initialisiert Attribute für Felder
class Field:
    def __init__(self, name, id, xKoord, yKoord):
        self.name = name
        self.id = id
        self.owner = None
        self.xKoord = xKoord
        self.yKoord = yKoord

# Initialisiert Attribute für Immobilien
class Property(Field):
    def __init__(self, name, id, price, color, xKoord, yKoord):
        super().__init__(name, id, xKoord, yKoord)
        self.price = price
        self.color = color
        self.owner = None
        
# Initialisiert Attribute für Straßen
class Street(Property):
    def __init__(self, name, id, price, rent, color, setNumber, xKoord, yKoord):
        super().__init__(name, id, price, color, xKoord, yKoord)
        self.houses = 0
        self.hotel = 0
        self.rent = rent
        self.setNumber = setNumber
        self.owner = None

# Initialisiert Attribute für Bahnhöfe       
class Station(Property):
    def __init__(self, name, id, price, rent, color, xKoord, yKoord):
        super().__init__(name, id, price, color, xKoord, yKoord)
        self.rent = rent
        self.owner = None

# Initialisiert Attribute für Fabriken
class Factory(Property):
    def __init__(self, name, id, price, color, xKoord, yKoord):
        super().__init__(name, id, price, color, xKoord, yKoord)
        self.owner = None

 # Initialisiert Attribute für Steuern
class Tax(Field):
    def __init__(self, name, id, tax, xKoord, yKoord):
        super().__init__(name, id, xKoord, yKoord)
        self.tax = tax
        self.owner = None

# Initialisiert Attribute für spezielle Felder
class SpecialField(Field):
    def __init__(self, name, id, xKoord, yKoord):
        super().__init__(name, id, xKoord, yKoord)
        self.owner = None

# Initialisiert Spielerattribute
class player:
    def __init__(self, number, name, color):
        self.number = number
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.jail_counter = 0
        self.jail_card = 0
        self.number_of_stations = 0
        self.number_of_factories = 0
        self.color = color 

# Schreibe den Text auf das Canvas 
class TextRenderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def render_text(self, text):
        self.canvas.delete("text") 
        self.canvas.create_text(110, 710, anchor="nw", text=text, tags="text")

# Warte auf das Drücken eines Buttons
class ButtonWaiter:
    def __init__(self, root):
        self.root = root
        self.button_pressed = False

    def wait_for_button(self, button):
        button.config(state="normal")
        button.bind("<Button-1>", self.on_button_pressed)

    def on_button_pressed(self, event):
        self.button_pressed = True
        self.root.quit()

#  Übergibt die Entscheidung des Spielers 
class AnswerUpdater:
    def __init__(self):
        self.answer = None

    def choose_yes(self):
        self.answer = "Yes"

    def choose_no(self):
        self.answer = "No"
    