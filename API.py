from flask import Flask, request, render_template, send_file
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportGenerator import generate_text_report_olderYouth, generate_text_report_youngerYouth, honMentions
from sessionPlanGenerator import generate_session_plan_text

text = ""


app = Flask(__name__)
match_data = {}
session_data = {}
goodPlayers = []
goodStats = []

def create_pdf(content):
    # Create a BytesIO object to hold the PDF in memory
    pdf_buffer = BytesIO()

    # Create the PDF with ReportLab
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter

    # Define text settings
    pdf.setFont("Helvetica", 12)
    margin = 50
    line_height = 14
    max_width = width - 2 * margin

    # Split the large string into lines using \n (newlines)
    paragraphs = content.splitlines()

    # Set the initial y position for writing text
    y_position = height - margin

    # Iterate over each paragraph (split by newlines)
    for paragraph in paragraphs:
        # If the paragraph is empty (i.e., blank line), skip it but keep the spacing
        if not paragraph.strip():
            y_position -= line_height
            continue

        # Break paragraph into smaller chunks that fit within the page width
        while len(paragraph) > 0:
            # Check if we need to create a new page before writing the next chunk of text
            if y_position < margin + line_height:
                pdf.showPage()  # Start a new page when we run out of space
                y_position = height - margin
                pdf.setFont("Helvetica", 12)  # Reset font settings after new page

            # Fit as much text as possible within the page width
            text_chunk = paragraph[:95]  # Adjust to fit your desired text width

            # Draw the text chunk
            pdf.drawString(margin, y_position, text_chunk)

            # Move to the next line
            y_position -= line_height

            # Update paragraph to remove the written chunk
            paragraph = paragraph[95:]

        # Add additional spacing after the paragraph
        y_position -= line_height

    # Save the PDF
    pdf.save()

    # Move the buffer's position to the start
    pdf_buffer.seek(0)

    return pdf_buffer



@app.route('/')
def getLandingPage():
    return render_template("index.html")

@app.route('/generate/cricket/match_report/main-details', methods=['POST', 'GET'])
def main_details():
    global match_data
    if request.method == "POST":
        match_data.update(request.form)
    print("Input:", match_data)
    return render_template("mainDetails.html")

@app.route('/generate/cricket/match_report/match-overview', methods=['POST', 'GET'])
def match_overview():
    global match_data
    if request.method == "POST":
        match_data.update(request.form)
    print("Input: ", match_data)
    return render_template("matchOverview.html")

@app.route('/generate/cricket/match_report/stats', methods=['POST', 'GET'])
def matchStats():
    global match_data
    if request.method == "POST":
        match_data.update(request.form)
    print("Input:", match_data)
    return render_template("matchStats.html")

@app.route('/generate/cricket/match_report/skill-breakdown', methods=['POST', 'GET'])
def skillBreakdown():
    global match_data
    if request.method == "POST":
        match_data.update(request.form)
    print("Input:", match_data)
    if match_data['team'] == "u19" or match_data['team'] == "u17":
        return render_template("skillBreakdown.html")
    return render_template("skillBreakdownYounger.html")

@app.route('/generate/cricket/match_report/mentions', methods=['POST', 'GET'])
def honMention():
    global match_data, goodPlayers, goodStats
    string = ""
    if request.method == "POST":
        goodPlayer = request.form.get('goodPlayer')
        goodStat = request.form.get('goodStat')
        goodPlayers.append(goodPlayer)
        goodStats.append(goodStat)
        string += honMentions(goodPlayers, goodStats)

    match_data.update({'honMentions' : string})
    print("Input:", match_data)
    return render_template("honMention.html")

@app.route('/generate/cricket/match_report/signoff', methods=['POST', 'GET'])
def signoff():
    global match_data
    if request.method == "POST":
        match_data.update(request.form)
    print("Input:", match_data)
    return render_template("signoff.html")

@app.route('/generate/cricket/session_planner', methods=['POST', 'GET'])
def generate_session_planner():
    global session_data
    if request.method == "POST":
        session_data.update(request.form)
        return render_template("sessionGen.html")
    return render_template("sessionGen.html")

@app.route('/output/report', methods=['GET', 'POST'])
def outputReport():
    endState = ""
    global text

    if (match_data["team"] == "u17" or match_data["team"] == "u19"):

        # Main Details:
        club = match_data.get('club')
        gender = match_data.get('gender')
        team = match_data.get('team')
        opposition = match_data.get('opposition')
        venue = match_data.get('venue')
        victory = match_data.get('victor')
        if victory == "Yes":
            victor = club
        elif victory == "No":
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

        # Honourable Mentions:
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
        
    elif (match_data["team"] == "u11" or match_data["team"] == "u13" or match_data['team'] == "u15"):
        # Main Details:
        club = match_data.get('club')
        gender = match_data.get('gender')
        team = match_data.get('team')
        opposition = match_data.get('opposition')
        venue = match_data.get('venue')
        victor = match_data.get('victor')
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
        goodSkills = match_data.get('goodSkills')
        whyGoodSkills = match_data.get('whyGoodSkills')
        badSkills = match_data.get('badSkills')
        whyBadSkills = match_data.get('whyBadSkills')

        # Stats:
        bestPlayer = match_data.get('bestPlayer')
        bestStats = match_data.get('bestStats')

        # Honourable Mentions:
        honMentions = match_data.get('honMentions')

        # Signoff:
        name = match_data.get('name')
        position = match_data.get('position')

        text = generate_text_report_youngerYouth(club, gender, team, opposition, venue, victor, margin, endState, date, book, 
                                                 toss_details, first_innings, second_innings, mCatches, mRunouts, bBatter, bBowler, 
                                                 batStats, bowlStats, catchStats, nRunouts, goodSkills, whyGoodSkills, badSkills, 
                                                 whyBadSkills, bestPlayer, bestStats, honMentions, name, position)

    return render_template("output.html", text=text)

@app.route("/output/session_planner", methods=["POST", "GET"])
def outputSession():
    global session_data, text
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
    return render_template("output.html")

@app.route('/download-pdf')
def download_pdf():
    global text

    # Create the PDF
    pdf_buffer = create_pdf(text)

    # Send the PDF file as a downloadable file
    return send_file(pdf_buffer, as_attachment=True, download_name="generated.pdf", mimetype='application/pdf')




if __name__ == '__main__':
    app.run(port=8000, debug=True)