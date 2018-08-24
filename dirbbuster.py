import argparse
import os
from random import randint
from shutil import copy


parser = argparse.ArgumentParser(prog="DirbBuster.py", description="Detection system for web application directiories listing.")

parser.add_argument('directory', help='Target directory where the bait directories are gonna be created.')
parser.add_argument('-w', '--wordlist', help='Specific path to the wordlist where the names of directories are gonna be randomly selected. Default is Dirb\'s default wordlist, common.txt at /usr/share/wordlists/dirb/common.txt.', nargs=1, dest='wordlist', default='common.txt', required=False)
parser.add_argument('-l', '--lines', help='Number of lines to be randomly selected from the wordlist file.', nargs=1, dest='lines', default=['3'], required=False)
parser.add_argument('-s', '--source', help='Specific path to the source code intended to show on the files inside the bait directories.', nargs=1, dest='source', default="sources/index.php", required=False)

args = parser.parse_args()

if args.directory.endswith("/") == False:
	args.directory = args.directory + "/"


def banner():
	print('Amazing script title with 1337 ascii art.\n')

def getRandomLines(wordlist, num):
	if os.path.isfile(wordlist) == False:
		print('[-] Received wordlist does not exist, dying.')
		exit()

	f = open(wordlist).read().splitlines()
	lines={}

	for x in range(0,int(num)):
		lines[x] = f[randint(0,len(f) - 1)]

	return lines

def populate(dir):
	copy(args.source, args.directory + dir)

def main(args):
	banner()
	print('Testing received directory...')

	if os.path.isdir(args.directory) == True:
		print('[+] We are good to go.')
	else:
		print('[-] The received directory is not available, dying.')
		exit()

	print('\nSelecting random directories...')

	verified=int(args.lines[0])
	while verified != 0:
		verified=int(args.lines[0])
		directories = getRandomLines(args.wordlist, args.lines[0])

		for d in directories:
			if os.path.exists(args.directory + directories[d]) == True:
				print('Randomly selected directory already exists, selecting new ones.')
				break
			else:
				verified = verified - 1

	print('[+] %s directories selected, creating...' % args.lines[0])

	for d in directories:
		try:
			os.makedirs(args.directory + directories[d])
			print('[+] Successfully created ' + directories[d])
			populate(directories[d])
			print('[+]	 ' + directories[d] + ' propulated with bait script.')
		except Exception as e:
			print("Error: $s" % e)
			exit()

if __name__ == "__main__":
	main(args)

