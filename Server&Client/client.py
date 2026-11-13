import socket as sck

IP = '127.0.0.1'
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:

    client.connect((IP, PORTA))

    messaggio = input("Inserisci il nome da trasformare: ")

    client.sendall(messaggio.encode('utf-8'))

    risposta = client.recv(1024).decode('utf-8')

    print("Risultato BWT ricevuto dal server:", risposta)