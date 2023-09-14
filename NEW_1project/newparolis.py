logek=input("введи логин")
hah=input("Введи пароль")
while True:
    if logek=="QWERTY" and hah=="qwerza":
        print("Ты вошель")
        break
    else:
        print("Ты что-то не правильно ввел попробуй снова")
        logek = input("введи логин")
        hah = input("Введи пароль")