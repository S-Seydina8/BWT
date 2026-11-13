import sys
import os
import socket as sck

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import BWT_executor

IP = '127.0.0.1'
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:

    server.bind((IP, PORTA))
    server.listen(5)

    print(f"Server BWT in ascolto su {IP}:{PORTA}...")

    conn, add = server.accept()

    with conn:

        print("Connesso con:", add)

        dati = conn.recv(1024)

        messaggio = dati.decode('utf-8')

        print("Nome ricevuto dal client:", messaggio)

        # Esecuzione della logica BWT
        risposta = BWT_executor.esegui_bwt(messaggio)

        print("Risultato BWT:", risposta)

        # Invio del risultato al client
        conn.sendall(risposta.encode('utf-8'))