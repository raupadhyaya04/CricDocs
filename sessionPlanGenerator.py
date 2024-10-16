def generate_session_plan_text(age, cgoals, pgoals, date, venue, duration, equipment, safety, warmup, skills, drills, games, cooldown, eval):
    title = f"""Session Plan:\n
"""
    deets = f"""
Date: {date}\n
Coach Outcomes: {cgoals}\n
Player Outcomes: {pgoals}\n
Age Group: {age}\n
Duration: {duration}\n
Venue: {venue}\n
Equipment: {equipment}\n
Safety Considerations: {safety}\n"""
    
    session = f"""
Warm up: {warmup}\n
Skills: {skills}\n
Drills: {drills}\n
Games: {games}\n"""
    eOfSession = f"""
Cooldown: {cooldown}\n
Evaluation (Key points/learnings, etc): {eval}"""
    text = title + deets + session + eOfSession
    return text