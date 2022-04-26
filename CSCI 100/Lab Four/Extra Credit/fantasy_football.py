# Whose ready for some football?

# Open players.txt to get a list of players and positions.

# We want to build the best team of:
# 1 QB
# 2 RB
# 2 WR
# 1 TE
# 1 RB or WR or TE

Master_Roster = {
    "QB" : [],
    "QB_SCORES" : [],
    "RB" : [],
    "RB_SCORES" : [],
    "WR" : [],
    "WR_SCORES" : [],
    "TE" : [],
    "TE_SCORES" : []
}

Final_List = []


# Your code here!
with open("players.txt") as f:
    data = f.readlines()
    for i in data:
        Player_List = [i.split(" ") for i in data]


for i in Player_List:
    Position = i[0]
    Name = i[1]
    Passing_Yards_Points = int(i[2]) // 25
    Passing_TD_Points = int(i[3]) * 4
    Rushing_Yards_Points = int(i[4]) // 10
    Rushing_TD_Points = int(i[5]) * 6
    Recieving_Yards_Points = int(i[6]) // 10
    Recieving_Td_Points = int(i[7]) * 6
    Score = Passing_Yards_Points + Passing_TD_Points + Rushing_Yards_Points + Rushing_TD_Points + Recieving_Yards_Points + Recieving_Td_Points
    

    if Position == "QB":
        Master_Roster["QB"].append({"Name" : Name, "Score" : Score })
        Master_Roster["QB_SCORES"].append(Score)
    
    if Position == "RB":
        Master_Roster["RB_SCORES"].append(Score)
        Master_Roster["RB"].append({"Name" : Name, "Score" : Score })
        


    if Position == "WR":
        Master_Roster["WR"].append({"Name" : Name, "Score" : Score })
        Master_Roster["WR_SCORES"].append(Score)
    if Position == "TE":
        Master_Roster["TE"].append({"Name" : Name, "Score" : Score })
        Master_Roster["TE_SCORES"].append(Score)

    

Master_Roster["RB_SCORES"] = sorted(Master_Roster["RB_SCORES"])

Master_Roster["WR_SCORES"] = sorted(Master_Roster["WR_SCORES"])



for player in Master_Roster["QB"]:
    if max(Master_Roster["QB_SCORES"]) == player["Score"]:
        print(f"QB {player['Name']} {player['Score']}")


for player in Master_Roster["RB"]:
    if Master_Roster["RB_SCORES"][-1] == player["Score"]:
         print(f"RB1 {player['Name']} {player['Score']}")
    
for player in Master_Roster["RB"]:  
    if Master_Roster["RB_SCORES"][-2] == player["Score"]:
            print(f"RB2 {player['Name']} {player['Score']}")

for player in Master_Roster["WR"]:
    if Master_Roster["WR_SCORES"][-1] == player["Score"]:
        print(f"WR1 {player['Name']} {player['Score']}")



for player in Master_Roster["WR"]:
    if Master_Roster["WR_SCORES"][-2] == player["Score"]:
        print(f"WR2 {player['Name']} {player['Score']}")



for player in Master_Roster["TE"]:
    if max(Master_Roster["TE_SCORES"]) == player["Score"]:
         print(f"TE {player['Name']} {player['Score']}")

for player in Master_Roster["RB"]:
    if Master_Roster["RB_SCORES"][-3] == player["Score"]:
         print(f"FLEX {player['Name']} {player['Score']}")

        
