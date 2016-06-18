import logger;
logger.log(1, "Imported logger Module");
import time
logger.log(1, "Imported time Module");
import ShellCommandSystem
logger.log(1, "Imported ShellCommandSystem Module");
logger.log(2, "Starting Shell...");
while True:
	command = raw_input("> ").split()
	ShellCommandSystem.command(command);
