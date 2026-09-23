
games_file = open("games.txt", "r", encoding="utf-8")
lines_in_file = games_file.readlines()
#print(lines_in_file)
for line in lines_in_file:
    game_info= line.split("|")
    price = float(game_info[2])
    copies_sold = int(game_info[3])
    revenue = price * copies_sold
    game_name = game_info[0]
    print(f"{game_name} earned ${revenue}")
