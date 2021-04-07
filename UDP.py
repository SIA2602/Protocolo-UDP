import sys 
import socket

host = '192.168.0.21'
port = 12001
server_address = ('192.168.0.21', 12001)
print("sou o clinete")

file = open("arquivosTest/GRUPO6.txt", "r", encoding="utf-8")
dado = file.read()

mensageOut = ""

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM)

try:
	for i in range(len(dado)):
		mensagem = bytes(dado[i], encoding = "cp850")
		#print(mensagem)
		sock.sendto(mensagem, server_address)
		#print("aqui")

		dados, address = sock.recvfrom(1024)
		#print("aqui")
		mensageOut +=dados.decode('cp850')
		#print('Received:', mensageOut)

finally:
	sock.close()

print('Received:', mensageOut)