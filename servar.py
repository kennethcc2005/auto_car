import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('www.google.com')
mysocket.connect(host,80)
