import sys
import socket
from threading import Thread



if len(sys.argv)!= 3:
	print('''Argumentos esperados
	porta file_name''')
	sys.exit(-1)

  
  
HOST = ''              		   # IP do Servidor
port =  int(sys.argv[1])            
file_name = sys.argv[2]




try:
	data = open(file_name,'rb').read()
	datalen = len(data)
	datalen = datalen.to_bytes(length=4, byteorder='big', signed=False)
except Exception as e:
	print(e)
	sys.exit(-1)

  

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, port)
tcp.bind(orig)
tcp.listen()



def iteractionWithClient(con,client):
	global data,datalen
	# envia o arquivo
	con.send(datalen)
	con.send(data)
	# encerra conexao
	con.close()


def acceptClients():
	while True:
		con,client = tcp.accept()
		Thread(target=iteractionWithClient,args=(con,client)).start()

Thread(target=acceptClients,daemon=True).start()



while True:
	x = input()
	if x == 'exit':
		break
	print('Para sair digite: "exit"')
