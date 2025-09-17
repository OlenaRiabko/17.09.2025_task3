#Завдання 5 Напишіть програму, яка вводить з клавіатури послідовність чисел, 
#перетворює послідовність на кортеж і виводить його відсортованим у порядку зростання. 


numbers_list = []
print("Введіть довільну послідовність чисел:")
while True:
    value=input("Введіть число,або 'stop':")
    if  value=="stop":
        break
    else:
        value = int(value)
        numbers_list.append(value)
number_tuple = tuple(numbers_list)
print(f"Ваш список: {numbers_list}")

print(f"Ваш відсортований кортеж:{sorted(number_tuple)}")