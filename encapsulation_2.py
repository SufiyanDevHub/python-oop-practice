class Student:
    def __init__(self,name):
        self.name=name  #public
        self.__grade= 0 #private

    #Set the grade
    def set_grade(self,grade):
        if grade >=0 and grade <=100:
            self.__grade = grade

        else:
            print("grade must be between 0 and 100")
            

    def get_grade(self):
        return self.__grade


    def get_status(self):
        if self.__grade>= 60:
            return "Passed"        
        else:
            return "Fail"

c = Student("Sufiyan Ali")
c.set_grade(95)
print(c.get_grade())
print(c.get_status())
