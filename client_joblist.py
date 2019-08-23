import socket 

ip = '10.74.153.229' #IP com o software CarbonCoder
porta = 1120
 
sck = socket.socket()
sck.connect((ip,porta))

#Mensagem de Exemplo - pela lista de Jobs
message = "CarbonAPIXML1 68 <?xml version =\"1.0\" encoding=\"UTF-8\"?><cnpsXML TaskType=\"JobList\"/>"
 
sck.send(message.encode("utf-8"))
data = sck.recv(4096).decode()
 
print ('Resposta do Servidor: ' + data)
         
sck.close()

print("socket closed")

# bia-rodrig