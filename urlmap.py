import re
import glob
import codecs

with codecs.open('urlmap.txt', 'w', 'utf-8') as file:
    for filename in glob.iglob('html/**/*.*', recursive=True):
        if re.match('.*\.html$|.*\.htm$|.*\.php$|.*\.asp$|.*\.aspx$|.*\.pl$|.*\.jsp$|.*\.jsf$', filename):
            filename = filename.split('\\')[1:]
            filename = str.join('/', filename)
            file.write(filename + '\n')
