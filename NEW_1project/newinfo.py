# int() # числа
# float() # целое число
# str() # строки

# str_1 = 'hello '
# str_2 = 'world'
# num = 2
# num = str(num)
# print(str_1 + ' ' + str_2 + str(num)) # контикинация
# print(10 * str_1)
# print(str_1 * 10) #использовать контикинацию для вывода и рассчета
# True
# False

# num_1 = 1
# num_2 = 2
# result = num_1 <= num_2
# print(result)

#ниже представлен один из видов каскады
#условие работает на том же уровне что и элз
# num = int(input('Enter: '))
# if num == 1:
#     print('hello')
#     if num > 2:
#         print('here')
# else:
#     print('not hello')
# print('hi')

# num = int(input('enter: '))
# if num == 0:
#     pass # тут игнорируется сценарий, пасс используется как затычка
# elif num > 0:
#     pass
# elif num < 0:
#     pass
# else:
#     print('hi') #если элза не будет, то есть вероятность что выведет ошибку.

# num_1 = int(input('Enter: '))
# num_2 = int(input('Enter: '))
# num_3 = int(input('Enter: '))
    # if num_1 > num_2:
    #     larger_number = num_1
    # else:
    #     larger_number = num_2
    # print(larger_number)
# print(max(num_1, num_2, num_3))
# print(min(num_1, num_2, num_3))


# num = int(input('Enter: '))
# if num == (1, 3, 5, 7):
#     print('even nuber')
# if num / 2:
#         print('here')
# else:
#     print('Ood numdber')
# print('num')

# num_1 = int(input('Enter: '))
# num_2 = int(input('Enter: '))
# if num_1 > num_2:
#     larger_number = num_1
# else:
#     larger_number = num_2
# print(max(num_1, num_2))
# print(min(num_1, num_2))

a = int(input())
b = int(input())
if a > b:
    print('макс число' , a)
else:
    print('макс число', b)