def command(command):
	if command[0] == "help":
		import module.help
	if command[0] == "print":
		import module.printer
		module.printer.echo(command);
