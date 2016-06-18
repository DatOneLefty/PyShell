def command(command):
	if not command:
		return 1
	if command[0] == "help":
		import module.help
		return 0
	elif command[0] == "print":
		import module.printer
		module.printer.echo(command);
		return 0
	elif command[0] == "stop":
		import sys
		print "Exiting..."
		sys.exit();
		return 0
	elif command[0] == "info":
		import module.info
		return 0
	else:
		return 2
			
