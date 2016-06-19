import logger;
logger.log(1, "Imported logger Module");
import os;
logger.log(1, "Imported os Module");
import errorsys;
logger.log(1, "Imported errorsys Module");
import time
logger.log(1, "Imported time Module");
import ShellCommandSystem
logger.log(1, "Imported ShellCommandSystem Module");
logger.log(2, "Starting Shell...");
while True:
	directory = os.getcwd()
	dir2 = directory + "> "
	command = raw_input(dir2).split()
	error = ShellCommandSystem.command(command);
	errorsys.err(error);
