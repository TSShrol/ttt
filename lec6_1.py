class Alpha:
    __doc__ = "Один із супер класів"
    def infoClass(self):
        print("Class Alpha")

class Betta:
    def infoClass(self):
        print("Class Betta")

class Jamma(Alpha):
    pass
    # def infoClass(self):
    #     print("Class Jamma")

class Delta(Betta,Alpha):
    pass

class Omega(Jamma):
    __doc__ = "Похідний клас від Jamma"
    pass

class Omega2(Delta,Omega):
    pass

#
# obj1=Delta()
# obj1.infoClass()
# obj2=Omega()
# obj2.infoClass()
# obj3=Omega2()
# obj3.infoClass()
# print(Omega2.__mro__)
# print(Omega2.__bases__)
# print(Omega2.__dict__)
# print(Omega2.__doc__)
# print(Omega.__doc__)
# print(Alpha.__doc__)
# print(Omega2.__module__)

