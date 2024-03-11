from DiceRoll import *

### finale Version ###

if __name__ == "__main__":
    num_players = player_config()
    
    # Fenstername und -position
    root.title("Monopoly")
    canvas.pack()

    draw_board(canvas)


    # Weiter button 
    next_button.pack(side="left", expand=True)
    # Eigentum button
    show_button = tk.Button(root, text="Eigentum", command=lambda: show_properties(canvas, players[x]))
    show_button.pack(side="left", expand=True)
    # Haus/Hotel verkaufen button 
    sell_button = tk.Button(root, text="Haus/Hotel verkaufen", command=lambda: sell_house_button(canvas, players[x]))
    sell_button.pack(side="left", expand=True)
    # Geld button 
    money_button = tk.Button(root, text="Geld", command=lambda: show_money(canvas, players[x]))
    money_button.pack(side="left", expand=True)
    # yes button
    yes_button = tk.Button(root, text="Yes", command=lambda: [answer_updater.choose_yes(), root.quit()])
    yes_button.pack(side="left", expand=True)
    # no button
    no_button = tk.Button(root, text="No", command=lambda: [answer_updater.choose_no(), root.quit()])
    no_button.pack(side="left", expand=True)
 
   
    game_over = False
    # Schleife bis das Spiel vorbei ist
    while not game_over:
        for x in range(num_players): 
            num_players_with_money = 0
            for player in players:
                if player.money > 0:
                    num_players_with_money += 1
            # Wennn nur noch ein Spieler Geld hat, ist das Spiel vorbei
            if num_players_with_money == 1:
                game_over = True
                msg = "Game over. Nur noch ein Spieler ist übrig."
                text_renderer = TextRenderer(canvas)
                text_renderer.render_text(msg)

            msg = "Du bist dran " + str(players[x].name) + ", du hast " + str(players[x].money) + "€"
            text_renderer = TextRenderer(canvas)
            text_renderer.render_text(msg)

            # Wartet auf Benutzerinteraktion
            waiting()
            
            # Spieler würfelt
            main_dice_roll(players[x], canvas)
