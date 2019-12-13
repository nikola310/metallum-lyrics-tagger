'''
Created on Nov 21, 2019

@author: Nikola
'''

import os
from phrydy import MediaFile
from phrydy.mediafile import FileTypeError
from metallum_lyrics_getter import MetallumLyricsGetter
from lyrics_getter import NoLyricsException

class FileHandler(object):
    '''
    classdocs
    '''


    def __init__(self, overwrite_lyrics=False):
        '''
            Constructor
        '''
        self._lyrics = 'lyrics'
        self._lyrics_getter = MetallumLyricsGetter()
        self._overwrite_lyrics = overwrite_lyrics
        self._supported_files = ['.mp3', '.m4a', 'mp3', '.aac', '.alac', '.ogg', '.opus', '.flac', '.ape', '.wv', '.mpc', '.asf', '.aiff', '.dsf']
        
    def read_files_and_add_lyrics(self, root_directory):
        for root, _, files in os.walk(root_directory, topdown=False):
            for name in files:
                if self._is_music_file(name): #name.endswith('.mp3'):
                    try:
                        mp3_file = MediaFile(os.path.join(root, name))
                        if self._has_lyrics(mp3_file):
                            if self._overwrite_lyrics:
                                self._get_lyrics_and_save_file(mp3_file)
                            else:
                                print('Skipping since there are already lyrics for', mp3_file.title)
                        else:
                            self._get_lyrics_and_save_file(mp3_file)
                        
                    except FileTypeError:
                        print('Unsupported file', name)
                    except TypeError:
                        print('Moving on, since tags are not formatted correctly for', name)
                    
                        
    def _has_lyrics(self, file):
        has_lyrics = False
        if file.lyrics is not None:
            if str(file.lyrics) != '':
                has_lyrics = True

        return has_lyrics

    def _is_music_file(self, name):
        for file_type in self._supported_files:
            if name.endswith(file_type):
                return True
        return False
        
    def _get_lyrics_and_save_file(self, file):
        
        try: 
            lyrics = self._lyrics_getter.get_lyrics(file.artist, file.album, file.title)
            
            file.lyrics = lyrics
            file.save()
            print('Saved lyrics for', file.title)
                            
        except NoLyricsException:
            print('No lyrics found for', file.title)
        