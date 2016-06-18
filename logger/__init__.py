def log(logtype, message):
	if logtype == 1:
		print "[INFO] " , message

	if logtype == 2:
		print "[WARN] " , message

	if logtype == 3:
		print "[FATAL]" , message
		import sys
		sys.exit()
