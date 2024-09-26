from flask import Flask, request, jsonify
from reportGenerator import generate_text_report, honMention
from sessionPlanGenerator import generate_session_plan_text

app = Flask(__name__)
goodPlayers = []
goodStats = []

# @app.route('/')
# def getLandingPage():
 #   return 

@app.route('/generate_cricket_match_report', methods=['POST', 'GET'])
def generate_report():
    if request.method == "POST":
        club = request.form["clubName"]
        team = request.form["teamGroup"]
        opposition = request.form["opp"]
        venue = request.form["venue"]
        victor = request.form["victor"]
        margin = request.form["margin"]
        endState = request.form["endState"]
        date = request.form["date"]
        book = request.form["book"]
        toss_details = request.form["toss_details"]
        first_innings = request.form["first_innings"]
        second_innings = request.form["second_innings"]
        bBatter = request.form["bBatter"]
        batStats = request.form["batStats"]
        bBowler = request.form["bBowler"]
        bowlStats = request.form["bowlStats"]
        mCatches = request.form["mCatches"]
        catchStats = request.form["catchStats"]
        mRunouts = request.form["mRunouts"]
        nRunouts = request.form["nRunouts"]
        goodBatSkills = request.form["goodBatSkills"]
        whyGoodBat = request.form["whyGoodBat"]
        goodBowlSkills = request.form["goodBowlSkills"]
        whyGoodBowl = request.form["whyGoodBowl"]
        goodFieldSkills = request.form["goodFieldSkills"]
        whyGoodField = request.form["whyGoodField"]
        badBatSkills = request.form["badBatSkills"]
        whyBadBat = request.form["whyBadBat"]
        badBowlSkills = request.form["badBowlSkills"]
        whyBadBowl = request.form["whyBadBowl"]
        badFieldSkills = request.form["badFieldSkills"]
        whyBadField = request.form["whyBadField"]
        bestPlayer = request.form["bestPlayer"]
        bestStats = request.form["bestStats"]
        goodPlayer = request.form["goodPlayer"]
        goodPlayers.append(goodPlayer)
        goodStat = request.form["goodStat"]
        goodStats.append(goodStat)
        name = request.form["coachName"]
        position = request.form["coachPos"]
    
    honMentions = honMention(goodPlayers, goodStats)
    return jsonify({"report": generate_text_report(club, team, opposition, venue, victor, margin, endState, date, book, toss_details, first_innings, second_innings, bBatter, batStats, bBowler, bowlStats, mCatches, catchStats, mRunouts, nRunouts, goodBatSkills, whyGoodBat, goodBowlSkills, whyGoodBowl, goodFieldSkills, whyGoodField, badBatSkills, whyBadBat, badBowlSkills, whyBadBowl, badFieldSkills, whyBadField, bestPlayer, bestStats, honMentions, name, position)})


@app.route('/generate_cricket_match_report', methods=['POST', 'GET'])
def generate_session_planner():
    if request.method == "POST":
        age = request.form["age"]
        cgoals = request.form["cGoals"]
        pgoals = request.form["pGoals"]
        date = request.form["date"]
        venue = request.form["venue"]
        duration = request.form["duration"]
        equipment = request.form["equipment"]
        safety = request.form["safety"]
        warmup = request.form["warmup"]
        skills = request.form["skills"]
        drills = request.form["drills"]
        games = request.form["games"]
        cooldown = request.form["cooldown"]
        eval = request.form["eval"]
    
    return jsonify({"session plan": generate_session_plan_text(age, cgoals, pgoals, date, venue, duration, equipment, safety, warmup, skills, drills, games, cooldown, eval)})

if __name__ == '__main__':
    app.run(debug=True)