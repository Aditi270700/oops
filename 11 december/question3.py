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
'''

declaration of instance variable


# inside class
# 1. through constructor
# 2. through instance method

# outside class
# 1. through object

# calling
# inside class---> used self
         #         1. constructor
         #         2. instance
# outside class---> used object
    
'''
