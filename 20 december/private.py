class A:
    __x=10  #private variable
    def __show(self): #private method
        print("from class A")
class B(A):
    pass
print(dir(B))
obj=B()
print(obj._A__x)
obj._A__show()