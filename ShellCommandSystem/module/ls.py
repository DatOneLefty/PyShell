import os
def ls(directory):
	clist = os.listdir(directory)
	print ' '.join(clist)
