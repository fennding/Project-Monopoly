from Jail import *


used_numbers_cc = []
used_numbers_chance = []

def community_chest(player, canvas):
    card = generate_number(used_numbers_cc)
    if card == 1:
        CommunityChestCard1(player, canvas)
    elif card == 2:
        CommunityChestCard2(player, canvas)
    elif card == 3:
        CommunityChestCard3(player, canvas)
    elif card == 4:
        CommunityChestCard4(player, canvas)
    elif card == 5:
        CommunityChestCard5(player, canvas)
    elif card == 6:
        CommunityChestCard6(player, canvas)
    elif card == 7:
        CommunityChestCard7(player, canvas)
    elif card == 8:
        CommunityChestCard8(player, canvas)
    elif card == 9:
        CommunityChestCard9(player, canvas)
    elif card == 10:
        CommunityChestCard10(player, canvas)
    elif card == 11:
        CommunityChestCard11(player, canvas)
    elif card == 12:
        CommunityChestCard12(player, canvas)
    elif card == 13:
        CommunityChestCard13(player, canvas)
    elif card == 14:
        CommunityChestCard14(player, canvas)
    elif card == 15:
        CommunityChestCard15(player, canvas)
    elif card == 16:
        CommunityChestCard16(player, canvas)

def chance(player, canvas):
    card = generate_number(used_numbers_chance)
    if card == 1:
        ChanceCard1(player, canvas)
    elif card == 2:
        ChanceCard2(player, canvas)
    elif card == 3:
        ChanceCard3(player, canvas)
    elif card == 4:
        ChanceCard4(player, canvas)
    elif card == 5:
        ChanceCard5(player, canvas)
    elif card == 6:
        ChanceCard6(player, canvas)
    elif card == 7:
        ChanceCard7(player, canvas)
    elif card == 8:
        ChanceCard8(player, canvas)
    elif card == 9:
        ChanceCard9(player, canvas)
    elif card == 10:
        ChanceCard10(player, canvas)
    elif card == 11:
        ChanceCard11(player, canvas)
    elif card == 12:
        ChanceCard12(player, canvas)
    elif card == 13:
        ChanceCard13(player, canvas)
    elif card == 14:
        ChanceCard14(player, canvas)
    elif card == 15:
        ChanceCard15(player, canvas)
    elif card == 16:
        ChanceCard16(player, canvas)

def generate_number(used_numbers):
    all_numbers = list(range(1, 17))
    available_numbers = [number for number in all_numbers if number not in used_numbers]
    
    if not available_numbers:
        used_numbers.clear()
        available_numbers = all_numbers
    
    number = random.choice(available_numbers)
    used_numbers.append(number)
    
    return number

def CommunityChestCard1(player, canvas):
    msg = "Sie kommen aus dem Gefängnis frei! Behalten Sie diese Karte, bis Sie sie benötigen oder verkaufen."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.jail_card += 1
    waiting()
def CommunityChestCard2(player, canvas):
    msg = "Schulgeld. Zahlen Sie 50€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money -= 50
    waiting()
def CommunityChestCard3(player, canvas):
    msg = "Urlaubsgeld! Sie erhalten 100€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 100
    waiting()
def CommunityChestCard4(player, canvas):
    msg = "Ihre Lebensversicherung wird fällig. Sie erhalten 100€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 100
    waiting()
def CommunityChestCard5(player, canvas):
    msg = "Arzt-Kosten. Zahlen Sie 50€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money -= 50
    waiting()
def CommunityChestCard6(player, canvas):
    msg = "Einkommenssteuerrückerstattung. Sie erhalten 20€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 20
    waiting()
def CommunityChestCard7(player, canvas):
    msg = "Krankenhausgebühren. Zahlen Sie 100€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money -= 100
    waiting()
def CommunityChestCard8(player, canvas):
    msg = "Gehen Sie in das Gefängnis. Begeben Sie sich direkt dorthin. Gehen Sie nicht über Los. Ziehen Sie nicht 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position = 10
    player.in_jail = True
    show_player(player, canvas)
    waiting()
def CommunityChestCard9(player, canvas):
    msg = "Sie erhalten auf Vorzugs-Aktien 7% Dividende: 25€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 25
    waiting()
def CommunityChestCard10(player, canvas):
    msg = "Sie haben Geburtstag. Jeder Spieler schenkt Ihnen 10€"
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    for i in players:
        if i != player:
            i.money -= 10
            player.money += 10
    waiting()
def CommunityChestCard11(player, canvas):
    msg = "Sie erben 100€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 100
    waiting()
def CommunityChestCard12(player, canvas):
    msg = "Aus Lagerverkäufen erhalten Sie 50€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 50
    waiting()
def CommunityChestCard13(player, canvas):
    msg = "Zweiter Preis im Schönheitswettbewerb. Sie erhalten 10€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 10
    waiting()
def CommunityChestCard14(player, canvas):
    msg = "Sie werden zu Straßenausbesserungsarbeiten herangezogen. Zahlen Sie 40€ je Haus und 115€ je Hotel an die Bank."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    for i in player.properties:
        if isinstance(i, Street):
            player.money -= i.houses * 40
            player.money -= i.hotel * 115
    waiting()
def CommunityChestCard15(player, canvas):
    msg = "Rücken Sie vor bis auf Los. (Ziehe 200€ ein)."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position = 0
    player.money += 200
    show_player(player, canvas)
    waiting()
