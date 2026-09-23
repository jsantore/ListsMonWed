
games_file = open("games.txt", "r", encoding="utf-8")
lines_in_file = games_file.readlines()
#print(lines_in_file)
for line in lines_in_file:
    print(line)
    #force to top