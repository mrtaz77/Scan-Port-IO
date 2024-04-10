import socket
from colorama import init, Fore

import argparse
from threading import Thread, Lock
from queue import Queue

# colors
init()
RESET = Fore.RESET
LIGHT_GREEN = Fore.LIGHTGREEN_EX
LIGHT_RED = Fore.LIGHTRED_EX

number_of_threads = 200
threads = Queue()
print_lock = Lock()

def port_scan(port):
	sckt = socket.socket()
	try:
		# tries to connect to host using that port
		sckt.connect((host, port))
	except:
		# port is closed
		with print_lock:
			print(f"{LIGHT_RED}[!] {host}:{port} is closed	{RESET}")
	else:
		# port is opened
		with print_lock:
			print(f"{LIGHT_GREEN}[+] {host}:{port} is open	{RESET}")
	finally:
		sckt.close()

def scan_thread():
	global threads
	while True:
		port_no = threads.get()
		port_scan(port_no)
		# tells the queue that the scanning for that port is done
		threads.task_done()

def main(host, ports):
	global threads
	for thread in range(number_of_threads):
		thread = Thread(target = scan_thread)
		# when we set daemon to true, that thread will end when the main thread ends
		thread.daemon = True
		thread.start()

	for port in ports:
		threads.put(port)

	threads.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Scan Port IO")
    parser.add_argument("host", help = "Host to Scan.")
    parser.add_argument("--ports", "-p", dest = "port_range", default = "1-65535", help = "Port range to scan, default is 1-65535 (all ports)" )
    arguments = parser.parse_args()
    host, port_range = arguments.host, arguments.port_range
    
    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)
    
    ports = [ p for p in range(start_port, end_port)]
    
    print(host, start_port, end_port)

    main(host, ports)