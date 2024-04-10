import socket
from colorama import init, Fore

# colors
init()
BLUE = Fore.BLUE
LIGHT_GREEN = Fore.LIGHTGREEN_EX
MAGENTA = Fore.MAGENTA


def chk_open_port(host, port):
	sckt = socket.socket()
	try:
		# tries to connect to host using that port
		sckt.connect((host, port))
	except:
		# port is closed
		return False
	else:
		# port is opened
		return True

