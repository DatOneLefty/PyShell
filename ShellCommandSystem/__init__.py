def command(command):
	if command[0] == "help":
		import module.help
	else if command[0] == "print":
		import module.printer
		module.printer.echo(command);
	else if command[0] == "stop":
		import sys
		print "Exiting..."
		sys.exit();
	else if command[0] == "info":
		import module.info
	else:
		print "Command not found"
			
