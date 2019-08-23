import socket 

ip = '127.0.0.1' #Machine IP - Carbon Coder Software
porta = 1120 #Default Carbon Coder port
 
sck = socket.socket()
sck.connect((ip,porta))

message = "CarbonAPIXML1 158 <?xml version=\"1.0\" encoding=\"UTF-8\"?><cnpsXML TaskType=\"JobCommand\"><JobCommand Command=\"QueryInfo\" GUID=\"{3051C2F8-0501-47DF-8A3B-4A984732814E}\"/></cnpsXML>"
 
sck.send(message.encode("utf-8"))
data = sck.recv(5120).decode()
 
print ('Resposta do Servidor: ' + data)
         
sck.close()

print("Socket closed")

# bia-rodrig