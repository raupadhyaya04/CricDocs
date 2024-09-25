from reportGenerator import generate_text_report, honMention # Aim: Reduce input and provide a solid output
print("Main Header:\n")
club = input("Which club is this for?\n")
team = input(f"Which {club} team was playing\n") 
opposition = input("Which club was the team playing against?\n")
venue = input("Was this game at Home or Away?\n")
victor = input("Who won this game?\n")
if (victor != team and victor != opposition):
    print(f"sorry, invalid input, please insert {club} or {opposition}")
    victor = input("Who won this game?\n")
endState = input("Did they bat or bowl first? (bat/bowl)\n")
while (endState != "bat" and endState != "bowl"):
    print("Sorry, incorrect input\n")
    endState = input("Did they bat or bowl first? (bat/bowl)\n")
margin = ""
if endState == "bat":
    endState = "runs"
    margin = input("How many runs did they win by?\n")
elif endState == "bowl":
    endState = "wickets"
    margin = input("How many wickets did they win by?\n")
date = input("What's today's date?\n")
book = input("Where can people find the scorebook? (insert the link if there is one)\n")
print("Match Overview:\n")
toss_details = input("Describe what happened at the coin toss, add on any details about the match here (eg if it got rained off)\n") 
first_innings = input("Describe what happened in the first innnings\n") 
second_innings = input("Describe what happened in the second innings\n")
print("Stats:\n")
bBatter = input("Who was the best batter?\n")
batStats = input("How many runs did they score?\n")
bBowler = input("Who was the best bowler?\n")
bowlStats = input("What were their bowling figures?")
mCatches = input("Who took the most catches?\n")
catchStats = input("How many catches did they take?\n")
mRunouts = input("Who got the most runouts?\n") 
nRunouts = input("How many runouts did they get?\n")
print("Skill Breakdown:\n")
goodBatSkills = input("What skills were well implemented by the batters?\n")
whyGoodBat = input("Why was it good that these skills were done well?\n")
goodBowlSkills = input("What skills were well implemented by the bowlers?\n")
whyGoodBowl = input("Why was it good that these skills were done well?\n")
goodFieldSkills = input("What skills were well implemented by the fielders?\n")
whyGoodField = input("Why was it good that these skills were done well?\n")
badBatSkills = input("What skills were not as well implemented by the batters?\n")
whyBadBat = input("Why is it important to work on these skills to a better standard? What suggestions would you make to the players/parents of players?\n")
badBowlSkills = input("What skills were not as well implemented by the bowlers?\n")
whyBadBowl = input("Why is it important to work on these skills to a better standard? What suggestions would you make to the players/parents of players?\n")
badFieldSkills = input("What skills were not as well implemented by the fielders?\n")
whyBadField = input("Why is it important to work on these skills to a better standard? What suggestions would you make to the players/parents of players?\n")
print("Mentions:\n")
bestPlayer = input("Who is the player of the Match?\n")
bestStats = input("What was the main statistic(s) that stood out?\n")
eHonMentions = True
goodPlayers = []
goodStats = []
e = input("Are there any honourable mentions? (y/n)")
if e == "y":
    eHonMentions = False
while (eHonMentions != True):
    goodPlayer = input("Any other performances that you felt deserved credit?\n")
    goodPlayers.append(goodPlayer)
    goodStat = input("What was the main statistic(s) that stood out?\n")
    goodStats.append(goodStat)
    e = input("Is that all the honourable mentions? (y/n)")
    if e == "y":
        eHonMentions = True
honMentions = honMention(goodPlayers, goodStats)
print("Signing off:\n")
name = input("What is your name? (full name ideally)\n") 
position = input("What position do you work as in terms of coaching (i.e. Youth Cricket Coach, Boys u17 Head Coach, etc)\n") 

print(generate_text_report(club, team, opposition, venue, victor, margin, endState, date, book, toss_details, first_innings, second_innings, bBatter, batStats, bBowler, bowlStats, mCatches, catchStats, mRunouts, nRunouts, goodBatSkills, whyGoodBat, goodBowlSkills, whyGoodBowl, goodFieldSkills, whyGoodField, badBatSkills, whyBadBat, badBowlSkills, whyBadBowl, badFieldSkills, whyBadField, bestPlayer, bestStats, honMentions, name, position))