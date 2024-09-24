from reportGenerator import generate_text_report
print("Main Header:\n")
club = input("Which club is this for?\n")
team = input("Which team was playing\n") 
opposition = input("Who was the team playing against? (ideally insert just the club name)\n")
venue = input("Was this game at home or away? (H/A)\n")
while (venue != "H" or venue != "A"):
    print("Sorry, invalid input\n")
    venue = input("Was this game at home or away? (H/A)\n")
victor = input("Who won this game?\n")
if victor != team or victor != opposition:
    print("sorry, invalid input, please insert {club} or {opposition}")
    victor = input("Who won this game?\n")
endState = input("Did they win by batting or bowling first? (bat/bowl)\n")
margin = ""
if endState == "bat":
    endState = "runs"
    margin = input("By how many runs?\n")
elif endState == "bowl":
    endState == "wickets"
    margin = input("By how many wickets?\n")
date = input("What's today's date?\n")
book = input("Where can people find the scorebook (or insert the link now)\n") 
print("Match Overview:\n")
overview = input("What happened in the match?\n") # TODO: Reduce the amount of work one must do for this
print("Stats:\n")
bBatter = input("Who was the best batter? What were their batting stats?\n") # TODO for all stats: Separate the fucking name and the stats
bBowler = input("Who was the best bowler? What were their bowling stats?\n") 
mCatches = input("Who took the most catches? What were their catching stats?\n")
mRunouts = input("Who got the most runouts? What were their runout stats?\n") 
print("Skill Breakdown:\n")
goodBatSkills = input("What skills were well implemented by the batters? Why?\n") # TODO for all types of skills: Separate the skills from the why
goodBowlSkills = input("What skills were well implemented by the bowlers? Why?\n") 
goodFieldSkills = input("What skills were well implemented by the fielders? Why?\n") 
badBatSkills = input("What skills were not as well implemented by the batters? Why?\n") 
badBowlSkills = input("What skills were not as well implemented by the bowlers? Why?\n") 
badFieldSkills = input("What skills were not as well implemented by the fielders? Why?\n")
print("Mentions:\n")
motm = input("Who is the player of the Match?\n") 
goodPlayers = input("Any other performances that you felt deserved credit?\n") 
name = input("What is your name? (full name ideally)\n") 
position = input("What position do you work in terms of coaching (i.e. Youth Cricket Coach, u11 Head Coach, etc)\n") 

print(generate_text_report(team, opposition, venue, victor, margin, endState, date, book, overview, bBatter, bBowler, mCatches, mRunouts, goodBatSkills, goodBowlSkills, goodFieldSkills, badBatSkills, badBowlSkills, badFieldSkills, motm, goodPlayers, name, position))