def generate_session_plan_text(age, cgoals, pgoals, date, venue, duration, equipment, safety, warmup, skills, drills, games, cooldown, eval):
    title = f"""Session Plan:\n
"""
    deets = f"""Date: {date}
Coach Outcomes: {cgoals}
Player Outcomes: {pgoals}
Age Group: {age}
Duration: {duration}
Venue: {venue}
Equipment: {equipment}
Safety Considerations: {safety}"""
    
    session = f"""Warm up: {warmup}
Skills: {skills}
Drills: {drills}
Games: {games}"""
    eOfSession = f"""Cooldown: {cooldown}
Evaluation (Key points/learnings, etc): {eval}"""
    text = title + deets + session + eOfSession
    return text