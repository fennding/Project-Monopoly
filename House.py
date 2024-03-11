from Player import *

# Haus verkaufen mittels Button
def sell_house_button(canvas, player):
    show_properties(canvas, player)
    msg = "Auf welchem Grundstück möchtest du Häuser/Hotels verkaufen? (Terminal)"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    streetId = int(input("Gebe die ID des Grundstücks ein: "))
    if board[int(streetId)][0].owner == player:
        selling(streetId, player, canvas)
        waiting()
    else:
        msg = "Du bist nicht Eigentümer dieser Immobilie"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()

# Prüft ob der Spieler alle Straßen einer Farbe besitzt
def building_check(current_field, player, setNumber, canvas):
    number_of_properties = 0
    for property in player.properties:
        if property.color == current_field.color:
            number_of_properties += 1
    if number_of_properties == setNumber:
        building(current_field, player, canvas)
        show_houses(canvas, current_field)


# Haus oder Hotel bauen   
def build_house(player, street, cost, canvas):
    if street.houses == 4 and player.money >= cost:
        street.hotel += 1
        street.houses = 0
        player.money -= cost
        msg = "Du hast ein Hotel gebaut, du hast jetzt " + str(player.money) +"€"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
    elif street.houses + 1 <= 4 and player.money >= cost:
        street.houses += 1
        player.money -= cost
        msg = "Du hast ein Haus gebaut, du hast jetzt " + str(player.money) + "€"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
        building(street, player, canvas)
    else:
        msg = "Du kannst nicht so viele Häuser bauen"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        return building(street, player, canvas)

# Prüft ob ein Haus gebaut werden kann und legt den Preis fest   
def building(current_field, player, canvas):
    if current_field.hotel == 1:
        msg = "Sie haben bereits ein Hotel auf diesem Grundstück, Sie können keine weiteren Häuser bauen."
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
        return 0

    elif current_field.houses == 4:
        msg = "Sie haben bereits 4 Häuser auf diesem Grundstück, wollen Sie ein Hotel bauen?"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        root.mainloop()
        answer = answer_updater.answer
        if answer == "Yes":
            if current_field.color == "brown" or current_field.color == "lightblue":
                build_house(player, current_field, 50, canvas)
            elif current_field.color == "pink" or current_field.color == "orange":
                build_house(player, current_field, 100, canvas)
            elif current_field.color == "red" or current_field.color == "yellow":
                build_house(player, current_field, 150, canvas)
            elif current_field.color == "green" or current_field.color == "darkblue":
                build_house(player, current_field, 200, canvas)
            else:
                return 0
            show_houses(canvas, current_field)
            waiting()

    msg = "Willst du ein Haus bauen?"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    root.mainloop()
    answer = answer_updater.answer
    if answer == "Yes":
        if current_field.color == "brown" or current_field.color == "lightblue":
            build_house(player, current_field, 50, canvas)
        elif current_field.color == "pink" or current_field.color == "orange":
            build_house(player, current_field, 100, canvas)
        elif current_field.color == "red" or current_field.color == "yellow":
            build_house(player, current_field, 150, canvas)
        elif current_field.color == "green" or current_field.color == "darkblue":
            build_house(player, current_field, 200, canvas)
        else:
            waiting()
            return building(current_field, player, canvas)
    else:
        return 0


# Prüft ob ein Haus/Hotel verkauft werden kann 
def selling(streetId, player, canvas):
    street_position = board[streetId][0]
    if street_position.hotel == 1:
        msg = "Du hast ein Hotel auf diesem Grundstück, willst du ein Hotel verkaufen?"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        root.mainloop()
        answer = answer_updater.answer
        if answer == "Yes":
            if street_position.color == "brown" or street_position.color == "lightblue":
                sell_house(player, street_position, 50, canvas)
            elif street_position.color == "pink" or street_position.color == "orange":
                sell_house(player, street_position, 100, canvas)
            elif street_position.color == "red" or street_position.color == "yellow":
                sell_house(player, street_position, 150, canvas)
            elif street_position.color == "green" or street_position.color == "darkblue":
                sell_house(player, street_position, 200, canvas)
            msg = "Du hast ein Hotel verkauft, du hast jetzt " + str(player.money) + "€"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            waiting()
        elif answer == "No":
            return 0
        else:
            msg = "Bitte gib eine gültige Antwort ein, versuche es erneut"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            return selling(streetId, player)
        

    msg = "Möchtest du ein Haus verkaufen?"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    root.mainloop()
    answer = answer_updater.answer
    if answer == "Yes":
        if street_position.color == "brown" or street_position.color == "lightblue":
            sell_house(player, street_position, 50, canvas)
        elif street_position.color == "pink" or street_position.color == "orange":
            sell_house(player, street_position, 100, canvas)
        elif street_position.color == "red" or street_position.color == "yellow":
            sell_house(player, street_position, 150, canvas)
        elif street_position.color == "green" or street_position.color == "darkblue":
            sell_house(player, street_position, 200, canvas)
        msg = "Du hast ein Haus verkauft, du hast jetzt " + str(player.money) + "€"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
    elif answer == "No":
        return 0
    else:
        msg = "Bitte gib eine gültige Antwort ein, versuche es erneut"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        return selling(streetId, player)

