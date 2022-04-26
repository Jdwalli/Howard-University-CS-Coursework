#Extra Credit Included
# Who wants to be a Millionaire??

# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000 
# 5 answers correct: $50000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000

# Your code here!

import random

def award_prize(qc):
    if qc == 1:
        return 500
    if qc == 2:
        return 1000
    if qc == 3:
        return 5000
    if qc == 4:
        return 20000
    if qc == 5:
        return 50000
    if qc == 6:
        return 250000
    if qc == 7:
        return 500000
    if qc == 8:
        return 1000000
        

Millionaire_Questions = {
    "Q1" : {
        "Question" : 'What does the acronym "smh" stand for?\na. Shaking my head\nb. Shaking my hands\nc. Shaking my heart\nd. Shaqs money hands',
        "Answer" : "a"
    },
    
    "Q2" : {
        "Question" : 'Which Avenger other than Captain America was able to pick up Thor’s Mjolnir in the Marvel movies?\na. Ronin\nb. Captain America\nc. Vision\nd. Groot',
        "Answer" : "c"
    },
    
    "Q3" : {
        "Question" : 'What day is Star Wars Day?\na. Leptember 192nd\nb. January 25th\nc. April 1st\nd. May 4th',
        "Answer" : "d"
    },
    
    "Q4" : {
        "Question" : 'Who was the highest-paid actress of 2019, according to Forbes?\na. Joshua Wallington\nb.Zendaya\nc. Scarrlet Johanson\nd. Peter Parker',
        "Answer" : "c"
    },
    
    "Q5" : {
        "Question" : 'What is the name of the alternate dimension in Netflix’s Stranger Things?\na. Elevens World\nb. The Upside Down\nc. The Rightside Up\nd. std::cout <<Hey<<',
        "Answer" : "b"
    },
    
    "Q6" : {
        "Question" : 'Who was the first African-American man to achieve EGOT status?\na. John Legend\nb. Common\nc. Morgan Freeman\nd. Mr. Allen Washington',
        "Answer" : "a"
    },
    
    "Q7" : {
        "Question" : ' Which hit 1998 Eddie Murphy comedy finally got a sequel in 2021?\na. America to Coming\nb. The Waterworks\nc. Coming to America\nd. Black Panther',
        "Answer" : "c"
    },
    
    "Q8" : {
        "Question" : 'What year did Keeping Up with the Kardashians first premiere?\na. 1997\nb. 2007\nc. 2001\nd. 2004',
        "Answer" : "b"
    }
    
    
}

name = input("Welcome to Millionaire! What is your name? ")
questions_correct = 0
Friend_Uses = 0 #I looked it up and it said two was the max 
print(f"Currently you have made $0.")

def Phone_A_Friend(Friend_Uses, Question, Answer):
    if Friend_Uses >= 2:
        print("You have exahusted all of your phone calls, sorry!")
    else:
        Friend_Names = ["Derek", "Gary" ,"Amy", "Ari", "Veronica", "Will", "Reed","Rebecca", "Alvin"]
        Friend = random.choice(Friend_Names)
        
        
        if random.random() == 0.15:
            answer = chr(ord(Answer) + 1)
        else:
            answer = Answer
        
        
        print(f"\n{name} : {Friend}! I need your help answering this question : {Question}")
        print(f"\n{Friend} : Hm...... I think the answer is : {answer}\n")
        


for i in Millionaire_Questions:
    print(Millionaire_Questions[i]["Question"])
    if Friend_Uses <= 2:
        print("\nYou can type friend to use one of your two phone a friend's\n")
    Answer = input(">> ").lower()
    if Answer == "friend":
        Phone_A_Friend(Friend_Uses, Millionaire_Questions[i]["Question"], Millionaire_Questions[i]["Answer"])
        Answer = input("Your final answer : ").lower()
        Friend_Uses += 1
    print(f"\n Your answer : {Answer}\n")
    
    
    if Answer == Millionaire_Questions[i]["Answer"]:
        questions_correct += 1
        print(f"Correct!\nCurrently you have made ${award_prize(questions_correct)}.\n")
    else:
        print("I'm sorry, that is incorrect.\n")
        break

if questions_correct == 8:
    print("You are a millionaire!")
else:
    pass
 


 
 
    