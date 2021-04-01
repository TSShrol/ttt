# def infoUser():
#     print("Info  user")
#
# def infoUserByName(nameUser):
#     print(nameUser+", раді тебе бачити!")
#
# def infoUserByNameAndYear(nameUser,year):
#     print(nameUser+", раді тебе бачити! Сьогодні тобі виповнилося "+str(year))
#
# def usingPass():
#     pass
#
# def returnInfoUserByName(nameUser='Mikola'):
#     return f'{nameUser}, раді тебе бачити на курсі!'
#
# def multipleInt(*args):
#     dob=1
#     for i in args:
#         dob*=i
#     return args,dob # a,b=3,4
#
# def multipleFloat(*args):
#     dob=1
#     for i in args:
#         dob*=i
#     return {'dobutok':dob} # a,b=3,4
#
# def exampleFunc(nameUser,*bals):
#     return f'{nameUser} ти отримав такі оцінки: {bals}'
#
# def vivedTowns(**countries):
#     for country in countries.keys():
#         print(country,'has town:')
#         for town in countries[country]:
#             print(town,end=',')
#         print()
#
# def addList(nameUser1,*spisok): #
#     global nameUser
#     def lenList(nameUser):
#         return f'{nameUser} you have...'
#     nameUser1=lenList('Kate')
#     print(nameUser1,id(spisok)) #((2,3,4),) (2,3,4)
#     spisok=list(spisok)
#     spisok[2]=6
#     nameUser='Olga'
#     print(nameUser)
#     return spisok
#
#
# # infoUser()
# # exampleFuncVariable=infoUser
# # exampleFuncVariable()
# # print(infoUser)
# # print(exampleFuncVariable)
# # infoUserByName('Ольга')
# # infoUserByNameAndYear('Kate',23)
# # infoUserByNameAndYear(year=20,nameUser='Lesya')
# # print(infoUser())
# print(returnInfoUserByName('Ira'))
# print(returnInfoUserByName())
# print(multipleInt(2,4,7,8))
# resultDob=multipleInt(2,3,4,5,6,7)[1]
# print(resultDob)
# print(multipleFloat(2.3,2.0))
# print(exampleFunc('Misha',5,4,5,4,5))
# bal=[5,6,7,8]
# print(exampleFunc('Ira',*bal))
#
# slovnik={'Ukrain':['Rivne','Kiyv'],'Poland':['Varshava','Vroclav']}
# vivedTowns(**slovnik)
# spisok=[2,3,4]
# nameUser='Igor'
# print(addList(nameUser,*spisok))
# print(nameUser)
# print(id(spisok))
#
# try:
#     n=int(input('inputs data:'))
#     if n==0:
#         raise ValueError
#     print(4/n)
# except ValueError as vl:
#     print('це не число!')
# except ZeroDivisionError:
#     print('Ділення на нуль!')
# else:
#     print('No errors!')
# finally:
#     print('Good!')

# def get_sum(data,lnum=[]):
#     print(lnum)
#     lnum.append(data)
#     return lnum

# print(get_sum(1,[2,3]))
# print(get_sum(4))
# print(get_sum(3))
# print(get_sum(2))
# print(get_sum(25))
# l1=[]
# print(get_sum(1,l1))
# print(get_sum(2,l1))
# lambda список_аргументів: вираз

func=lambda x,y : x+y

def get_sum(data,lnum=None):
    print(lnum)
    if lnum is None:
        lnum=[]
    lnum.append(data)
    lnum.append((lambda x: x+1)(data))
    return lnum

# print(get_sum(1,[2,3]))
print(get_sum(5))
print(get_sum(6))


print(func(2,3))