# Verkaufen von Häusern oder Hotels  
def sell_house(player, street, cost, canvas):
    if street.hotel == 1:
        street.hotel -= 1
        street.houses = 4
        player.money += cost/2
        msg = "Du hast ein Hotel verkauft"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        delete_one_house(canvas, street, "5")
        show_houses(canvas, street)
        waiting()
        return selling(street.id, player, canvas)
    elif street.houses > 0:
        delete_one_house(canvas, street, str(street.houses))
        street.houses -= 1
        player.money += cost/2
        msg = "Du hast ein Haus verkauft"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        show_houses(canvas, street)
        waiting()
        return selling(street.id, player, canvas)
    else:
        msg = "In dieser Straße kann man keine Häuser verkaufen."
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()

# Häuser/Hotels auf dem Spielfeld anzeigen
def show_houses(canvas, field):
    if field.color == "brown" or field.color == "lightblue":
        x = field.xKoord
        y = field.yKoord
        if field.houses > 0:
            canvas.create_rectangle(x+45, y+25, x+58, y+38, fill="green", outline="black", width=1, tags= str(field.id) + "1")
        if field.houses > 1:
            canvas.create_rectangle(x+45, y+12, x+58, y+25, fill="green", outline="black", width=1, tags= str(field.id) + "2")
        if field.houses > 2:
            canvas.create_rectangle(x+45, y-1, x+58, y+12, fill="green", outline="black", width=1, tags= str(field.id) + "3")
        if field.houses > 3:
            canvas.create_rectangle(x+45, y-14, x+58, y-1, fill="green", outline="black", width=1, tags= str(field.id) + "4")
        if field.hotel == 1:
            delete_houses(canvas, field)
            canvas.create_rectangle(x+45, y+25, x+58, y+38, fill="red", outline="black", width=1, tags= str(field.id) + "5")

    elif field.color == "pink" or field.color == "orange":
        a = field.xKoord
        b = field.yKoord
        if field.houses > 0:
            canvas.create_rectangle(a-13, b+63, a, b+50, fill="green", outline="black", width=1, tags= str(field.id) + "1")
        if field.houses > 1:
            canvas.create_rectangle(a, b+63, a+13, b+50, fill="green", outline="black", width=1, tags= str(field.id) + "2")
        if field.houses > 2:
            canvas.create_rectangle(a+13, b+63, a+26, b+50, fill="green", outline="black", width=1, tags= str(field.id) + "3")
        if field.houses > 3:
            canvas.create_rectangle(a+26, b+63, a+39, b+50, fill="green", outline="black", width=1, tags= str(field.id) + "4")
        if field.hotel == 1:
            delete_houses(canvas, field)
            canvas.create_rectangle(a-13, b+63, a, b+50, fill="red", outline="black", width=1, tags= str(field.id) + "5")

    elif field.color == "red" or field.color == "yellow":
        c = field.xKoord
        d = field.yKoord
        if field.houses > 0:
            canvas.create_rectangle(c-32, d+25, c-45, d+38, fill="green", outline="black", width=1, tags= str(field.id) + "1")
        if field.houses > 1:
            canvas.create_rectangle(c-32, d+12, c-45, d+25, fill="green", outline="black", width=1, tags= str(field.id) + "2")
        if field.houses > 2:
            canvas.create_rectangle(c-32, d-1, c-45, d+12, fill="green", outline="black", width=1, tags= str(field.id) + "3")
        if field.houses > 3:
            canvas.create_rectangle(c-32, d-14, c-45, d-1, fill="green", outline="black", width=1, tags= str(field.id) + "4")
        if field.hotel == 1:
            delete_houses(canvas, field)
            canvas.create_rectangle(c-32, d+25, c-45, d+38, fill="red", outline="black", width=1, tags= str(field.id) + "5")

    elif field.color == "green" or field.color == "darkblue":
        e = field.xKoord
        f = field.yKoord
        if field.houses > 0:
            canvas.create_rectangle(e-13, f-40, e, f-27, fill="green", outline="black", width=1, tags= str(field.id) + "1")
        if field.houses > 1:
            canvas.create_rectangle(e, f-40, e+13, f-27, fill="green", outline="black", width=1, tags= str(field.id) + "2")
        if field.houses > 2:
            canvas.create_rectangle(e+13, f-40, e+26, f-27, fill="green", outline="black", width=1, tags= str(field.id) + "3")
        if field.houses > 3:
            canvas.create_rectangle(e+26, f-40, e+39, f-27, fill="green", outline="black", width=1, tags= str(field.id) + "4")
        if field.hotel == 1:
            delete_houses(canvas, field)
            canvas.create_rectangle(e-13, f-40, e, f-27, fill="red", outline="black", width=1, tags= str(field.id) + "5")

# Löscht die Häuser/Hotels auf dem Spielfeld


def delete_one_house(canvas, field, number):
    canvas.delete(str(field.id) + number)

def delete_houses(canvas, field):
    canvas.delete(str(field.id) + "1")
    canvas.delete(str(field.id) + "2")
    canvas.delete(str(field.id) + "3")
    canvas.delete(str(field.id) + "4")
