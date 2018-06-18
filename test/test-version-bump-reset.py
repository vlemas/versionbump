#a script to reset the test file
import os
from optparse import OptionParser

filename = '.\VERSION.txt'
nextversion = '10.345.54-SNAPSHOT'

parser = OptionParser()
parser.add_option("-f", "--file", dest='fname', help='name of the version text file')
parser.add_option("-v", "--version", dest='newversion', help='new version number to be added to the file')
(opts, args) = parser.parse_args()

if opts.fname:
    filename = opts.fname
print('Recreating '+filename+' for version-bump.py')

if opts.newversion:
    nextversion = opts.newversion
print("Using version "+nextversion)

try:
    os.remove(filename)
except FileNotFoundError:
    print('could not find and delete ' + filename + '. Will create new file')

with open(filename, 'w', encoding='utf-8') as v:
    v.write('#a comment\n')
    v.write('\n')
    v.write('#that was a blank space\n')
    v.write('#2.0.6-SNAPSHOT\n')
    v.write('#What to do with this one?\n')
    v.write('<version>10.345.54-SNAPSHOT<\\version>\n')
    if nextversion:
        v.write(nextversion+"\n")
    v.write('11.4.6-SNAPSHOT\n')
    v.write('#THE SCRIPT SHOULD IGNORE THAT ONE\n')
print('done')
    
    
    
