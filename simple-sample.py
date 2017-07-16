#Task 1:
#Есть два списка разной длины.
#В первом содержатся ключи, а во втором значения.
#Напишите функцию, которая создаёт из этих ключей и значений словарь.
#Если ключу не хватило значения, в словаре должно быть значение None.
#Значения, которым не хватило ключей, нужно игнорировать.
#Есть два списка разной длины. 

l1 = ['one', 'two', 'three', 'four', 'five']
l2 = ['1', '2', '3', '4']
my_dict = dict(zip(keys, value + [None]))
my_dict

#Task2:
#Написать скрипт, который: определяет, является ли заданная строка полиндромом.
# Строку можно жестко задать в коде.

word = str(input("Введите слово: "))
a = word[::-1]
if word == a:
  print("Введенное слово - полиндром")
else:
  print("Введенное слово не полиндром")

#Task3:
#Заданы 2 списка:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Напишите скрипт, который вернет 1 список, в котором будут элементы общие для списков a и b. 
#Результирующий список не должен сожердать дубликатов.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a)&set(b))


#Task 4:
#Предположим, у нас есть access.log веб­сервера. 
#Нужно написать скрипт, который найдет десять IP­адресов, от которых было больше всего запросов.
#Пример формата лога и самого лога можно найти по ссылке: http://ossec­docs.readthedocs.org/en/latest/log_samples/apache/apache.html

f = open('access.log')
data = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', f.read())
f.close()
for ip in Counter(data).most_common(10):
    print ip[0]
