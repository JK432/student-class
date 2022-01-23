class Student:
  
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
        
    
    def displayStudent(self):
        print("Roll No :  ",self.rollno)
        print("Name :  ",self.name)
        print("Couse: ",self.course)

stud1=Student(10,"Jack","IT")
stud2=Student(11,"Jill","CE")

stud1.displayStudent()
stud2.displayStudent()