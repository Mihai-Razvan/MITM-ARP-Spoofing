import socket
import logging
import time
import random

logging.basicConfig(format=u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

port = 10000
adresa = '198.7.0.2'   #adresa serverului
server_address = (adresa, port)

try:
    logging.info('Handshake cu %s', str(server_address))
    sock.connect(server_address)
    while True:
        mesaj = str(random.randint(1, 100))  # Generate a random message
        sock.send(mesaj.encode('utf-8'))  # Send the message
        time.sleep(1)  # Wait for 1 second
        data = sock.recv(1024)
        logging.info('Content primit: "%s"', data)

finally:
    logging.info('closing socket')
    sock.close()
