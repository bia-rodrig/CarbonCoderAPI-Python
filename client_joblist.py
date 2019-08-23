import socket 

ip = '127.0.0.1' #Machine IP - Carbon Coder Software
porta = 1120 #Default Carbon Coder port
 
sck = socket.socket()
sck.connect((ip,porta))

message = "CarbonAPIXML1 68 <?xml version =\"1.0\" encoding=\"UTF-8\"?><cnpsXML TaskType=\"JobList\"/>"
 
sck.send(message.encode("utf-8"))
data = sck.recv(4096).decode()
 
print ('Resposta do Servidor: ' + data)
         
sck.close()

print("socket closed")

# bia-rodrig