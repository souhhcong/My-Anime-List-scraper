from requests import get
from bs4 import BeautifulSoup
from string import ascii_uppercase

if __name__ == "__main__":
    for letter in ascii_uppercase: # iterate to consequent letters
        num = 0
        name_list = []
        while 1:
            URL = "https://myanimelist.net/anime.php?letter=" + letter + '&show=' + str(num)
            #print(URL)
            page_html = get(URL).text
            page = BeautifulSoup(page_html, features="html.parser")
            rows = page.find_all('a', class_="hoverinfo_trigger fw-b fl-l")
            if (len(rows) == 0):
                break
            for r in rows:
                long_name = str(r.find_all('strong'))
                name = long_name[len('[<strong>'):-len('</strong>]')] + '\n'
                name_list.append(name)
            num += 50 # iterate to consequent pages
        output = ''.join(name_list)
        with open(letter + '.txt', 'w', encoding='utf-8') as f:
            print(output, file=f)
    #breakpoint()