def CommunityChestCard16(player, canvas):
    msg = "Bank-Irrtum zu Ihren Gunsten. Ziehen Sie 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 200
    waiting()


def ChanceCard1(player, canvas):
    msg = "Rücken Sie vor bis zur Schlossallee."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position = 39
    waiting()
    show_player(player, canvas)
    field_check(player, 10, canvas)
def ChanceCard2(player, canvas):  
    msg = "Machen Sie einen Ausflug zum Südbahnhof. Wenn Sie über Los kommen, ziehen Sie 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    if player.position > 5:
        player.money += 200
    player.position = 5
    waiting()
    show_player(player, canvas)
    field_check(player, 10, canvas)
def ChanceCard3(player, canvas):
    msg = "Ihr Bausparvertrag wird fällig. Sie erhalten 200€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 200
    waiting()
def ChanceCard4(player, canvas):
    msg = "Rücken Sie vor bis zum Opernplatz. Wenn Sie über Los kommen, ziehen Sie 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    if player.position > 24:
        player.money += 200
    player.position = 24
    waiting()
    show_player(player, canvas)
    field_check(player,10, canvas)
def ChanceCard5(player, canvas):
    msg = "Rücken Sie vor bis zum nächsten Versorgungswerk."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    if player.position < 12:
        player.position = 12
    elif player.position < 28:
        player.position = 28
    else:
        player.position = 12
        player.money += 200
    waiting()
    show_player(player, canvas)
    field_check(player,10,canvas)
def ChanceCard6(player, canvas):
    msg = "Gehen Sie in das Gefängnis. Begeben Sie sich direkt dorthin. Gehen Sie nicht über Los. Ziehen Sie nicht 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position = 10
    player.in_jail = True
    show_player(player, canvas)
    waiting()
def ChanceCard7(player, canvas):
    msg = "Rücken Sie vor bis auf Los. (Ziehe 200€ ein)."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position = 0
    player.money += 200
    show_player(player, canvas)
    waiting()
def ChanceCard8(player, canvas):
    msg = "Die Bank zahlt Ihnen eine Dividende von 50€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 50
    waiting()
def ChanceCard9(player, canvas):
    msg = "Sie lassen Ihre Häuser renovieren. Zahlen Sie: 25€ pro Haus, 100€ pro Hotel."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    for i in player.properties:
        if isinstance(i, Street):
            player.money -= i.houses * 25
            player.money -= i.hotel * 100
    waiting()
def ChanceCard10(player, canvas):
    msg = "Sie kommen aus dem Gefängnis frei! Behalten Sie diese Karte, bis Sie sie benötigen oder verkaufen."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.jail_card += 1
    waiting()
def ChanceCard11(player, canvas):
    msg = "Rücken Sie vor bis zur Seestraße. Wenn Sie über Los kommen, ziehen Sie 200€ ein."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    if player.position > 11:
        player.money += 200
    player.position = 11
    waiting()
    show_player(player, canvas)
    field_check(player, 10, canvas)
def ChanceCard12(player, canvas):
    msg = "Sie sind zum Vorstand gewählt worden. Zahlen Sie jedem Spieler 50€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    for i in players:
        if i != player:
            i.money += 50
            player.money -= 50
    waiting()
def ChanceCard13(player, canvas):
    msg = "Ihr Bausparvertrag wird fällig. Sie erhalten 200€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money += 200
    waiting()
def ChanceCard14(player, canvas):
    msg = "Gehen Sie 3 Felder zurück."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.position -= 3
    waiting()
    show_player(player, canvas)
    field_check(player,10,canvas)
def ChanceCard15(player, canvas):
    msg = "Strafzettel! Zahlen Sie 15€."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    player.money -= 15
    waiting()
def ChanceCard16(player, canvas):
    msg = "Rücken Sie vor bis zum nächsten Verkehrsfeld."
    text_renderer = TextRenderer(canvas)
    text_renderer.render_text(msg)
    if player.position < 5:
        player.position = 5
    elif player.position < 15:
        player.position = 15
    elif player.position < 25:
        player.position = 25
    elif player.position < 35:
        player.position = 35
    else:
        player.position = 5
        player.money += 200
    waiting()
    show_player(player, canvas)
    field_check(player,10,canvas)

def field_check(player, rolled_value, canvas):
    current_field = board[player.position][0]


    if isinstance(current_field, SpecialField):
        if current_field.name == "Gemeinschaftsfeld":
            community_chest(player, canvas)
            #input("Press enter to continue")
        elif current_field.name == "Ereignisfeld":
            chance(player, canvas)
            #input("Press enter to continue")
        elif current_field.name == "GehInDasGefängnis":
            jailCheck(player, canvas)
        
    if isinstance(current_field, Property) and  current_field.owner == None:
        buy_property(player, current_field, canvas)
        
    elif isinstance(current_field, Street) and current_field.owner == player:
            building_check(current_field, player, current_field.setNumber, canvas)

    elif isinstance(current_field, Tax):
        player.money -= current_field.tax
        msg = "Du hast " + str(current_field.tax) + "€ bezahlt"
        text_renderer = TextRenderer(canvas)
        text_renderer.render_text(msg)
        waiting()

    elif current_field.owner != None and current_field.owner != player and isinstance(current_field, Property):
        if isinstance(current_field, Street):
            pay_rent_street(player, current_field, canvas)

        elif isinstance(current_field, Station):
            pay_rent_station(player, current_field, canvas)

        elif isinstance(current_field, Factory):
            pay_rent_factory(player, current_field, rolled_value, canvas)