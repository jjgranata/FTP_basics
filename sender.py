import socket

credentials = {}

with open('user_pass.txt', 'r') as f:

    for line in f:
        user, pwd = line.strip().split(':')
        credentials[user] = pwd

username = input("Enter your username")

if username in credentials:

    password = input("Enter pwd")
    if credentials[username] == password:

        port = 60000
        s = socket.socket()

        host = socket.gethostname()
        s.bind((host, port))
        s.listen(5)

        print("Loading....")

        while True:
            connection, address = s.accept()
            print("Connection address:", address)
            chunks = connection.recv(1024)
            print("Loaded", repr(chunks))

            filename = 'my-test.txt'
            file = open(filename, 'rb')
            buffer = file.read(1024)

            while buffer:
                connection.send(buffer)
                print("Sent ", repr(buffer))
                buffer = file.read(1024)
            file.close()

            print("Done")

            connection.send(bytes('Exiting', 'UTF-8'))

            connection.close()  # socket.shutdown()

    else:
        print("Pwd invalid")
else:
    print("Username invalid")
