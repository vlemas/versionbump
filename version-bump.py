#this is the script
import os
import re
import sys
import subprocess
from optparse import OptionParser
#TODO What happens if writing fails half way through?
#TODO Compare old and new version.txt
 
p = re.compile('^(\d+\.)?(\d+\.)?(\d+\-SNAPSHOT)$')
np = re.compile('^(\d+\.)?(\d+\.)?(\d+)?(\-SNAPSHOT)?$')
# find filename
filename = 'VERSION.txt'

class GitError(Exception):
    def _init_(self, errorCode, message):
        print("GitError " + str(message))

def findFile(filename):
    #read all files in directory
    print("Checking that "+filename+" exists")
    lcfilename = filename.lower()
    allfiles = os.listdir()
    
    for afile in allfiles:
        if lcfilename == afile.lower():
            return afile
    print("Oops "+filename+"  does not exist")
    raise FileNotFoundError("filename")

        
def updateFile(uncasedfilename, nextversion):
    foundit = False
    tagversion = None
    try:
        filename = findFile(uncasedfilename)
        with open(filename, 'r', encoding='utf-8') as v, open('NEW'+filename, 'w', encoding='utf-8') as nv:
            print('write data to '+'NEW'+filename)
            for read_data in v:
                #Check for string matching vesion pattern
                m = p.match(read_data)
                if foundit:
                #Found a match so now just ignore the rest of the file
                    nv.write(read_data)
                else:
                    #TODO What if no version in file yet?
                    if m:
                        print('Found version in file! '+read_data[:-1])
                        tagversion=read_data[:-10]
                        #remove '-SNAPSHOT', don't forget the newline character
                        print('Changed to '+tagversion)
                        if nextversion:
                            print('New version added to file: '+nextversion)
                            nv.write(nextversion+'\n')
                        else:
                            print('Version not updated in file')
                            #nv.write(newversion+'\n')
                        print('now just ignore the rest of the file')
                        foundit = True
                    else:
                        #not found a match yet so just ignore line
                        nv.write(read_data)
                 
            #delete old file and rename new one
            v.close()
            nv.close()
            #now create Git tag, if sucessful delete old file and rename new one
            #if it fails rename old file and delete new
            try:
                createTag(tagversion)
                try:
                    os.remove('OLD'+filename)
                    print('deleted '+'OLD'+filename)
                except FileNotFoundError:
                    print('OLD'+filename+' not found')
                    
                os.rename(filename, 'OLD'+filename)
                print('renamed '+filename+' to '+'OLD'+filename)
                os.rename('NEW'+filename, filename)
                print('renamed '+'NEW'+filename+' to '+filename)
            except GitError:
                #TODO Git failed, rollback
                print("Git Failed, rolling back "+filename)
                try:
                    os.remove('NEW'+filename)
                    print('deleted '+'NEW'+filename)
                except FileNotFoundError:
                    print('NEW'+filename+' not found')
             
    except FileNotFoundError:
        print(filename+' not found, no action taken')
    #return newversion

def createTag(version):
    # Create a Git tag and commit it then push it to the server
    # git tag -a version -m "Automatic tag created by version-bump."
    # git push --tags
    print("Creating a new tag in Git")
    response = subprocess.run(["git", "tag", "-a", version, "-m", "Automatic tag created by version-bump."],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("response: "+str(response.returncode))
    print("output: "+str(response.stdout))
    if response.returncode != 0:
        print("Git Tag failed!! " + str(response.stdout))
        raise GitError(str(response.stdout))
    else:
        #push the tag to the server
        print("Pushing the tag to the server")
        response = subprocess.run(["git", "push", "--tags"],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("response: "+str(response.returncode))
        print("output: "+str(response.stdout))
        if response.returncode != 0:
            print("Git push failed!! " + str(response.stdout))
            raise GitError(str(response.stdout))
    
#argv = sys.argv
#print('Argument List:', str(argv))

    
parser = OptionParser()
parser.add_option("-f", "--file", dest='fname', help='name of the version text file')
parser.add_option("-v", "--version", dest='newversion', help='new version number to be added to the file')
(opts, args) = parser.parse_args()
if opts.fname:
    filename = opts.fname
print('Updating version file: '+filename)

nextversion = None

if opts.newversion:
    nextversion = opts.newversion
    if np.match(nextversion):
        print('Updating version file with version '+nextversion)
        updateFile(filename, nextversion)
    else:
        print(nextversion+' is not a valid version, no action taken')
        #HOW DO I GET OUT FROM HERE
else:
    #new version not supplied, prompt for it
    invalidVersion = True
    while invalidVersion:
        inputversion = input('Please provide a new version, format <major>.<minor>.<patch>-SNAPSHOT')
        if p.match(inputversion):
            print('Updating version file with version '+inputversion)
            invalidVersion = False
            nextversion = inputversion
        else:
            print('new version is not in the correct format')
            
    updateFile(filename, nextversion)
#print("version used is "+finalversion)
 
