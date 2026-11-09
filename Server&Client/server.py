import socket as sck
IP = '127.0.0.1'
PORTA = 5000

Seydina = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as Seydina:

    Seydina.bind((IP, PORTA))

    Seydina.listen(5) # numero massimo delle richieste nella stessa rete
    conn, add=Seydina.accept()

    print("socket di ascolto: ", Seydina.getsockname())
    print("socket di ascolto: ", conn.getsockname())

    dati=conn.recv(1024) # un numero di massimo di byte che andiamo leggere per chiamata

    print("Dati ricevuto dal client ", dati.decode())

    conn.sendall(dati)
    conn.close()
    Seydina.close()
