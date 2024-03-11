from SpecialCards import *

# Würfeln
def main_dice_roll(player, canvas):
    # Prüfen ob Spieler im Gefängnis ist
    if player.in_jail == True:
        msg = "Du bist im Gefängnis"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        playerInJail(player, canvas)
        if player.in_jail == False:
            return main_dice_roll(player, canvas)
        else:
            return None
    dice1 = random_dice_value()
    dice2 = random_dice_value()
    rolled_value = dice1 + dice2
    # Würfel anzeigen, Spieler bewegen und Feld prüfen
    show_dice(dice1, dice2, canvas)
    move_player(rolled_value, player, canvas)
    field_check(player, rolled_value, canvas)
    # Prüfen ob Pasch gewürfelt wurde
    if dice1 == dice2:
        msg = "Du hast einen Pasch gewürfelt, du darfst nochmal würfeln"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()
        return main_dice_roll(player, canvas)




