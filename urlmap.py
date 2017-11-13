import re
import os
import glob
import codecs


def urlmap(file, output):
    with codecs.open(output, 'w', 'utf-8') as urlmap:
        for filename in glob.iglob(file, recursive=True):
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
                    urlmap.write('http://' + url + '\n')


if __name__=='__main__':
    file_reg = 'html/**/*.*'
    output = 'urlmap.txt'
    urlmap(file_reg, output)

