import socket
import json


def invio_dati(dati, ip):
    #connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,1238))

    #trasformo in oggetto json


    # invio dati
    s.send(bytes("#123abc", "utf-8"))
    s.send(bytes(dati, "utf-8"))


    #messaggio per connesione riuscita
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
