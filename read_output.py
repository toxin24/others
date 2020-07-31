import os
import sys

#give the path you want to look
#example read_output.py <path tree> <file output hasil>
path = sys.argv[1]
output1 = str("{}/{}_files.txt".format(os.getcwd(),sys.argv[2]))
output2 = str("{}/{}_directories.txt".format(os.getcwd(),sys.argv[2]))
fi = open (output1,'a')
h = open(output2,'a')
fname =[]
fdir = []
#get all  tree directories and file name also save any thing in the files
for root,d_names, f_names in os.walk(path):
	for f in f_names:
		fname.append(os.path.join(root,f))
print ("list files")
for i in fname:
	ini= open(i, 'r').read()
	fi.write(i+ "\n"+ini)
	print (i)
# read directories  and save it 
print ("list directories")
for dirpath, dirs, files in os.walk(path):
	print (dirpath)
	fdir.append(dirpath)
for s in fdir:
	h.write(s+"\n")
