import urllib.request
from bs4 import BeautifulSoup

def get_member_since(username):
    
    url = 'https://www.codewars.com/users/' + username
    page = urllib.request.urlopen(url).read().decode(encoding='utf8', errors='ignore')
    soup = BeautifulSoup(page, 'html.parser')  # or use 'lmxl'
    b = soup.find('b', text='Member Since:')  # find appropriate <b> tag
    return b.next_sibling  # Gets text (the next node) after that <b> tag

get_member_since('jhoffner')