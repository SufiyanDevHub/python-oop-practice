# class my_calss():
#     name = "Sufiyan ali"
#     age = 23
#     Field = "Computer science"
#     city = "karachi"


# x = my_calss()
# print(x.name)
# print(x.age)
# print(x.city)
# print(x.Field)

class Teacher():

    # initialize attributes
    def __init__(self,name,course_name,institute):
        self.name=name
        self.course_name=course_name
        self.institute = institute

    #initialize method
    def user_name(self):
        print(f"My name is {self.name}")

    def user_course_name(self):
        print(f"I am learning {self.course_name}")

    def user_institute(self):
        print(f"I am leraning from this course at {self.institute}")

# class store in object
p1 = Teacher("Sufiyan Ali","AI & Data Science","SMIT")
# calling attributes
print(p1.name)
print(p1.course_name)
p1.user_institute()
# calling attributes
p2 = Teacher("Huzaifa","Web development","Memon Industrial")
print(p2.name)
print(p2.course_name)