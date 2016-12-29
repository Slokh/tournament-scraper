from challonge import challonge

link = raw_input("Enter the bracket link: ")
link = link.strip()

size = raw_input("Enter the bracket type (16SE, 32SE, 64SE): ")
size = int(size[:2])

if size == 16 or size == 32 or size == 64:
	try:
		print(challonge(link, size))
	except:
		print("Invalid link")
else:
	print("\nERROR: Incorrect bracket type")

