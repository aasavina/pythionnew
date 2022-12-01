# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
m = int(input("введите номер месяца"))
#if m>3 and m<6:
#    print("весна")
#elif m>5 and m<9:
#    print("лето")
#elif m>8 and m<12:
#    print("осень")
#else:  print("зима")

seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
months_dict = {1: seasons.get(1), 2: seasons.get(1), 3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
               6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3), 9: seasons.get(4), 10: seasons.get(4),
               11: seasons.get(4), 12: seasons.get(1)}
value = months_dict[m]

print(f" это {value}")
