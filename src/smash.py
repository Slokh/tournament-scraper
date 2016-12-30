import urllib
from bs4 import BeautifulSoup

from bracket import generate16SEBracket
from bracket import generate32SEBracket
from bracket import generate64SEBracket

def smash(link, size):

    results = urllib.urlopen(link).read()
    soup = BeautifulSoup(results, 'html.parser')
    matches = soup.findAll('div', class_='match-affix-wrapper')
	
    team1 = []
    team2 = []
    score1 = []
    score2 = []

    for match in matches:
        names = match.findAll('div', class_='text-ellipsis')
        nameTop = names[0].contents[0]
        nameBottom = names[1].contents[0]

        scores = match.findAll('div', class_='match-player-stocks')
        scoreTop = scores[0].contents[0]
        scoreBottom = scores[1].contents[0]

        team1.append(nameTop)
        team2.append(nameBottom)
        score1.append(scoreTop)
        score2.append(scoreBottom)
		
    if len(team1) < size - 1:
        return "ERROR: Retry with a smaller bracket size"

    team1 = team1[::-1][:(size-1)][::-1]
    team2 = team2[::-1][:(size-1)][::-1]
    score1 = score1[::-1][:(size-1)][::-1]
    score2 = score2[::-1][:(size-1)][::-1]
    for x in range(0, len(team1)):
        print("{0} vs {1}".format(team1[x], team2[x]))
    
    if size == 64:
        return generate64SEBracket(team1, team2, score1, score2)
    elif size == 32:
        return generate32SEBracket(team1, team2, score1, score2)
    elif size == 16:
        return generate16SEBracket(team1, team2, score1, score2)
    else:
        return "ERROR: No result"
