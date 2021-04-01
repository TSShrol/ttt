# class Calculator: #a+b,a-b,...
#     # a=0
#     # b=0
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def set_a(self):
#         self.a=int(input('Input a: \n'))
#
#     def set_b(self):
#         self.b=int(input('Input b: \n'))
#
#     def calc(self, operation):
#         if operation =='+':
#             return int(self.a)+int(self.b)
#
# calc1=Calculator(2,3)
# print(calc1.calc('+'))
# # print(Calculator.a)


# class Calculator: #a+b,a-b,...
#     # a=0
#     # b=0
#     def __init__(self,a,b):
#         self.__a=str(a)
#         self.__b=str(b)
#
#     def __del__(self):
#         print("Object deleted!")
#
#     def set_a(self):
#         self.__a=input('Input a: \n')
#
#     def set_b(self):
#         self.__b=input('Input b: \n')
#
#     def calc(self, operation):
#         return eval(''.join([self.__a,operation,self.__b]))
#
#     def calcRez(self, operation):
#         print(eval(''.join([self.a,operation,self.b])))
#
#
# calc2=Calculator(3,4)
# print(calc2.calc('+'))
# print(calc2.calc('-'))
# print(calc2.calc('**'))
# print(calc2.calc('/'))
# print(calc2.a)
# calc2._Calculator__a=str(7)
# print(calc2.a)
# print(calc2.calc('+'))


# class Calculator: #a+b,a-b,...
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b
#
#     def __del__(self):
#         print("Object deleted!")
#     name=property(get_a,set_a,set_b,"It's attribute name")
#     def set_a(self,a):
#         self.__a=a
#
#     def get_a(self):
#         return self.__a
#
#     def set_b(self, b):
#         self.__b = b
#
#     def get_b(self):
#         return self.__b
#
#     def calc(self, operation):
#         return eval(''.join([str(self.__a),operation,str(self.__b)]))
#
# calc1=Calculator(2,4)
# print(calc1.calc('*'))
# calc1.set_a(8)
# print(calc1.get_a())
# print(calc1.calc('*'))

# властивостей геттери використовується анотацій @property
# властивостей сеттери  використовується анотацій @імя_властивості_property.setter
class Calculator: #a+b,a-b,...
    def __init__(self,a=0,b=0):
        self.__a=a
        self.__b=b

    def __del__(self):
        print("Object deleted!")

    #getters
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    #setters
    @a.setter
    def a(self,a):
        self.__a=a

    @b.setter
    def b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def calc(self, operation):
        return eval(''.join([str(self.__a),operation,str(self.__b)]))

    def __str__(self):
        return f'Object include number1={self.__a}; number2={self.__b}'





calc1=Calculator(2,4)
print(calc1.a)
print(calc1.calc('*'))
calc1.a=22
print(calc1.a)
print(calc1.calc('*'))
print(calc1)