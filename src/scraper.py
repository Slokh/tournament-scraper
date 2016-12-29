from challonge import challonge
from smash import smash

link = raw_input("Enter the bracket link: ")
link = link.strip()

size = raw_input("Enter the bracket type (16SE, 32SE, 64SE): ")
size = int(size[:2])

if size != 16 or size != 32 or size != 64:
	print("\nERROR: Incorrect bracket type")
else:
	print(challonge(link, size))

