'''
Created on Nov 22, 2019

@author: Nikola
'''

import requests
from html.parser import HTMLParser
import lxml.html as lh
from lyrics_getter import LyricsGetter, NoLyricsException, LyricsNotAvailable
import urllib.parse
import re


class MetallumLyricsGetter(LyricsGetter):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        self._metallum_url = 'https://www.metal-archives.com/'
        self._search_songs_url = 'search/ajax-advanced/searching/songs?'
        self._song_title_url = 'songTitle='
        self._exact_song_match_url = 'exactSongMatch=1'
        self._band_name_url = 'bandName='
        self._release_title_url = 'releaseTitle='
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
                        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.5',
                        # 'Connection': 'keep-alive',
                        'Host': 'www.metal-archives.com',
                        'Upgrade-Insecure-Requests': '1'
                         }
        self._data_key = 'aaData'
        self._html_parser = HTMLParser()
        self._lyrics_url = 'https://www.metal-archives.com/release/ajax-view-lyrics/id/'
        self._lyrics_not_available = 'lyrics not available'
        self._html_regex = re.compile(r'<[^>]+>')
        
    def get_lyrics(self, artist, release, song):

        search_url = self._build_search_url(artist, release, song)
        # print(search_url)
        response = requests.get(search_url, headers=self._headers)
        response_dict = response.json()
        lyrics = self._find_lyrics(response_dict[self._data_key])
            
        return lyrics
        
    def _find_lyrics(self, data):
        
        if len(data) > 0:
            for i in range(len(data)):
                result = data[i]
                if len(result) >= 5:
                    tree = lh.fromstring(result[4])
    
                    a_tag = tree.xpath('//a')
                    lyrics_id = a_tag[0].get('id').split('_')[1]
                    
                    lyrics_response = requests.get("".join([self._lyrics_url, lyrics_id]), headers=self._headers)
                    try:
                        lyrics_text = self._parse_raw_lyrics(lyrics_response.content)
                        
                        return lyrics_text
                    except LyricsNotAvailable:
                        print('Lyrics are unavailable, trying next link.')
        
        raise NoLyricsException()
        
    def _build_search_url(self, artist, release, song):
        '''
            Example: https://www.metal-archives.com/search/ajax-advanced/searching/songs/?songTitle=Black+Metal&bandName=Venom&releaseTitle=Black+Metal&sEcho=1&iColumns=5&sColumns=&iDisplayStart=0&iDisplayLength=200&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&_=1574460194700
        '''
        song_title = urllib.parse.quote(song)
        release_title = urllib.parse.quote(release)
        band_name = urllib.parse.quote(artist)
        return "".join([self._metallum_url, self._search_songs_url, self._song_title_url, song_title, '&', self._band_name_url, band_name, '&', self._release_title_url, release_title])

    def _parse_raw_lyrics(self, lyrics):
        
        decoded_lyrics = lyrics.decode('utf-8')
        
        if self._lyrics_not_available in decoded_lyrics:
            raise LyricsNotAvailable()
        
        lyrics_without_html_tags = self._html_regex.sub('', decoded_lyrics)
        #lyrics_without_br_tags = decoded_lyrics.replace('<br />', '')
        return lyrics_without_html_tags.strip() #lyrics_without_br_tags.strip()
    
    