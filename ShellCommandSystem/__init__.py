def command(command):
	if command[0] == "help":
		import module.help
	if command[0] == "print":
		import module.printer
		module.printer.echo(command);
	if command[0] == "stop":
		import sys
		print "Exiting..."
		sys.exit();
