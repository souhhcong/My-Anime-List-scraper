import re
import pathlib
import os

from requests import get
from bs4 import BeautifulSoup

PATH = pathlib.Path().absolute()

def get_anime_list():
    for number in range(1,27):          # iterate to
        letter = chr(ord('@')+number)   # next letters
        position = 0
        name_list = []
        while 1:
            URL = "https://myanimelist.net/anime.php?letter=" + letter + '&show=' + str(position)
            #print(URL)
            page_html = get(URL).text
            page = BeautifulSoup(page_html, features="html.parser")
            rows = page.find_all('a', class_="hoverinfo_trigger fw-b fl-l") # parts with the names
            if (len(rows) == 0): # 404 not found
                break
            for r in rows:
                long_name = str(r.find_all('strong')) 
                name = long_name[len('[<strong>'):-len('</strong>]')] + '\n' # extract the name only
                name_list.append(name)
            position += 50 # iterate to next pages
        output = ''.join(name_list)

        newpath = str(PATH) + '/anime_names' # create new directory if not exists
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        with open('anime_names/' + letter + '.txt', 'w', encoding='utf-8') as f:
            print(output, file=f)
        print(letter + ' done\n') # currently can not done all the letters in one batch because MAL restricts heavy access

def get_character_list():
    for number in range(1,27):          # iterate to
        letter = chr(ord('@')+number)   # next letters
        position = 0
        name_list = []
        while 1:
            URL = "https://myanimelist.net/character.php?letter=" + letter + '&show=' + str(position)
            #print(URL)
            page_html = get(URL).text
            page = BeautifulSoup(page_html, features="html.parser")
            rows = page.find_all('td', class_="borderClass bgColor1", width = "175") # parts with the names
            if (len(rows) == 0): # 404 not found
                break
            for r in rows:
                long_name = str(r.find_all('a')) 
                name = re.split('[><]', long_name)[2] + '\n' # regex idk
                #print(name)
                name_list.append(name)
            position += 50 # iterate to next pages
        output = ''.join(name_list)

        newpath = str(PATH) + '/character_names' # create new directory if not exists
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open('character_names/' + letter + '.txt', 'w', encoding='utf-8') as f:
             print(output, file=f)
        print(letter + ' done\n') # currently can not done all the letters in one batch because MAL restricts heavy access
    
if __name__ == "__main__":
    get_character_list()
