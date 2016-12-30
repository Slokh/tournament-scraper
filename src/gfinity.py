import urllib
import codecs
import sys
import math
import time
from selenium import webdriver
from bs4 import BeautifulSoup

from bracket import generate16SEBracket
from bracket import generate32SEBracket
from bracket import generate64SEBracket

def gfinity(link, size):

    if ".net" in link:
        urllib.URLopener.version = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; T312461)'
        results = urllib.urlopen(link).read()
    else:
        results = codecs.open(link, 'r', 'utf-8').read()
		
    soup = BeautifulSoup(results, 'html.parser')
    matches = soup.findAll('div', class_='match')
	
    team1 = []
    team2 = []
    score1 = []
    score2 = []
    for match in matches:
        if match.find('div', class_='team-top') and match.find('div', class_='team-top').find('a'):
            nameTop = match.find('div', class_='team-top').find('a')['title'].encode('utf-8')
        else:
            nameTop = ""

        if "freewin" in match.get('class'):
            nameBottom = "BYE"
            scoreTop = 0
            scoreBottom = 0
        else:
            if match.find('div', class_='team-bottom') and match.find('div', class_='team-bottom').find('a'):
                nameBottom = match.find('div', class_='team-bottom').find('a')['title'].encode('utf-8')
            else:
                nameBottom = ""
            if match.find('div', class_='team-top') and match.find('div', class_='team-top').find('span', class_='score'):
                scoreTop = match.find('div', class_='team-top').find('span', class_='score').contents[0]
            else:
                scoreTop = 0
            if match.find('div', class_='team-bottom') and match.find('div', class_='team-bottom').find('span', class_='score'):
                scoreBottom = match.find('div', class_='team-bottom').find('span', class_='score').contents[0]
            else:
                scoreBottom = 0
		
        team1.append(nameTop)
        team2.append(nameBottom)
        score1.append(scoreTop)
        score2.append(scoreBottom)

    if len(team1) < size - 1:
        return "ERROR: Retry with a smaller bracket size"

    
    team1 = team1[::-1][:(size)][::-1]
    team2 = team2[::-1][:(size)][::-1]
    score1 = score1[::-1][:(size)][::-1]
    score2 = score2[::-1][:(size)][::-1]
    
    if size == 64:
        return generate64SEBracket(team1, team2, score1, score2)
    elif size == 32:
        return generate32SEBracket(team1, team2, score1, score2)
    elif size == 16:
        return generate16SEBracket(team1, team2, score1, score2)
    else:
        return "No result"
