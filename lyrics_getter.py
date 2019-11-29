'''
Created on Nov 22, 2019

@author: Nikola
'''

from abc import ABC, abstractmethod

class LyricsGetter(ABC):
    '''
    classdocs
    '''

    @abstractmethod
    def get_lyrics(self, artist, release, song):
        pass
    
    
class NoLyricsException(Exception):
    '''
        Raised when there are no lyrics found
    '''

    pass

class LyricsNotAvailable(Exception):
    '''
        Raised when lyrics for given song are not available
    '''
    
    pass