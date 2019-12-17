# Metallum Lyrics Tagger 🤘

Metallum Lyrics Tagger is a simple Python script for adding lyrics from Encyclopedia Metallum into your music files. In order for it to work, the artist names, song names and album names, must be configured like in the Metallum.

```
Python >= 3.0
pip for installing dependencies
```

## External dependencies:
 - phrydy
 - lxml
 
All of which can be installed through pip:

```
pip install dependency
```

## Usage:

```
  python get_lyrics.py -dirname <root_directory> [--overwrite]
	
Options:
  
-d  --dir   TEXT    Path to root directory, from where the program will start scanning for music files.
-o  --overwrite OPTIONAL  Optional parameter, add if you want the program to overwrite existing lyrics.
-h  --help                Show this message and exit.
```
