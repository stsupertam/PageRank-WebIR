import re
import os
import glob
import codecs


with codecs.open('urlmap.txt', 'w', 'utf-8') as urlmap:
    for filename in glob.iglob('html/**/*.*', recursive=True):
        if re.match('.*\.html$|.*\.htm$|.*\.php$|.*\.asp$|.*\.aspx$|.*\.pl$|.*\.jsp$|.*\.jsf$', filename):
            if(not os.path.isdir(filename)):
                filename_split = filename.split('\\')
                name = filename_split[-1]
                folder = filename_split[0:len(filename_split) - 1]
                if(name == 'index.html'):
                    for file in os.listdir(str.join('\\', folder)):
                        extension = file.split('.')[-1]
                        if(extension == 'php' or extension == 'asp'):
                            continue
                url = filename_split[1:]
                url = str.join('/', url)
                urlmap.write(url + '\n')
