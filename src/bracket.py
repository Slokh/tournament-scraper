team1 = []
team2 = []
score1 = []
score2 = []

def formatResult(identifier, start, end):
    global team1
    global team2
    global score1
    global score2
    result = ""
    for x in range(start,end):
        y = 2*(x-start)+1
        if team1[x] != "BYE" and team2[x] != "BYE":
            if score1[x] > score2[x]:
                team1[x] = "'''{{{{teamShort|{0}}}}}'''".format(team1[x])
                team2[x] = "{{{{teamShort|{0}}}}}".format(team2[x])
                score1[x] = "'''{0}'''".format(score1[x])
            else:
                team1[x] = "{{{{teamShort|{0}}}}}".format(team1[x])
                team2[x] = "'''{{{{teamShort|{0}}}}}'''".format(team2[x])
                score2[x] = "'''{0}'''".format(score2[x])
            result += "|R{0}{1}={2} |R{3}{4}score={5}\n".format(identifier, y, team1[x], identifier, y, score1[x])
            y = y + 1
            result += "|R{0}{1}={2} |R{3}{4}score={5}\n".format(identifier, y, team2[x], identifier, y, score2[x])
        elif team1[x] == "BYE" and team2[x] != "BYE":
            result += "|R{0}{1}={2} |R{3}{4}score={5}\n".format(identifier, y, "BYE", identifier, y, "-")
            y = y + 1
            result += "|R{0}{1}='''{{{{teamShort|{2}}}}}''' |R{3}{4}score={5}\n".format(identifier, y, team2[x], identifier, y, "'''W'''")
        elif team1[x] != "BYE" and team2[x] == "BYE":
            result += "|R{0}{1}='''{{{{teamShort|{2}}}}}''' |R{3}{4}score={5}\n".format(identifier, y, team1[x], identifier, y, "'''W'''")
            y = y + 1
            result += "|R{0}{1}={2} |R{3}{4}score={5}\n".format(identifier, y, "BYE", identifier, y, "-")
    return result

def generate64SEBracket(team1, team2, score1, score2):
    initializeBracket(team1, team2, score1, score2)
    result = "{{64SEBracket\n"
    result += " <!-- ROUND OF 64 (Ro64) -->\n"
    result += formatResult("1D", 0, 32)
    result += "\n <!-- ROUND OF 32 (Ro32) -->\n"
    result += formatResult("2W", 32, 48)
    result += "\n <!-- ROUND OF 16 (Ro16) -->\n"
    result += formatResult("3W", 48, 56)
    result += "\n <!-- QUARTERFINALS -->\n"
    result += formatResult("4W", 56, 60)
    result += "\n <!-- SEMIFINALS -->\n"
    result += formatResult("5W", 60, 62)
    result += "\n <!-- FINAL MATCH -->\n"
    result += formatResult("6W", 62, 63)
    result += "\n <!-- 3RD PLACE (optional) -->\n|R6D1=    |R6D1score=\n|R6D2=    |R6D2score=\n}}"
    return result

def generate32SEBracket(team1, team2, score1, score2):
    initializeBracket(team1, team2, score1, score2)
    result = "{{32SEBracket\n"
    result += " <!-- ROUND OF 32 (Ro32) -->\n"
    result += formatResult("1D", 0, 16)
    result += "\n <!-- ROUND OF 16 (Ro16) -->\n"
    result += formatResult("2W", 16, 24)
    result += "\n <!-- QUARTERFINALS -->\n"
    result += formatResult("3W", 24, 28)
    result += "\n <!-- SEMIFINALS -->\n"
    result += formatResult("4W", 28, 30)
    result += "\n <!-- FINAL MATCH -->\n"
    result += formatResult("5W", 30, 31)
    result += "\n <!-- 3RD PLACE (optional) -->\n|R5D1=    |R5D1score=\n|R5D2=    |R5D2score=\n}}"
    return result

def generate16SEBracket(team1, team2, score1, score2):
    initializeBracket(team1, team2, score1, score2)
    result = "{{16SEBracket\n"
    result += " <!-- ROUND OF 16 (Ro16) -->\n"
    result += formatResult("1D", 0, 8)
    result += "\n <!-- QUARTERFINALS -->\n"
    result += formatResult("2W", 8, 12)
    result += "\n <!-- SEMIFINALS -->\n"
    result += formatResult("3W", 12, 14)
    result += "\n <!-- FINAL MATCH -->\n"
    result += formatResult("4W", 14, 15)
    result += "\n <!-- 3RD PLACE (optional) -->\n|R4D1=    |R4D1score=\n|R4D2=    |R4D2score=\n}}"
    return result
	
def initializeBracket(team1in, team2in, score1in, score2in):
    global team1
    global team2
    global score1
    global score2
    team1 = team1in
    team2 = team2in
    score1 = score1in
    score2 = score2in