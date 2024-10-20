from flask import Flask, request, render_template, send_file, redirect, session, url_for
from reportGenerator import generate_text_report_olderYouth, generate_text_report_youngerYouth, honMentions
from sessionPlanGenerator import generate_session_plan_text
from creating_pdf import create_pdf
import os
from configurer import configure

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


app = Flask(__name__)

app.secret_key = os.getenv("secret_key")

def main():
    configure()
main()

@app.route('/')
def getLandingPage():
    session.clear()
    if 'match_data' not in session:
        session['match_data'] = {}
    if 'session_data' not in session:
        session['session_data'] = {}
    return render_template("index.html")

@app.route('/generate/cricket/match_report/team-sheet', methods=['POST', 'GET'])
def getTeamSheet():
    match_data = session["match_data"]
    teamSheet = match_data.get('teamSheet', [])
    if request.method == "POST":
        player = request.form.get('player')
        if player:
            teamSheet.append(player)
    match_data['teamSheet'] = teamSheet
    session["match_data"] = match_data
    print("Input:", session['match_data'])
    return render_template("teamSheet.html", teamSheet = teamSheet)

@app.route('/generate/cricket/match_report/main-details', methods=['POST', 'GET'])
def main_details():
    if request.method == "POST":
        match_data = session["match_data"]
        mainDetails = request.form.to_dict()
        match_data.update(mainDetails)
        session['match_data'] = match_data
    print("Input:", session['match_data'])
    return render_template("mainDetails.html")

@app.route('/generate/cricket/match_report/match-overview', methods=['POST', 'GET'])
def match_overview():
    if request.method == "POST":
        match_data = session["match_data"]
        matchOverview = request.form.to_dict()
        match_data.update(matchOverview)
        session['match_data'] = match_data
    print("Input: ", session['match_data'])
    return render_template("matchOverview.html")

@app.route('/generate/cricket/match_report/stats', methods=['POST', 'GET'])
def matchStats():
    if request.method == "POST":
        match_data = session['match_data']
        matchStats = request.form.to_dict()
        match_data.update(matchStats)
        session['match_data'] = match_data
    print("Input:", session['match_data'])

    if session['match_data'].get('team') in ['u13', 'u11']:
        return redirect(url_for("honMention"))
    return render_template("matchStats.html", teamSheet = session["match_data"].get("teamSheet"))

@app.route('/generate/cricket/match_report/skill-breakdown', methods=['POST', 'GET'])
def skillBreakdown():
    if request.method == "POST":
        match_data = session['match_data']
        skillBdown = request.form.to_dict()
        match_data.update(skillBdown)
        session['match_data'] = match_data
    print("Input:", session['match_data'])
    if session['match_data'].get("team") == "u19" or session['match_data'].get("team") == "u17":
        return render_template("skillBreakdown.html", teamSheet = session["match_data"].get("teamSheet"))
    return render_template("skillBreakdownYounger.html")

@app.route('/generate/cricket/match_report/remove-player', methods=['POST'])
def remove_player():
    match_data = session["match_data"]
    teamSheet = match_data.get("teamSheet")
    player_to_remove = request.form.get('player_to_remove')
    if player_to_remove in teamSheet:
        teamSheet.remove(player_to_remove)
    session["match_data"] = match_data
    return redirect(url_for('getTeamSheet'))


@app.route('/generate/cricket/match_report/mentions', methods=['POST', 'GET'])
def honMention():
    goodPlayers = []
    goodStats = []
    string = ""
    if request.method == "POST":
        match_data = session["match_data"]
        goodPlayer = request.form.get('goodPlayer')
        goodStat = request.form.get('goodStat')
        goodPlayers.append(goodPlayer)
        goodStats.append(goodStat)
        string += honMentions(goodPlayers, goodStats)
        if string == None or string.isalpha() == False:
            string = "Nothing of note, everyone did well in their own regards"
        match_data.update({'honMentions' : string})
        session["match_data"] = match_data
    print("Input:", session['match_data'])
    return render_template("mentions.html", teamSheet = session["match_data"].get("teamSheet"))

@app.route('/generate/cricket/match_report/signoff', methods=['POST', 'GET'])
def signoff():
    if request.method == "POST":
        match_data = session["match_data"]
        signingOff = request.form.to_dict()
        match_data.update(signingOff)
        session["match_data"] = match_data
    print("Input:", session['match_data'])
    return render_template("signoff.html")

@app.route('/generate/cricket/session_planner', methods=['POST', 'GET'])
def generate_session_planner():
    if request.method == "POST":
        session_data = session['session_data']
        sesh = request.form.to_dict()
        session_data.update(sesh)
        session['session_data'] = session_data

        return render_template("sessionGen.html")
    return render_template("sessionGen.html")

