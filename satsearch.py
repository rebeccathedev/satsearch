import os
import sys
import argparse

def gotox(offset, time):
	os.system("gotox -d " + str(offset) + " -t " + str(time) + " && gotox -d " + str(offset) + " -t " + str(time))

parser = argparse.ArgumentParser(description='Searches for satellites.')
parser.add_argument("satellite")
parser.add_argument("-s", "--start", help="Where to start looking.", default=0, type=float)
parser.add_argument("-e", "--end", help="Where to stop looking.", default=20, type=float)
parser.add_argument("-d", "--direction", help="Which direction (E or W).", default="W")
parser.add_argument("-i", "--increment", help="How much to move each time by.", default=0.1, type=float)

args = parser.parse_args()

if args.direction == "W":
	args.start = args.start * -1
	args.end = args.end * -1

offset=args.start
gotox(offset, 30)
while (offset != args.end):
	print ("Offset ", offset)
	gotox(offset, 5)
	exit = os.system("w_scan -s " + args.satellite + " -f s")

	if exit == 0:
		print(offset)
		sys.exit(0)

	if args.direction == "W":
		offset = round(offset - args.increment, 2)
	else:
		offset = round(offset + args.increment, 2)
