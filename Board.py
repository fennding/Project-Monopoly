from GUIfunc import *

# Erstellen der einzelnen Spielfelder
Badstraße = Street("Badstraße",1, 60, 2, "brown",2,33,565)
Turmstraße = Street("Turmstraße",3, 60, 4, "brown",2,33,452)
Chausseestraße = Street("Chausseestraße",6, 100, 6, "lightblue",3,33,282)
Elisenstraße = Street("Elisenstraße",8, 100, 6, "lightblue",3,33,169)
Poststraße = Street("Poststraße",9, 120, 8, "lightblue",3,33,113)
Seestraße = Street("Seestraße",11, 140, 10, "pink",3,109,26)
Hafenstraße = Street("Hafenstraße",13, 140, 10, "pink",3,223,26)
NeueStraße = Street("Neue Straße",14, 160, 12, "pink",3,280,26)
MünchenerStraße = Street("Münchener Straße",16, 180, 14, "orange",3,394,26)
WienerStraße = Street("Wiener Straße",18, 180, 14, "orange",3,508,26)
BerlinerStraße = Street("Berliner Straße",19, 200, 16, "orange",3,565,26)
Theaterstraße = Street("Theaterstraße",21, 220, 18, "red",3,650,113)
Museumstraße = Street("Museumstraße",23, 220, 18, "red",3,650,226)
Opernplatz = Street("Opernplatz",24, 240, 20, "red",3,650,282)
Lessingstraße = Street("Lessingstraße",26, 260, 22, "yellow",3,650,395)
Schillerstraße = Street("Schillerstraße",27, 260, 22, "yellow",3,650,451)
Goethestraße = Street("Goethestraße",29, 280, 24, "yellow",3,650,564)
Rathausplatz = Street("Rathausplatz",31, 300, 26, "green",3,562,645)
Hauptstraße = Street("Hauptstraße",32, 300, 26, "green",3,506,645)
Bahnhofsstraße = Street("Bahnhofsstraße",34, 320, 28, "green",3,393,645)
Parkstraße = Street("Parkstraße",37, 350, 35, "darkblue",2,224,645)
Schlossallee = Street("Schlossallee",39, 400, 50, "darkblue",2,111,645)
Südbahnhof = Station("Südbahnhof",5, 200, 25, "black", 33, 340)
Westbahnhof = Station("Westbahnhof",10, 200, 25, "black", 337, 26)
Nordbahnhof = Station("Nordbahnhof",15, 200, 25,"black", 650, 346)
Hauptbahnhof = Station("Hauptbahnhof",20, 200, 25,"black", 339, 645)
Elektrizitätswerk = Factory("Elektrizitätswerk",12, 150,"white", 166, 26)
Wasserwerk = Factory("Wasserwerk",28, 150,"white", 650, 514)
Einkommensteuer = Tax("Einkommensteuer",4, 200, 28, 396)
Zusatzsteuer = Tax("Zusatzsteuer",38, 100, 168, 645)
Start = SpecialField("Start",0,39,645)
NurZuBesuch = SpecialField("NurZuBesuch",10,10,10)
FreiParken = SpecialField("FreiParken",20,637,45)
GehInDasGefängnis = SpecialField("GehInDasGefängnis",30,639,645)
Gemeinschaftsfeld1 = SpecialField("Gemeinschaftsfeld",2,33,508)
Gemeinschaftsfeld2 = SpecialField("Gemeinschaftsfeld",17,451,26)
Gemeinschaftsfeld3 = SpecialField("Gemeinschaftsfeld",33,453,645)
Ereignisfeld1 = SpecialField("Ereignisfeld",7,33,228)
Ereignisfeld2 = SpecialField("Ereignisfeld",22, 650, 178)
Ereignisfeld3 = SpecialField("Ereignisfeld",36, 282, 645)

# Array mit allen Spielfeldern
board=[[Start],[Badstraße],[Gemeinschaftsfeld1],[Turmstraße],[Einkommensteuer],[Südbahnhof],[Chausseestraße],[Ereignisfeld1],[Elisenstraße],[Poststraße],[NurZuBesuch],[Seestraße],[Elektrizitätswerk],[Hafenstraße],[NeueStraße],[Westbahnhof],[MünchenerStraße],[Gemeinschaftsfeld2],[WienerStraße],[BerlinerStraße],[FreiParken],[Theaterstraße],[Ereignisfeld2],[Museumstraße],[Opernplatz],[Nordbahnhof],[Lessingstraße],[Schillerstraße],[Wasserwerk],[Goethestraße],[GehInDasGefängnis],[Rathausplatz],[Hauptstraße],[Gemeinschaftsfeld3],[Bahnhofsstraße],[Hauptbahnhof],[Ereignisfeld3],[Parkstraße],[Zusatzsteuer],[Schlossallee]]

# Funktion, die den Spieler als Kreis auf dem Canvas anzeigt
def show_player(player, canvas):
    # Zuerst die aktuelle Figur des Spielers löschen
    delete_player(player.color, canvas)  
    current_field = board[player.position][0]
    # Das Oval mit der Spielerfarbe als Tag erstellen
    canvas.create_oval(current_field.xKoord, current_field.yKoord, current_field.xKoord+20, current_field.yKoord+20, fill=player.color, tags=player.color)

# Funktion zum Löschen der Figur des Spielers
def delete_player(player_color, canvas):
    # Überprüfen, ob ein Oval mit der Spielerfarbe als Tag vorhanden ist
    if canvas.find_withtag(player_color):
        canvas.delete(player_color)  # Lösche das Oval des Spielers




