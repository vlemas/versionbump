#a script to reset the test file
import os
try:
    os.remove('..\VERSION.txt')
except FileNotFoundError:
    print('File not found')

with open('..\VERSION.txt', 'w') as v:
    v.write('10.345.-SNAPSHOT')
        
    
