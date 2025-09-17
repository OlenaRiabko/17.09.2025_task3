#Завдання 2


#Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5 чисел).
#Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної послідовності. 
print("Введіть не менше 5 чисел")
numbers_list = [] 
for i in range(5):
    value = int(input(f"Введіть число {i+1}: "))
    numbers_list.append(value)
print("\n Ви ввели 5 чисел.")
print(f"\n Ваш список: {numbers_list}")
while True:
    choice = input("Бажаєте продовжити введення чисел? (+/-): ")    
    if choice == "+":
        value = int(input(f"Введіть додаткове число,або введіть '-' , щоб закінчити): "))
        numbers_list.append(value)
        print(numbers_list)
    elif choice == "-":
        break
    else:
        print("Помилка. Введіть 'так' або 'ні'.")
print(f"\n Ваш список: {numbers_list}")

for number in numbers_list:
    numbers_list2= numbers_list[::2]
print(f"\n Новий список: {numbers_list}")
print(f"Сума: {sum(numbers_list2)}")
print(f"Середнє арифметичне: {sum(numbers_list2)/len(numbers_list2)}")
