def generate_text_report(team, opposition, venue, victor, margin, endState, date, book, overview, bBatter, bBowler, mCatches, mRunouts, goodBatSkills, goodBowlSkills, goodFieldSkills, badBatSkills, badBowlSkills, badFieldSkills, motm, goodPlayers, name, position):
    text = f"""\033[3mMatch Report — {team} vs {opposition} ({venue}):\033[3m

Result: {victor} won by {margin} {endState}
Date: {date}
Scorebook: {book}

Match Overview:
{overview}

Stats:
Best Batting: {bBatter}
Best Bowling: {bBowler}
Most Catches: {mCatches}
Most runouts: {mRunouts}

Skill Breakdown:
What went well:
Batting:
{goodBatSkills}

Bowling:
{goodBowlSkills}

Fielding:
{goodFieldSkills}

What to improve on:
Batting:
{badBatSkills}

Bowling:
{badBowlSkills}

Fielding:
{badFieldSkills}


Man of the match: {motm}

Honourable mentions:
{goodPlayers}


Best wishes,
{name},
{position}"""
    return text