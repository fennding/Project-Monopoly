from House import *
import random

# Gefängnis
def playerInJail(player, canvas):
     if player.in_jail == True:
            player.jail_counter += 1
            # Wenn Spieler 3 mal im Gefängnis war

            # Wenn Spieler eine Gefängniskarte hat
            if player.jail_card > 0:
                msg = "Du bist im Gefängnis"
                text_renderer = TextRenderer(canvas)
                text_renderer.render_text(msg)
                msg = "Willst du deine Gefängniskarte benutzen?"
                text_renderer = TextRenderer(canvas)
                text_renderer.render_text(msg)
                root.mainloop()
                answer = answer_updater.answer      
                if answer == "Yes":
                    player.in_jail = False
                    player.jail_counter = 0
                    player.jail_card -= 1
                    msg = "Du bist raus aus dem Gefängnis"
                    text_renderer = TextRenderer(canvas)
                    text_renderer.render_text(msg)
                    waiting()
                else:
                    msg = "Du bist immer noch im Gefängnis" 
                    text_renderer = TextRenderer(canvas)
                    text_renderer.render_text(msg)
                    return playerInJailRoll(player, canvas)
            
            elif player.jail_card == 0:
                playerInJailRoll(player, canvas)
                
            if player.jail_counter == 3:
                player.in_jail = False
                player.jail_counter = 0
                msg = "Du bist raus aus dem Gefängnis"
                text_renderer = TextRenderer(canvas)
                text_renderer.render_text(msg)
                waiting()

            
                
            
# Prüft ob Spieler auf dem Gefängnisfeld ist      
def jailCheck(player, canvas): 
    if player.position == 30:
            player.position = 10
            player.in_jail = True
            msg = "Du bist im Gefängnis!"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)
            show_player(player, canvas)
            waiting()

# Würfeln um aus dem Gefängnis zu kommen
def playerInJailRoll(player, canvas):
    dice1 = random_dice_value()
    dice2 = random_dice_value()
    show_dice(dice1, dice2, canvas)
    msg = "Du bist immer noch im Gefängnis"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    waiting()

    # Wenn Pasch gewürfelt wurde, verlässt der Spieler das Gefängnis
    if dice1 == dice2:
        player.in_jail = False
        player.jail_counter = 0
        msg = "Du bist raus aus dem Gefängnis"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()



# Zufällige zwischen 1 und 6
def random_dice_value():
    return random.randint(1, 6)