import os
import sys

#give the path you want to look
#example a.py <path tree> <file output hasil>
path = sys.argv[1]
fname =[]

#get all  tree directories and file name
for root, d_names, f_names in os.walk(path):
        for f in f_names:
                fname.append(os.path.join(root,f))
# read files on list
f = open (sys.argv[2], 'a')
for i in fname:
        ini= open(i, 'r').read()
        print ini
        f.write(ini)
