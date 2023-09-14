age = int(input("Введите возраст"))
if age>0 and age<14:
    print("Вы еще малы")
elif age>=14 and age<23:
    print("Вы подходите")
elif age >=23 and age <100:
    print ("вы подходите")
else:
    print("вы перестарели")