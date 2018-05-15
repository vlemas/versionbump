#this is the script
import os
import re

p = re.compile('^(\d+\.)?(\d+\.)?(\d+\-SNAPSHOT)$')
with open('VERSION.txt', 'r') as v, open('NEWVERSION.txt', 'w') as nv:
    read_data = v.readline()
    #Check for string matching vesion pattern
    m = p.match(read_data)
    #check for '-SNAPSHOT' and remove
    #if (read_data.endswith('-SNAPSHOT')):
    if m:
        print('found it: ' + read_data)
        nv.write(read_data[:-9])
    else:
        print('not here: ' + read_data)
    #delete old file and rename new one
    v.close()
    nv.close()
    os.remove('VERSION.txt')
    os.rename('NEWVERSION.txt', 'VERSION.txt')
        
    
