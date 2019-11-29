'''
Created on Nov 21, 2019

@author: Nikola
'''
import unittest
from file_handler import FileHandler
from phrydy import MediaFile

class TestFileHandler(unittest.TestCase):


    def test_has_lyrics(self):
        handler = FileHandler()
        file_with_lyrics = MediaFile('./test_files/01 - Magla.mp3')
        file_without_lyrics =  MediaFile('./test_files/01. U Smrti Zatečen.mp3')
        self.assertTrue(handler._has_lyrics(file_with_lyrics))
        self.assertFalse(handler._has_lyrics(file_without_lyrics))    

if __name__ == "__main__":
    unittest.main()
