# copytree
Python util to copy files from one directory tree to another, with regex

This python utility copies files that match a regular expression from one directory tree into another.
Normally, Linux tools such as rsync are sufficient for this, but for some reason, I was getting directory
and or file creation errors. With this utility I was able to successfuly copy parts of a very large directory
tree into another one.
