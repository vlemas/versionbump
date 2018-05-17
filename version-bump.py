#this is the script
import os
import re
import sys
from optparse import OptionParser
#TODO What happens if writing fails half way through?
#TODO Compare old and new version.txt
 
p = re.compile('^(\d+\.)?(\d+\.)?(\d+\-SNAPSHOT)$')
np = re.compile('^(\d+\.)?(\d+\.)?(\d+)?(\-SNAPSHOT)?$')
# find filename
filename = 'VERSION.txt'

def updateFile(filename, version):
    foundit = False
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
                        print('Found version in file! '+read_data[:-1])
                        newversion=read_data[:-10]
                        #remove '-SNAPSHOT', don't forget the newline character
                        print('Changed to '+newversion)
                        if version:
                            print('New version in file: '+version)
                            nv.write(version+'\n')
                        else:
                            print('New version in file: '+newversion)
                            nv.write(newversion+'\n')
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



#argv = sys.argv
#print('Argument List:', str(argv))

parser = OptionParser()
parser.add_option("-f", "--file", dest='fname', help='name of the version text file')
parser.add_option("-v", "--version", dest='version', help='new version number to be added to the file')
(opts, args) = parser.parse_args()
if opts.fname:
    filename = opts.fname
print('Updating version file: '+filename)
specifiedversion = None
if opts.version:
    specifiedversion = opts.version
    if np.match(specifiedversion):
        print('Updating version file with version '+specifiedversion)
        updateFile(filename, specifiedversion)
    else:
        print(specifiedversion+' is not a valid version, no action taken')
        #HOW DO I GET OUT FROM HERE
else:
    updateFile(filename, specifiedversion)
 
