# Коллекции

# Кортеж (tuple)

#  упорядоченный, не изменяемая, иммутабельная коллекция

#  нельзя добавлять, удалять элементы

# предв. зап. кортеж
tuple_1 = (10,20,30,3.14,'python', [1,2,3], (10,20,30))
tuple_1 = tuple('bigdickenergy')

# чтение значение
val_1 = tuple_1[0]

# срез кортежа
slice_1 = tuple_1[2:]
slice_1 = tuple_1[:3]
slice_1 = tuple_1[2:3]

# print(slice_1)

#словарь (dictionary)
# неупорядоченная, изменяемая
# элемент - это пара 'ключ-значение'

# создание пустого словаря
dict_slang = {}
dict_slang = dict()

# предварительно заполненный словарь
dict_slang_2 = {'lol' : 'laughing out loud', 'yolo' : 'you live only once', 'slang' : 'short language'}

lst = [(10,20),('k','v'),(2,dict_slang_2)]
dict_3 = dict(lst) 

dict_3 = dict(edward = 'vampire', jacob = 'werewolf', charlie = 'human')

# чтение значений
val_2 =  lst[2]

# замена значений
dict_slang_2['lol'] = 'lal'

# добавить пару
dict_slang_2['slay'] = 'to be very cool'

# удалить пару
del dict_slang_2['yolo']

# методы
print()
print(f'Исходный словарь: {dict_slang_2}')
print()

items_0 = list(dict_slang_2.items())
# когда нужны только ключи
keys_0 =  tuple(dict_slang_2.keys())
# когда нужны только ответы
val_0 = list(dict_slang_2.values())

print(f'Items: {items_0}')
print()
print(f'Keys: {keys_0}')
print()
print(f'Values : {val_0}')

# оффтоп
# for key, values in items_0:
#     print(key, values)

# остальные методы самостоятельно глянуть
# 4-ая коллекция (set)
  