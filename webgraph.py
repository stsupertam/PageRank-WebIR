import codecs
import hashlib
from bs4 import BeautifulSoup

def getFullUrl(line, soup):
    url_list = []
    line = line.replace('http://', '').split('/')
    line.pop(len(line) - 1)
    line = str.join('/', line)

    for tag in soup.findAll('a', href=True):
        if(tag['href'] != '#'):
            url = tag['href'].replace('://', '/').replace('https', 'http')
            url = url.split('/')
            if(url[0] != 'http'):
                i = 0
                for item in url:
                    if(item == '' or item == '.' or item == '..'):
                        url.pop(i)
                        i += 1
                    else:
                        break
                url = 'http://' + line + '/' + str.join('/', url)
            else:
                url = str.join('/', url).replace('http/', 'http://')
            if(url[-1] == '/'):
                url = url + 'index.html'
            url_list.append(url)

    return url_list


with codecs.open('urlmap.txt', 'r', 'utf-8') as file:
    url_list = file.read().splitlines()

i = 0
with open('webgraph.txt', 'w') as file:
    for line in url_list:
        path = line.replace('http://', '')
        path = 'html\\' + path.replace('/', '\\')
        soup = BeautifulSoup(codecs.open(path.strip(), 'r', 'utf-8'), 'lxml')

        urls = getFullUrl(line, soup)
        links = []
        for url in urls:
            try:
                if(url_list.index(url) not in links and url != line):
                    links.append(url_list.index(url))
            except ValueError:
                pass

        if(len(links) != 0):
            text = ",".join(map(str, links))
        else:
            text = '-'
        file.write(text + '\n')

        print(' \rProcess File :%d/%d' % (i, len(url_list)), end = '',flush=False)
        i += 1


