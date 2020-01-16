import os

path = os.path.abspath("test.txt")
tmpFile = open(path, 'a')
tmpFile.writelines("Some New Lines")