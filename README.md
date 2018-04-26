# versionbump

`version-bump.py` is a Python 3 script to increment a
[Maven Snapshot model](https://stackoverflow.com/questions/5901378/what-exactly-is-a-maven-snapshot-and-why-do-we-need-it)
VERSION.txt file that it [semantically versioned](https://semver.org/). creating a git tag for the release version along the way.

Specifically the script will:

 1. Bump the version number from a SNAPSHOT to equivalent release (e.g. from `2.4.4-SNAPSHOT` to `2.4.4`)
 1. Commit a tag with the release version number to git
 1. Prompt for the new version number, and update the VERSION.txt file with it
 
 Note:
 
  * The `VERSION.txt` file must already be part of a git repo.
  * The `version-bump.py` script must be in the repo's directory.
  * The script is case insensitive to the `version.txt` filename
  * The file must be utf-8
  * Lines starting with a `#` character will be ignored
  * The first line with a version matching the semantic versioning pattern is taken to be the version
  * The script will output to stdout a basic overview of the operations it has performed
  * If there is an error, the script will exit with a non-zero return code
  * An alternative filename for the version file can be specified with the `-f <filename>` parameter