#a script to reset the test file
import os
try:
    os.remove('..\VERSION.txt')
except FileNotFoundError:
    print('File not found')

with open('..\VERSION.txt', 'w', encoding='utf-8') as v:
    v.write('#a comment\n')
    v.write('\n')
    v.write('#that was a blank space\n')
    v.write('#2.0.6-SNAPSHOT\n')
    v.write('#What to do with this one?\n')
    v.write('<version>10.345.54-SNAPSHOT<\\version>\n')
    v.write('10.345.54-SNAPSHOT\n')
    v.write('11.4.6-SNAPSHOT\n')
    v.write('#THE SCRIPT SHOULD IGNORE THAT ONE\n')
    
    
    
