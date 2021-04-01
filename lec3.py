import copy

# from copy import deepcopy
list1 = [1, 25, 6]
print(list1)
list2 = [1, 2.3, 'Python', [2, 3]]
print(list2)
print(list1[1])
print(list2[2])
print(list2[3])
print(list2[3][1])
list1[1] = 2
print(list1)  # [1, 2, 6]
list3 = list1
print(list3)
print(id(list1), id(list3))
print(list1, list3)
list3[2] = 7
print(list1, list3)
list4 = list1[:]  # еквівалентно  list4=list1.copy() - неглибоке копіювання
print(list1, list4)
list4[2] = 8
print(list1, list3, list4)
print(id(list1), id(list3), id(list4))
list5 = [2, ['a', 'b'], [3.4, 6.5, -7.2]]
list6 = list5.copy()
print(list5, "\n", list6, sep="")
list6[1][1] = 'c'
print(list5, "\n", list6, sep="")
print(id(list5), id(list6))
print(id(list5[1][1]), id(list6[1][1]))
list7 = copy.deepcopy(list6)
# list7=deepcopy(list6)
print(list7)
list7[1][1] = 'd'
print(list6, "\n", list7, sep="")
print(id(list6), id(list7))
print(id(list6[1]), id(list7[1]))
list9 = []  # list9=list()
print(type(list9))
list10 = list('Python!')
print(list10)
list11 = list((2, 6, 7))
print(list11)
print("-" * 36)
# Сформувати список з цілих чисел [1,50], які кратні 7
listNumberof7 = list()
for number in range(1, 51):  # [1,2,3,..,50]
    if number % 7 == 0:
        listNumberof7.append(number)

print(listNumberof7)
# включення списків
listNumberOf8 = [number for number in range(1, 51) if number % 7 == 0]
print(listNumberOf8)

string1 = "Для научной и веб-разработки на Python. Поддерживает HTML, JS и SQL."
listStr = string1.split()
print(listStr)
print(string1.lower())
list12 = [symbol for symbol in string1.lower()]
print(list12)
symbolO = list12.count('о')
print(f"Кількість символів 'о' в рядку рівна {symbolO}")
print("Кількість символів 'о' в рядку рівна {}".format(symbolO))
print("Кількість символів 'о' в рядку рівна %s" % (symbolO))
print("Кількість символів 'о' в рядку рівна " + str(symbolO))
list12.remove('q')
print(list12)
list12.reverse()
print(list12)

spisok = [
            ['Kobzar', 'Katerina', 'Naymichka'],
            ['Lisovapisnya', 'Mavka']
        ]
for element_spisku in spisok:
    for element in element_spisku:
        print(element, end=", ")
print()
tuple2=3,
print(tuple2)
tuple1 = (
            ('Shevchenko', 'Katerin'),
            ('Ukrainka','Lisovapisnya')
        )
for elem_tuple in tuple1:
    avtor,tvir=elem_tuple #багатократне x=y=z=6, множинне avtor,tvir="Shevchenko","Lisova Pisnya"
    print(avtor," wrote ",tvir)

for elem_tuple in tuple1:
    print(elem_tuple)
    print(elem_tuple[0]," wrote ",elem_tuple[1])


spisok_avtor=['Shevchenko', 'Franko','Ukrainka']
spisol_title=[['kobzar','Naymichka'],['Kamenyari'],['Lisova Pisnya','Mavka']]
dict_literatura=dict(zip(spisok_avtor,spisol_title))
print(dict_literatura)
keys_dict=dict_literatura.keys()
print(keys_dict)

for key in keys_dict:
    print(key,"is written ", dict_literatura[key])

print("-"*36)
number_count=1
for avtor,tvory in dict_literatura.items():   # (key,value)
    print(number_count,avtor,end=':')
    for tvir in tvory:
        print(tvir,end=',')
    print('\n','*'*36)
    number_count+=1