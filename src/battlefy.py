import urllib
import sys
import math
import time
from selenium import webdriver
from bs4 import BeautifulSoup

from bracket import generate16SEBracket
from bracket import generate32SEBracket
from bracket import generate64SEBracket

def battlefy(link, size):

    driver = webdriver.Chrome("{0}/driver/chromedriver.exe".format(sys.path[0]))
    driver.get(link)
	
    print("Waiting for page to load...")
    time.sleep(5)
    results = driver.page_source
    driver.quit()
	
    soup = BeautifulSoup(results, 'html.parser')
    matches = soup.findAll('g', class_='node')
	
    team1 = []
    team2 = []
    score1 = []
    score2 = []

    for match in matches:
        matchNumber = match.find('text', class_='match-number').contents[0].strip('#')

        nameTop = match.find('text', { 'data-position': 'top' }).contents[0]
        nameBottom = match.find('text', { 'data-position': 'bottom' }).contents[0]


        if ( nameTop != 'BYE' and nameBottom != 'BYE'):
            scoreTop = match.find('text', class_='top-score').contents[0]
            scoreBottom = match.find('text', class_='bottom-score').contents[0]
			
        team1.append(nameTop)
        team2.append(nameBottom)
        score1.append(scoreTop)
        score2.append(scoreBottom)

		
    if len(team1) < size - 1:
        return "ERROR: Retry with a smaller bracket size"
		
    bracketSize = len(team1) + 1
    n = int(math.log(bracketSize, 2))
    finalteam1 = []
    finalteam2 = []
    finalscore1 = []
    finalscore2 = []
    
    for x in range(0, n):
        rowteam1 = []
        rowteam2 = []
        rowscore1 = []
        rowscore2 = []
        power = int(math.pow(2,x))
        for y in range(0, power):
            if y == 0:
                curr = x
            elif y % 2 == 1:
                curr = curr + bracketSize / power - 1
            elif y % 2 == 0 and y % 4 != 0 and y % 8 != 0 and y % 16 != 0 and y % 32 != 0:
                curr = curr + bracketSize / power
            elif y % 2 == 0 and y % 4 == 0 and y % 8 != 0 and y % 16 != 0 and y % 32 != 0:
                curr = curr + bracketSize / power + 1
            elif y % 2 == 0 and y % 4 == 0 and y % 8 == 0 and y % 16 != 0 and y % 32 != 0:
                curr = curr + bracketSize / power + 2
            elif y % 2 == 0 and y % 4 == 0 and y % 8 == 0 and y % 16 == 0 and y % 32 != 0:
                curr = curr + bracketSize / power + 3
            elif y % 2 == 0 and y % 4 == 0 and y % 8 == 0 and y % 16 == 0 and y % 32 == 0:
                curr = curr + bracketSize / power + 4
            rowteam1.append(team1[curr])
            rowteam2.append(team2[curr])
            rowscore1.append(score1[curr])
            rowscore2.append(score2[curr])
        finalteam1 = finalteam1 + rowteam1[::-1]
        finalteam2 = finalteam2 + rowteam2[::-1]
        finalscore1 = finalscore1 + rowscore1[::-1]
        finalscore2 = finalscore2 + rowscore2[::-1]
	
    team1 = finalteam1[:(size-1)][::-1]
    team2 = finalteam2[:(size-1)][::-1]
    score1 = finalscore1[:(size-1)][::-1]
    score2 = finalscore2[:(size-1)][::-1]
    
    if size == 64:
        return generate64SEBracket(team1, team2, score1, score2)
    elif size == 32:
        return generate32SEBracket(team1, team2, score1, score2)
    elif size == 16:
        return generate16SEBracket(team1, team2, score1, score2)
    else:
        return "No result"