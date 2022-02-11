""" 
1. Game Of The Century

Background
There has been much debate over who the best team in NBA history would be if anyone could be selected from any era. Past and current NBA players voted the following players to the following teams.

Team 1
Allen Iverson: PG
Michael Jordan: SG
Kevin Durant: SF
Tim Duncan: PF
Kareem Abdul-Jabar: C

Team 2
Kyrie Irving: PG
Kobe Bryant: SG
Lebron James: SF
Dirk Nowitski: PF
Hakeem Olojuan: C

[Instructions]

Your job is to calculate the ‘Game Of The Century’
Use closures to calculate
Do NOT use 3rd party libraries or anything you need to import.

In closures.py complete the following function
    1. outerFunction will take 2 parameters
        * team1: which will be a dictionary
        * team2: which will be a dictionary
    2.innerFunction which will take 2 parameters
        * commands: which will be a list (example below of commands format)
        * finalCommand: which will be a boolean. When finalCommand is True is the ONLY time your closure should give output.
    3. formatScore which you will use as a helper function to transform your dictionaries into the final output. All formatting should be done here. It is essentially your final answer.

[Guidelines]

# Allen Iverson: AI
# Michael Jordan: MJ
# Kevin Durant: KD
# Tim Duncan: TD
# Kareem Abdul-Jabar: KAJ

# Team 2
# Kyrie Irving: KI
# Kobe Bryant: KB
# Lebron James: LJ
# Dirk Nowitski: DN
# Hakeem Olojuan: HO

We are calculating the score differently than usual. You will have to consider positive values (for made shots) and negative values (for missed shots)

The point values are as follows
# Made Layup: +2
# Missed Layup: -2
# Made Dunk: +2
# Missed Dunk: -2
# Made Free Throw: +1
# Missed Free Throw: -1
# Made Mid Range: +2
# Missed Mid Range: -2
# Made Three: +3
# Missed Three: -3
# Made AND-1: +3

The commands parameter for innerFunction will be formatted everytime like the following
    * Inputs are not necessarily guaranteed to have these exact players or exact commands
    
# Format: ['Player Name Abbreviation,Command', 'Player Name Abbreviation,Command']
# Ex: ['KAJ,Made Three', 'KI,Made Free Throw']

Two Input Dictionaries:

1. {'AI':0, 'MJ':0, 'KD':0, 'TD':0, 'KAJ':0} 
2. {'KI':0, 'KB':0, 'LJ':0, 'DN':0, 'HO':0}

[Output]

Team 1 True Score
Allen Iverson: 2 points
Michael Jordan: 13 points
Kevin Durant: 9 points
Tim Duncan: 11 points
Kareem Abdul-Jabbar: 23 points
Team 1 Leading Scorer(s): Kareem Abdul-Jabbar 23 points
Team 1 Total Score: 58 points

Team 2 True Score
Kyrie Irving: -2 points
Kobe Bryant: 2 points
Lebron James: 8 points
Dirk Nowitzki: -2 points
Hakeem Olajuwon: 10 points
Team 2 Leading Scorer(s): Hakeem Olajuwon 10 points
Team 2 Total Score: 16 points

Final Score
58 - 16

Winner
Team 1 by 42 points

Team 1 True Score
Allen Iverson: 5 points
Michael Jordan: 17 points
Kevin Durant: -5 points
Tim Duncan: -18 points
Kareem Abdul-Jabbar: 23 points
Team 1 Leading Scorer(s): Kareem Abdul-Jabbar 23 points
Team 1 Total Score: 22 points

Team 2 True Score
Kyrie Irving: 15 points
Kobe Bryant: -7 points
Lebron James: 14 points
Dirk Nowitzki: -12 points
Hakeem Olajuwon: 16 points
Team 2 Leading Scorer(s): Hakeem Olajuwon 16 points
Team 2 Total Score: 26 points

Final Score
22 - 26

Winner
Team 2 by 4 points
"""

def formatScore():
      pass

def outerFunction(team1:dict, team2:dict):
    def innerFunction(commands:list, finalCommand:bool):
        pass
