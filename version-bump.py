#this is the script
import os
import re
import sys
from optparse import OptionParser
#TODO What happens if writing fails half way through?
#TODO Compare old and new version.txt
p = re.compile('^(\d+\.)?(\d+\.)?(\d+\-SNAPSHOT)$')
foundit = False

# find filename
filename = 'VERSION.txt'
#argv = sys.argv
#print('Argument List:', str(argv))

parser = OptionParser()
parser.add_option("-f", "--file", dest='fname', help='name of the version text file')
(opts, args) = parser.parse_args()
if opts.fname:
    filename = opts.fname
print('Updating version file: '+filename)

       
try:  
    with open(filename, 'r', encoding='utf-8') as v, open('NEW'+filename, 'w', encoding='utf-8') as nv:
        print('write data to '+'NEW'+filename)
        for read_data in v:
            #Check for string matching vesion pattern
            m = p.match(read_data)
            if foundit:
            #Found a match so now just ignore the rest of the file
                nv.write(read_data)
            else:
                if m:
                    newversion=read_data[:-10]
                    nv.write(newversion+'\n')
                    #remove '-SNAPSHOT', don't forget the newline character
                    print('Found version! '+read_data[:-1])
                    print('Changed to '+read_data[:-10])
                    print('now just ignore the rest of the file')
                    foundit = True
                else:
                    #not found a match yet so just ignore line
                    nv.write(read_data)
             
        #delete old file and rename new one
        v.close()
        nv.close()
    
        try:
            os.remove('OLD'+filename)
            print('deleted '+'OLD'+filename)
        except FileNotFoundError:
            print('OLD'+filename+' not found')
            
        os.rename(filename, 'OLD'+filename)
        print('renamed '+filename+' to '+'OLD'+filename)
        os.rename('NEW'+filename, filename)
        print('renamed '+'NEW'+filename+' to '+filename)
except FileNotFoundError:
    print(filename+' not found, no action taken')

    
        
    
