#this is the script
import os
import re
#TODO What happens if writing fails half way through?
#TODO Compare old and new version.txt
p = re.compile('^(\d+\.)?(\d+\.)?(\d+\-SNAPSHOT)$')
foundit = False
with open('VERSION.txt', 'r', encoding='utf-8') as v, open('NEWVERSION.txt', 'w', encoding='utf-8') as nv:
    for read_data in v:
        #Check for string matching vesion pattern
        m = p.match(read_data)
        #check for '-SNAPSHOT' and remove, don't forget the newline character
        if foundit:

            print('write the rest: ' + read_data)
            nv.write(read_data)
        else:
            if m:
                print('found it: ' + read_data)
                nv.write(read_data[:-10]+'\n')
                print('now just ignore the rest of the file')
                foundit = True
            else:
                print('not here: ' + read_data)
                nv.write(read_data)
        #Found a match so now just ignore the rest of the file
         
    #delete old file and rename new one
    v.close()
    nv.close()
    try:
        os.remove('OLDVERSION.txt')
    except FileNotFoundError:
        print('OLDVERSION.txt not found')
        
    os.rename('VERSION.txt', 'OLDVERSION.txt')
    os.rename('NEWVERSION.txt', 'VERSION.txt')

    
        
    
