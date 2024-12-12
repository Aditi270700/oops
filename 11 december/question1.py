class student:
    "student information"
    name="Aditi"
    age=24
    def add(p,q):
        return p+q
# print(dir(student))
# print(dir(student.__doc__))
# print(dir(student.__dict__))
obj=student
print(obj.name)
print(obj.age)
x = obj.add(5,6)
print(x)