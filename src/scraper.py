import os
import sys

from battlefy import battlefy
from challonge import challonge
from gfinity import gfinity
from smash import smash

def battlefyBracket():
	if size == 16 or size == 32 or size == 64:
		try:
		    printToFile(battlefy(link, size))
		except:
			print("ERROR: Invalid link")
	else:
		print("\nERROR: Incorrect bracket type")

def challongeBracket():
	if size == 16 or size == 32 or size == 64:
		try:
			printToFile(challonge(link, size))
		except:
			print("ERROR: Invalid link")
	else:
		print("\nERROR: Incorrect bracket type")

def gfinityBracket():
	if size == 16 or size == 32 or size == 64:
		try:
		    printToFile(gfinity(link, size))
		except:
			print("ERROR: Invalid link")
	else:
		print("\nERROR: Incorrect bracket type")

def smashBracket():
	if size == 16 or size == 32 or size == 64:
		try:
		    printToFile(smash(link, size))
		except:
			print("ERROR: Invalid link")
	else:
		print("\nERROR: Incorrect bracket type")
		
def printToFile(result):
    dir = os.path.dirname(os.path.realpath(__file__))
    file = open(dir+"/../data/bracket.txt", "w")
    file.write(result)
    file.close()

host = raw_input("Enter the host ([b]attlefy, [c]hallonge, [g]finity, [s]mash.gg): ")

link = raw_input("Enter the bracket link: ")
link = link.strip()

size = raw_input("Enter the bracket type (16SE, 32SE, 64SE): ")
size = int(size[:2])

if host[:1] == 'b' or host[:1] == 'B':
	battlefyBracket()
elif host[:1] == 'c' or host[:1] == 'C':
	challongeBracket()
elif host[:1] == 'g' or host[:1] == 'G':
	gfinityBracket()
elif host[:1] == 's' or host[:1] == 'S':
	smashBracket()
else:
	print("ERROR: Hosting site not found")
