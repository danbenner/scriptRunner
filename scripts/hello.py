import os

path = os.path.abspath("test.txt")
tmpFile = open(path, 'w')
tmpFile.writelines("Hello World...")