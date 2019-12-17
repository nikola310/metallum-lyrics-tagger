'''
Created on Nov 21, 2019

@author: Nikola
'''
from file_handler import FileHandler
import sys, getopt

def run_program(root_directory, overwrite_lyrics):
    
    print('Program started')
    
    handler = FileHandler(overwrite_lyrics=overwrite_lyrics)
    
    handler.read_files_and_add_lyrics(root_directory)

    print('Program finished')

def print_help_message():
	print('Usage:')
	print('\tget_lyrics.py -d <root_directory> [-o]\n')
	print('Options:')
	print('\t-d\t--dir\t\tTEXT\t\tPath to root directory, from where the program will start scanning for music files.')
	print('\t-o\t--overwrite\tOPTIONAL\tOptional parameter, add if you want the program to overwrite existing lyrics.')

def main(argv):
	root_directory = ''
	overwrite_lyrics = False
	try:
		opts, args = getopt.getopt(argv,"hd:o:",["dir=","overwrite="])
		if len(opts) > 0:
			for opt, arg in opts:
				if opt in ('-h', "--help"):
					print_help_message()
					sys.exit()
				elif opt in ("-d", "--dir"):
					root_directory = arg
				elif opt in ("-o", "--overwrite"):
					overwrite_lyrics = True
			
			run_program(root_directory, overwrite_lyrics)
		else:
			print_help_message()
			sys.exit(2)
	except getopt.GetoptError:
		print_help_message()
		sys.exit(2)


if __name__ == "__main__":
	main(sys.argv[1:])