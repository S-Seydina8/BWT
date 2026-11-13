import socket as sck
IP = '127.0.0.1'
PORTA = 5000

message=input("messaggio da inviare: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect((IP, PORTA))
    client.sendall(message.encode('utf-8'))
    dati=client.recv(1024)
    print("messaggiuo ricevuto dal server", dati.decode)