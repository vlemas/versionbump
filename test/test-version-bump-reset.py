#a script to reset the test file
import os
filename = '.\VERSIONsss.txt'
print('Recreating '+filename+' for version-bump.py')
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
    v.write('10.345.54-SNAPSHOT\n')
    v.write('11.4.6-SNAPSHOT\n')
    v.write('#THE SCRIPT SHOULD IGNORE THAT ONE\n')
print('done')
    
    
    
