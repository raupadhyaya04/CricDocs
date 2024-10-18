def generate_text_report_olderYouth(club, gender, team, opposition, venue, victor, margin, endState, date, book, toss_details, first_innings, second_innings, bBatter, batStats, bBowler, bowlStats, mCatches, catchStats, mRunouts, nRunouts, goodBatSkills, whyGoodBat, goodBowlSkills, whyGoodBowl, goodFieldSkills, whyGoodField, badBatSkills, whyBadBat, badBowlSkills, whyBadBowl, badFieldSkills, whyBadField, bestPlayer, bestStats, honMentions, name, position):
    title = f"""
Match Report — {club} {gender} {team} vs {opposition} ({venue}):

Result: {victor} won by {margin} {endState}
Date: {date}
Scorebook: {book}\n
"""
    overview = f"""Match Overview:
Toss:
At the toss, {toss_details}

First Innings:
In the first innings, {first_innings}.

Second Innings:
In the second innings, {second_innings}.\n
"""
    if mCatches == "" and mRunouts == "":
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}\n
"""
    elif mRunouts == "":
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most Catches: {mCatches}, {catchStats} catches\n
"""
    elif mCatches == "":
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most runouts: {mRunouts}, {nRunouts} runouts\n
"""
    else:
        stat = f"""
Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most Catches: {mCatches}, {catchStats} catches
Most runouts: {mRunouts}, {nRunouts} runouts\n
    """
        
    skills = f"""
Skill Breakdown:
What went well:
Batting:
{goodBatSkills}

Why it was good that these skills were done well:
{whyGoodBat}

Bowling:
{goodBowlSkills}

Why it was good that these skills were done well:
{whyGoodBowl}

Fielding:
{goodFieldSkills}

Why it was good that these skills were done well:
{whyGoodField}

What to improve on:
Batting:
{badBatSkills}

Why it's important to improve these skills to a better standard:
{whyBadBat}

Bowling:
{badBowlSkills}

Why it's important to improve these skills to a better standard:
{whyBadBowl}

Fielding:
{badFieldSkills}

Why it's important to improve these skills to a better standard:
{whyBadField}
\n
"""
    if (honMentions == "" or honMentions == None):
        mentions = f"""Player of the match: {bestPlayer} for their {bestStats}\n
"""
    else:
        mentions = f"""Player of the match: {bestPlayer} for their {bestStats}

Honourable mentions:
{honMentions}\n
"""
    signoff = f"""Best wishes,
{name},
{position}"""

    text = title + overview + stat + skills + mentions + signoff
    return text

def generate_text_report_youngerYouth(club, gender, team, opposition, venue, victor, margin, endState, date, book, toss_details, first_innings, second_innings, mCatches, mRunouts, bBatter, bBowler, batStats, bowlStats, catchStats, nRunouts, goodSkills, whyGoodSkills, badSkills, whyBadSkills, bestPlayer, bestStats, honMentions, name, position):
    title = f"""
Match Report — {club} {gender} {team} vs {opposition} ({venue}):

Result: {victor} won by {margin} {endState}
Date: {date}
Scorebook: {book}\n
"""
    overview = f"""Match Overview:
Toss:
At the toss, {toss_details}

First Innings:
In the first innings, {first_innings}.

Second Innings:
In the second innnings, {second_innings}.\n
"""
    if (mCatches == "" or mCatches == None) and (mRunouts == "" or mRunouts == None):
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}\n
"""
    elif (mRunouts == "" or mRunouts == None):
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most Catches: {mCatches}, {catchStats} catches\n
"""
    elif (mCatches == "" or mCatches == None):
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most runouts: {mRunouts}, {nRunouts} runouts\n
"""
    else:
        stat = f"""Stats:
Best Batting: {bBatter}, {batStats} runs
Best Bowling: {bBowler}, {bowlStats}
Most Catches: {mCatches}, {catchStats} catches
Most runouts: {mRunouts}, {nRunouts} runouts\n
    """
    
    skills = f"""
Skill Breakdown:
What went well:
{goodSkills}

Why it was good that these skills were done well:
{whyGoodSkills}

What to improve on:
{badSkills}

Why it's important to improve these skills to a better standard:
{whyBadSkills}
\n
"""
    if (honMentions == "" or honMentions == None):
        mentions = f"""Player of the match: {bestPlayer} for their {bestStats}\n
"""
    else:
        mentions = f"""Player of the match: {bestPlayer} for their {bestStats}

Honourable mentions:
{honMentions}\n
"""
    signoff = f"""Best wishes,
{name},
{position}"""

    text = title + overview + stat + skills + mentions + signoff
    return text


def honMentions(players, stats):
    string = ""
    for p, s in zip(players, stats):
        if (p and s) != "":
            string += f"{p} for their {s}\n"
    return string