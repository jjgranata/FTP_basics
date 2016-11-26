credentials = {}
with open('user_pass.txt', 'r') as f:
    for line in f:
        user, pwd = line.strip().split(':')
        credentials[user] = pwd

username = input("Enter your username")

if username in credentials:
    password = input("Enter pwd")
    if credentials[username] == password:
        print("Excellent!")
    else:
        print("Pwd invalid")
else:
    print("Username invalid")
