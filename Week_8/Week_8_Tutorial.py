class Student :
    def __init__(self,name,math,science,english):
        self.average = None
        self.name=name
        self.math=math
        self.science=science
        self.english=english
    def Student(self):
        print(self.name)
    def average_marks(self):
        self.average=(self.math+self.science+self.english)/3
        return self.average
    def last_name(self):
        print(self)
        two_names = self.name.split(" ")
        return two_names[-1]

obj = Student("babel pool", 80,80,80)
print(obj.average_marks())
print(obj.last_name())