import logger;
logger.log(1, "Imported logger Module");
import time
logger.log(1, "Imported time Module");
import ShellCommandSystem
logger.log(1, "Imported ShellCommandSystem Module");
logger.log(2, "Starting Shell...");
while True:
<<<<<<< HEAD
	command = raw_input("> ").split()
=======
	command = raw_input("> ");
>>>>>>> 6bcd0db48784ffc7660219f9c9e0b73251bd2946
	ShellCommandSystem.command(command);
