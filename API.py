from flask import Flask, request, render_template
from reportGenerator import generate_text_report, honMention
from sessionPlanGenerator import generate_session_plan_text

app = Flask(__name__)
goodPlayers = []
goodStats = []

@app.route('/')
def getLandingPage():
    return render_template("index.html")

@app.route('/generate/cricket/match_report', methods=['POST', 'GET'])
def generate_report():
    if request.method == "POST":
        clubs = request.form['club']
        team = request.form['team']
        opposition = request.form['opposition']
        venue = request.form.get('venue')
        victor = request.form.get('victor')
        endState = request.form.get('endState')
        margin = request.form.get('margin')
        date = request.form.get('date')
        book = request.form.get('book')
        toss_details = request.form.get('toss_details')
        first_innings = request.form.get('first_innings')
        second_innings = request.form.get('second_innings')
        bBatter = request.form.get('bBatter')
        batStats = request.form.get('batStats')
        bBowler = request.form.get('bBowler')
        bowlStats = request.form.get('bowlStats')
        mCatches = request.form.get('mCatches')
        catchStats = request.form.get('catchStats')
        mRunouts = request.form.get('mRunouts')
        nRunouts = request.form.get('nRunouts')
        bestPlayer = request.form.get('bestPlayer')
        bestStats = request.form.get('bestStats')
        honMentions = request.form.get('honMentions')
        goodPlayer = request.form.get('goodPlayers')
        goodPlayers.append(goodPlayer)
        goodStat = request.form.get('goodStats')
        goodStats.append(goodStat)
        name = request.form.get('name')
        position = request.form.get('position')

        goodBatSkills = request.form.get('goodBatSkills')
        whyGoodBat = request.form.get('whyGoodBat')
        goodBowlSkills = request.form.get('goodBowlSkills')
        whyGoodBowl = request.form.get('whyGoodBowl')
        goodFieldSkills = request.form.get('goodFieldSkills')
        whyGoodField = request.form.get('whyGoodField')
        badBatSkills = request.form.get('badBatSkills')
        whyBadBat = request.form.get('whyBadBat')
        badBowlSkills = request.form.get('badBowlSkills')
        whyBadBowl = request.form.get('whyBadBowl')
        badFieldSkills = request.form.get('badFieldSkills')
        whyBadField = request.form.get('whyBadField')
        
    
    
    return render_template("reportGen.html")

@app.route('/generate/cricket/session_planner', methods=['POST', 'GET'])
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

    text = generate_session_plan_text(age, cgoals, pgoals, date, venue, duration, equipment, safety, warmup, skills, drills, games, cooldown, eval)
    return text

if __name__ == '__main__':
    app.run(debug=True)