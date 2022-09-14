#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#Пример:
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5

value1 = 'qwe'
value2 = 'qwe asd zxc qwe ertqwe'


n = 3
def get_sec_entry(val1, val2):
    start = val2.find(val1)
    return val2.find(val1, start + 1)

print(get_sec_entry(value1, value2))