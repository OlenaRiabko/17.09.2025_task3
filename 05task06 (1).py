#Task 6
# Програма для збору фідбеку від клієнтів ресторану

feedback = input("Введіть ваш фідбек: ")
bonus = 0
if len(feedback) > 60:
    bonus += 15
    print("Знижка 15%")

if "меню" in feedback.lower(): 
    bonus += 5
    print("За 'меню' нараховано 5% знижки.")
        
if "спортзал" in feedback.lower():
    bonus += 5
    print("За 'спортзал'нараховано 5% знижки.")
        
if "обслуговування" in feedback.lower():
    bonus += 5
    print("За 'обслуговування' нараховано 5% знижки.")
        
print(f"\nЗагальний бонус на наступне відвідування: {bonus}%")
