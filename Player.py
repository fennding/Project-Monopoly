from Board import *

# Eingabe der Spieleranzahl und der Spielerdaten
def player_config():
    num_players = int(input("Gebe die Anzahl der Spieler ein (2-4): "))
    if num_players == 2 or num_players == 3 or num_players == 4:
        colors = ["blue", "red", "green", "yellow"]
        for i in range(num_players):
            name = input("Gebe den Namen des Spielers ein {}: ".format(i+1))
            color = colors[i]
            players.append(player(i+1, name, color))
        for i in range(num_players):
            print("Spieler:", players[i].name,"Farbe: ", players[i].color)
        return num_players
    else:
        print("Bitte gib eine gültige Anzahl von Spielern ein")
        return player_config()

# Aktueller Geldstand des Spielers anzeigen  
def show_money(canvas, player):
    msg = "Du hast " + str(player.money) + "€"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    return None

# Zeigt die Grundstücke des Spielers an
def show_properties(canvas, player):
    if len(player.properties) == 0:
        msg = "Du hast noch nichts gekauft"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
    elif len(player.properties) > 0:
        for i in range(len(player.properties)):
            msg = "Du hast folgende Immobilien: " + str(player.properties[i].id)+ "." + str(player.properties[i].name) + "\nDrücke Weiter"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            waiting()
        return None

# Bewegt den Spieler auf dem Spielfeld
def move_player(rolled_value, player, canvas):
    player.position=rolled_value+player.position
    if player.position >= 40:
        player.money += 200
        msg = "Du hast Start überschritten und 200€ erhalten, du hast jetzt " + str(player.money) + "€" 
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
        player.position=player.position-40
    msg = "Neue Position: " + str(board[player.position][0].name)
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    show_player(player, canvas)
    waiting()

# Immobile kaufen
def buy_property(player, property, canvas):
    msg = "Diese Straße kostet: " +  str(property.price) + "€, willst du sie kaufen?" 
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    root.mainloop()
    answer = answer_updater.answer      
    if answer == "Yes":
        if player.money >= property.price:
            player.money -= property.price
            property.owner = player
            player.properties.append(property)
            msg = "Du hast " + str(property.name) + " gekauft"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            waiting()
            if isinstance(property, Station):
                player.number_of_stations += 1
            elif isinstance(property, Factory):
                player.number_of_factories += 1
        else:
            msg = "Du hast nicht genug Geld, um diese Immobilie zu kaufen"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            waiting()   
    elif answer == "No":
        msg = "Du hast " + str(property.name) + " nicht gekauft"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()

# Miete zahlen 
def pay_rent_street(player, street, canvas):
    if street.houses == 0 and street.hotel == 0:
        rent = street.rent
    elif street.houses == 1:
        rent = street.rent * 5
    elif street.houses == 2:
        rent = street.rent * 15
    elif street.houses == 3:
        rent = street.rent * 45
    elif street.houses == 4:
        rent = street.rent * 80
    elif street.hotel == 1:
        rent = street.rent * 125
    player.money -= rent
    street.owner.money += rent
    msg = "Du hast " + str(rent) + "€ gezahlt an: " + str(street.owner.name) + ", jetzt besitzt du noch " + str(player.money) + "€"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    waiting()

# Miete für Bahnhof 
def pay_rent_station(player, current_field, canvas): 
    if current_field.owner.number_of_stations == 1:
        rent = current_field.rent
    elif current_field.owner.number_of_stations == 2:
        rent = current_field.rent * 2
    elif current_field.owner.number_of_stations == 3:
        rent = current_field.rent * 4
    elif current_field.owner.number_of_stations == 4:
        rent = current_field.rent * 8
    player.money -= rent
    current_field.owner.money += rent
    msg = "Du hast " + str(rent) + "€ gezahl an: " + str(current_field.owner.name) + ", jetzt besitzt du noch " +  str(player.money) + "€"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    waiting()

#Miete für Fabrik
def pay_rent_factory(player, factory, dice_roll_final, canvas):
    if factory.owner.number_of_factories == 1:
        rent = 4 * dice_roll_final
    elif factory.owner.number_of_factories == 2:
        rent = 10 * dice_roll_final
    player.money -= rent
    factory.owner.money += rent
    msg = "Du hast " + str(rent) + "€ gezahl an: " + str(factory.owner.name) + ", jetzt besitzt du noch " + str(player.money) + "€"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    waiting()
    



