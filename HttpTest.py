import requests
from bs4 import BeautifulSoup

rawurl=''
content = ''

def getcontent(rawurl):
    global content
    url = 'http://'+rawurl+'/'
    content = requests.get(url)
    content.encoding='utf-8'
    return 0

def basic_bsfilter():
    global content
    consoup = BeautifulSoup(content.text)
    print('Choose the Following Options to use the bs4 basic filter')
    print('''
    +---------------------------------------+
    |1.title in string                      |
    |2.paragraph in string                  |
    |3.all the text                         |
    |Other insertion returns the raw content|
    +---------------------------------------+
    ''')
    choice = input('enter the option')
    if choice=='1':
        print(consoup.title.string)
    elif choice=='2':
        print(consoup.p.string)
    elif choice=='3':
        print(consoup.get_text())
    else:
        print(consoup.prettify)
    return 0

while True:
    mchoice = input('1 for change rawurl;\n2 for the reach;\n3 for the filter.\nCurrent url:'+rawurl+'\n')
    if mchoice=='1':
        rawurl = input('enter the domain:\n')
    elif mchoice=='2':
        getcontent(rawurl)
    elif mchoice=='3':
        basic_bsfilter()
