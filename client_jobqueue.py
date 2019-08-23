import socket 

ip = '127.0.0.1' #Machine IP - Carbon Coder Software
porta = 1120 #Default Carbon Coder port
 
sck = socket.socket()
sck.connect((ip,porta))

message = "CarbonAPIXML1 342 <?xml version=\"1.0\" encoding =\"UTF-8\"?><cnpsXML TaskType=\"JobQueue\"><Sources><Module_0 Filename=\"D:\\mediamano\\Inbox\\TesteLabBianca.mp4\"/></Sources><Destinations><Module_0 PresetGUID=\"{A9715B80-9552-49AF-87EE-590B513B2AAC}\"><ModuleData CML_P_BaseFileName=\"TesteLabBianca3\" CML_P_Path=\"d:\\mediamano\\outbox\"/></Module_0></Destinations></cnpsXML>"
 
sck.send(message.encode("utf-8"))
data = sck.recv(2048).decode()
 
print ('Resposta do Servidor: ' + data)
         
sck.close()

print("Socket closed")

# bia-rodrig