@app.route('/output/report', methods=['GET', 'POST'])
def outputReport():
    match_data = session['match_data']
    text = ""
    endState = ""
    victor = ""

    if (match_data.get("team") == "u17" or match_data.get("team") == "u19"):

        # Main Details:
        club = match_data.get('club')
        gender = match_data.get('gender')
        team = match_data.get('team')
        opposition = match_data.get('opposition')
        venue = match_data.get('venue')
        victory = match_data.get('victor')
        if victory == "yes":
            victor = club
        elif victory == "no":
            victor = opposition
        endStater = match_data.get('endState')
        if endStater == "bat":
            endState = "runs"
        elif endStater == "bowl":
            endState = "wickets"
        margin = match_data.get('margin')
        date = match_data.get('date')
        book = match_data.get('book')

        # Match Overview:
        toss_details = match_data.get('toss_details')
        first_innings = match_data.get('first_innings')
        second_innings = match_data.get('second_innings')

        # Stats:
        bBatter = match_data.get('bBatter')
        batStats = match_data.get('batStats')
        bBowler = match_data.get('bBowler')
        bowlStats = match_data.get('bowlStats')
        mCatches = match_data.get('mCatches')
        catchStats = match_data.get('catchStats')
        mRunouts = match_data.get('mRunouts')
        nRunouts = match_data.get('nRunouts')

        # Skill Breakdown:
        goodBatSkills = match_data.get('goodBatSkills')
        whyGoodBat = match_data.get('whyGoodBat')
        goodBowlSkills = match_data.get('goodBowlSkills')
        whyGoodBowl = match_data.get('whyGoodBowl')
        goodFieldSkills = match_data.get('goodFieldSkills')
        whyGoodField = match_data.get('whyGoodField')

        badBatSkills = match_data.get('badBatSkills')
        whyBadBat = match_data.get('whyBadBat')
        badBowlSkills = match_data.get('badBowlSkills')
        whyBadBowl = match_data.get('whyBadBowl')
        badFieldSkills = match_data.get('badFieldSkills')
        whyBadField = match_data.get('whyBadField')

        # Stats:
        bestPlayer = match_data.get('bestPlayer')
        bestStats = match_data.get('bestStats')

        # Noteworthy Performances:
        honMentions = match_data.get('honMentions')

        # Signoff:
        name = match_data.get('name')
        position = match_data.get('position')

        text = generate_text_report_olderYouth(club, gender, team, opposition, venue, victor, margin, endState, date, 
                                    book, toss_details, first_innings, second_innings, bBatter, batStats, 
                                    bBowler, bowlStats, mCatches, catchStats, mRunouts, nRunouts, goodBatSkills, 
                                    whyGoodBat, goodBowlSkills, whyGoodBowl, goodFieldSkills, whyGoodField, badBatSkills, 
                                    whyBadBat, badBowlSkills, whyBadBowl, badFieldSkills, whyBadField, bestPlayer, bestStats, 
                                    honMentions, name, position)
        match_data.update({"text":text})
        session["match_data"] = match_data
        
    else:
        # Main Details:
        club = match_data.get('club')
        gender = match_data.get('gender')
        team = match_data.get('team')
        opposition = match_data.get('opposition')
        venue = match_data.get('venue')
        victory = match_data.get('victor')
        if victory == "yes":
            victor = club
        elif victory == "no":
            victor = opposition
        endStater = match_data.get('endState')
        if endStater == "bat":
            endState = "runs"
        elif endStater == "bowl":
            endState = "wickets"
        margin = match_data.get('margin')
        date = match_data.get('date')
        book = match_data.get('book')

        # Match Overview:
        toss_details = match_data.get('toss_details')
        first_innings = match_data.get('first_innings')
        second_innings = match_data.get('second_innings')

        # Skill Breakdown:
        goodSkills = match_data.get('goodSkills')
        whyGoodSkills = match_data.get('whyGoodSkills')
        badSkills = match_data.get('badSkills')
        whyBadSkills = match_data.get('whyBadSkills')

        # Honourable Mentions:
        honMentions = match_data.get('honMentions')

        # Signoff:
        name = match_data.get('name')
        position = match_data.get('position')

        text = generate_text_report_youngerYouth(club, gender, team, opposition, venue, victor, margin, endState, date, book, 
                                                 toss_details, first_innings, second_innings, goodSkills, whyGoodSkills, badSkills, 
                                                 whyBadSkills, honMentions, name, position)
        match_data.update({"text":text})
        session["match_data"] = match_data

    return render_template("output.html", text=text)

@app.route("/output/session_planner", methods=["POST", "GET"])
def outputSession():
    session_data = session['session_data']
    text = ""
    age = session_data.get("age")
    cgoals = session_data.get("cgoals")
    pgoals = session_data.get("pgoals")
    date = session_data.get("date")
    venue = session_data.get("venue")
    duration = session_data.get("duration")
    equipment = session_data.get("equipment")
    safety = session_data.get("safety")
    warmup = session_data.get("warmup")
    skills = session_data.get("skills")
    drills = session_data.get("drills")
    games = session_data.get("games")
    cooldown = session_data.get("cooldown")
    eval = session_data.get("eval")

    text = generate_session_plan_text(age, cgoals, pgoals, date, venue, duration, equipment, safety, warmup, skills, drills, games, cooldown, eval)
    session_data.update({"text":text})
    session["session_data"] = session_data
    return render_template("output.html", text=text)

@app.route('/download-pdf')
def download_pdf():
    session_data = session["session_data"]
    match_data = session["match_data"]
    text = ""

    if session_data.get("text") == None:
        text = match_data.get("text")
    elif match_data.get("text") == None:
        text = session_data.get("text")

    # Create the PDF
    pdf_buffer = create_pdf(text)

    # Send the PDF file as a downloadable file
    return send_file(pdf_buffer, as_attachment=True, download_name="CricDoc.pdf", mimetype='application/pdf')

@app.route("/generate/cricket/output/report")
def redirect_report():
    return redirect("/output/report", code=302)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False)