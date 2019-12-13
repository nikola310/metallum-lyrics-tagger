'''
Created on Nov 21, 2019

@author: Nikola
'''
from file_handler import FileHandler
import sys, getopt

def run_program(root_directory, overwrite_lyrics):
    
    print('Program started')
    
    handler = FileHandler(overwrite_lyrics=overwrite_lyrics)
    
    #for directory in root_directory:
    handler.read_files_and_add_lyrics(root_directory)

    print('All lyrics saved.')


def main(argv):
	root_directory = ''
	overwrite_lyrics = False
	try:
		opts, args = getopt.getopt(argv,"hd:o:",["dir=","overwrite="])
	except getopt.GetoptError:
		print('get_lyrics.py -d <root_directory> -o <overwrite_lyrics>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -d <root_directory> -o <overwrite_lyrics>')
			sys.exit()
		elif opt in ("-d", "--dir"):
			root_directory = arg
		elif opt in ("-o", "--overwrite"):
			overwrite_lyrics = arg
	run_program(root_directory, overwrite_lyrics)


if __name__ == "__main__":
	main(sys.argv[1:])