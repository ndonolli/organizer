#!/usr/bin/env python3
import os
from shutil import move

#globals
HOME = os.getcwd() + '/'
ONLYFILES = [f for f in os.listdir(HOME) if os.path.isfile(os.path.join(HOME, f))]
ONLYFILES.remove('organizer.py')
LOGPATH = (HOME + 'OrganizerLog.txt')
MOVED_FILES = []

docs =	[	'.doc',
		'.docx',
		'.pdf',
		'.txt',
		'.pages',
	]

audio =	[	'.mp3',
		'.wav',		
		'.mp4',
		'.ogg',
	]

pics =	[	'.jpg',
		'.jpeg',
		'.tiff',
		'.png',
		'.bmp',
	]

videos =[	'.mov',
		'.mpeg',
		'.mpg',
		'.flv',
		'.avi',
	]

python =[	'.py',
	]

EXT_LIST = {'Documents': docs, 'Audio Files': audio, 'Videos': videos,
			'Pictures': pics, 'Python Scripts': python}

def pathCheck(folder):
# Checks for existing directory, creates new one if it does not exist
	if os.path.exists(HOME + folder):
		pass
	else:
		new_path = os.path.join(HOME + folder)
		os.mkdir(new_path)

def createLog():
# Initiates plaintext log file OrganizerLog.txt in working directory
	f = open(LOGPATH, 'w')
	f.write('Log for files moved by organizer.\n')
	f.write('You may delete this file after sorting.\n\n')
	f.write('=' * 40 + '\n\n')

def log(message):
# Writes log action
	f = open(LOGPATH, 'a')
	f.write(message + '\n')
	f.close()

def logExceptions():
# Prints unmoved files to the log
	exceptions = [] #list of files that were not moved
	for file in ONLYFILES:
		if file not in MOVED_FILES:
			exceptions.append(file)
	print(MOVED_FILES)
	f = open(LOGPATH, 'a')
	f.write('\n The following files were not moved:\n')
	for file in exceptions:
		f.write(file + '\n')
	f.close()

def sort(folder):
# Scans files for known extentions and moves files
	for file in folder:
		if file != 'OrganizerLog.txt':
			ext_start = file.find('.')
			ext = file[ext_start:]
			for filetype in EXT_LIST:
				for ext in EXT_LIST[filetype]:
					if file.lower().endswith(ext):
						pathCheck(filetype)
						move(file, HOME + filetype)
						MOVED_FILES.append(file)
						log('- Moved %s to %s' % (file, (HOME + filetype)))
					else:
						pass
		else:
			pass

def main():
	createLog()
	sort(ONLYFILES)
	logExceptions()

if __name__ == "__main__":
	main()
