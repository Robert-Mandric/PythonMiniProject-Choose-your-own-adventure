from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input('What is the master password? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "\n" "Password:", str(fer.decrypt(passw.encode())))


def add():
    name = input("Account name: ")
    pwd = input("Passwords: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input(
        'Whould you like to view your existing passwords or add a new one? (view/add)\n Press "q" to quit. ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue