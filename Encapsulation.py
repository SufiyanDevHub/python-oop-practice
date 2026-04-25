# class EMP:
#     def __init__(self,name,salary):
#         self.name=name #public
#         self.__salary=salary #private

# a= EMP("sufiyan",50000)

# print(a.name)

class Person:
    def __init__(self,name,age):
        self.name= name
        self.__age=age

    def get_age(self):
        return self.__age

p = Person("Sufiyan",20)
print(p.name)
print(p.get_age())



