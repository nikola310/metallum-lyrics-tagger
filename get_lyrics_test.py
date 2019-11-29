'''
Created on Nov 21, 2019

@author: Nikola
'''
from file_handler import FileHandler

directory_list = [#'D:/Музика/Сједињене Америчке Државе/Cobalt', 'D:/Музика/Сједињене Америчке Државе/Possessed',
                  #'D:/Музика/Јапан/Sigh [Discography]', 'D:/Музика/Норвешка/Gorgoroth', 'D:/Музика/Русија/Welicoruss',
                  #'D:/Музика/Русија/Грай', # 
                  #'D:/Музика/Русија/Ак Бүре', 'D:/Музика/Русија/Аркона'
                  'D:/Музика/Немачка/Temple Of Oblivion'
                  # 'D:/Музика/Србија/The Stone'
                  ]

if __name__ == '__main__':
    
    print('Program started')
    
    handler = FileHandler(overwrite_lyrics=True)
    
    for directory in directory_list:
        
        handler.read_files_and_add_lyrics(directory)
        
    print('All lyrics saved.')