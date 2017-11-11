import codecs
import hashlib
from bs4 import BeautifulSoup
#with codecs.open('urlmap.txt', 'r', 'utf-8') as file:
#    for line in file:
#        print(line.strip())

file1 = BeautifulSoup(codecs.open("C:\\Users\\tam_2\\PageRank-WebIR\\html\\advanse.bus.ku.ac.th\\index.html", encoding='utf-8'), 'lxml')
file2 = BeautifulSoup(codecs.open("C:\\Users\\tam_2\\PageRank-WebIR\\html\\advanse.bus.ku.ac.th\\index.php", encoding='utf-8'), 'lxml')

hash_file1 = hashlib.sha224(file1).hexdigest()
hash_file2 = hashlib.sha224(file2).hexdigest()

if(hash_file1 == hash_file2):
    print('Fuck yeahhhhh')

