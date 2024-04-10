import socket
from colorama import init, Fore

# colors
init()
RESET = Fore.RESET
LIGHT_GREEN = Fore.LIGHTGREEN_EX
LIGHT_RED = Fore.LIGHTRED_EX

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

host = input("Enter host: ")

for port in range(1, 1025):
	if chk_open_port(host, port):
		print(f"{LIGHT_GREEN}[+] {host}:{port} is open	{RESET}")
	else :
		print(f"{LIGHT_RED}[!] {host}:{port} is closed	{RESET}")