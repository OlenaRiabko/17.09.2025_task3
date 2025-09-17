#Завдання 3
#Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) 
#у форматі RGB і виводить на екран кортеж, у якому зберігається колір.

print("Введіть параметри кольорів RGB (від 0 до 255).")
rgb_values = []
colors = ["Red", "Green", "Blue"]
while True:
    for color_name in colors:
        value_str = input(f"Введіть значення для {color_name}: ")
        value = int(value_str)
        if 0 <= value <= 255:
            rgb_values.append(value)
        else:
            print("Помилка. Спробуйте ще раз.")
    if len(rgb_values)==3:
        break
       
rgb_tuple = tuple(rgb_values)
print(f"RGB {rgb_tuple}")