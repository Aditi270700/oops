class student:
    "student information"
    name="Aditi"
    age=24
    def __init__(self):
        print(id(self))
        print("constructor called......")
    def add(p,q):
        return p+q
obj=student()
obj1=student()
print(id(obj))
#  self is a reference of current class of current object 