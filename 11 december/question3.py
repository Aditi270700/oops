class Student:
   "Student Information"
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def show_detail(self):
      print(self.name)
      print(self.age)

obj=Student("aditi",24)
obj.show_detail()

obj1=Student("pragti",24)
obj1.show_detail()
    
   
