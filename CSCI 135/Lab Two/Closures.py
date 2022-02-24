Player_Dict = { 
    'AI': 'Allen Iverson', 
    'MJ': 'Michael Jordan', 
    'KD': 'Kevin Durant', 
    'TD': 'Tim Duncan', 
    'KAJ': 'Kareem Abdul-Jabbar',
    'KI': 'Kyrie Irving', 
    'KB': 'Kobe Bryant', 
    'LJ': 'Lebron James', 
    'DN': 'Dirk Nowitzki', 
    'HO': 'Hakeem Olajuwon'
}

Points = {
    "Made Layup": +2, 
    "Missed Layup": -2, 
    "Made Dunk": +2,
    "Missed Dunk": -2,
    "Made Free Throw": +1, 
    "Missed Free Throw": -1, 
    "Made Mid Range": +2,
    "Missed Mid Range": -2, 
    "Made Three": +3, 
    "Missed Three": -3, 
    "Made AND-1": +3
}

def formatScore(team1:dict, team2:dict):
    team1_score = sum(team1.values())
    team2_score = sum(team2.values())

    solution = "Team 1 True Score\n"
    for player in team1:
        solution += f"{Player_Dict[player]}: {team1[player]} points\n"
    top_score = max(team1.values())
    top_scorers = [Player_Dict[player] for player in team1 if team1[player] == top_score]
    leads = ""
    if len(top_scorers) == 1:
        leads += f"{top_scorers[0]}"
    else:
        for index, player in enumerate(top_scorers):
            if index != len(top_scorers) - 1:
                leads += f"{player},"
            else:
                leads += f"{player}"
    solution += f"Team 1 Leading Scorer(s): {leads} {top_score} points\n"
    solution += f"Team 1 Total Score: {team1_score} points\n"
    solution += f"\nTeam 2 True Score\n"
    for player in team2:
        solution += f"{Player_Dict[player]}: {team2[player]} points\n"
    top_score = max(team2.values())
    top_scorers = [Player_Dict[player] for player in team2 if team2[player] == top_score]
    leads = ""
    if len(top_scorers) == 1:
        leads += f"{top_scorers[0]}"
    else:
        for index, player in enumerate(top_scorers):
            if index != len(top_scorers) - 1:
                leads += f"{player},"
            else:
                leads += f"{player}"
    solution += f"Team 2 Leading Scorer(s): {leads} {top_score} points\n"
    solution += f"Team 2 Total Score: {team2_score} points\n\nFinal Score\n"
    solution += f"{team1_score} - {team2_score}\n\nWinner\n"
    if team1_score > team2_score:
        solution += f"Team 1 by {team1_score - team2_score} points"
    elif team1_score < team2_score:
        solution += f"Team 2 by {team2_score - team1_score} points"
    else:
        solution += f"Score is tied at {team2_score} points"
    return solution

def outerFunction(team1:dict, team2:dict):
    def innerFunction(commands:list, finalCommand:bool):
        for entry in commands:
            player, command = entry.split(",")
            if player in team1:
                team1[player] += Points[command]
            if player in team2:
                team2[player] += Points[command]
        if finalCommand:
            return formatScore(team1, team2)
        
    return innerFunction


