import codecs
import hashlib
from bs4 import BeautifulSoup

with codecs.open('urlmap_test.txt', 'r', 'utf-8') as file:
    for line in file:
        path = line.replace('http://', '')
        path = 'html\\' + path.replace('/', '\\')
        soup = BeautifulSoup(codecs.open(path.strip(), 'r', 'utf-8'), 'lxml')

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
                
                print(url)

        

#file1 = BeautifulSoup(codecs.open("C:\\Users\\tam_2\\PageRank-WebIR\\html\\advanse.bus.ku.ac.th\\index.html", encoding='utf-8'), 'lxml')
#file2 = BeautifulSoup(codecs.open("C:\\Users\\tam_2\\PageRank-WebIR\\html\\advanse.bus.ku.ac.th\\index.php", encoding='utf-8'), 'lxml')
#