# This script is to quickly turn the listed publications
# in Eric's CV into HTML formatted links for the 
# publications.html page. It doesn't work that well
# because it grabs the first link from a google search
# of the article title, but it's really helpful if the
# publication.html page is really far behind Eric's CV

# Requires installation of bs4 (BeautifulSoup)  python 
# package to do the web scraping

import requests
from bs4 import BeautifulSoup

def GetLink(query: str = None):
    '''Gets the first Google search link
        for some query. Copied from StackOverflow'''
    search = query
    url = 'https://www.google.com/search'

    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}

    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')

    try:
        return str(first_link['href'])
    except TypeError as e:
        return None


if __name__ == "__main__":
    print_only = False

    # Read in the text file which contains the citations 
    # from Eric's CV
    with open('temp.txt', 'r') as infile:
        lines = infile.read().splitlines()

    # Clean the lines
    new_lines = []
    for line in lines:
        if not line == '':
            new_lines.append(str(line.strip('\n')))

    # Write the formatted html
    if not print_only:
        with open('formatted_publications.txt', 'w') as o:
            for line in new_lines:
                pub_number = int(str(line[:3]).strip())
                search_query = str(line[4:])
                pub = f'{pub_number}) <a href = {GetLink(search_query)}><font color="green"> {line[4:]} </a><br><br></font>'

                o.write(pub)
                o.write('\n')
    else:
        for line in new_lines:
            print(str(line[:3]).strip())
            pub_number = int(str(line[:3]).strip()) - 1
            search_query = str(line[4:])
            pub = f'{pub_number}) <a href = {GetLink(search_query)}><font color="green"> {line[4:]} </a><br><br></font>'

            print(pub, '\n')
