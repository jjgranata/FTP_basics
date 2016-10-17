import socket

socks = socket.socket()
hosts = socket.gethostname()
ports = 60000

socks.connect((hosts, ports))
socks.send("Test")

with open('received', 'wb') as file:
    print('open')

    while True:
        print('receiving data...')
        chunks = socks.recv(1024)
        print('data=%s', chunks)
        if not chunks:
            break

        file.write(chunks)

file.close()
print('Got data')

socks.close()
print('exiting')
