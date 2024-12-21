class A:
    _x=10  #protected variable
    def _show(self): #protected method
        print("from class A")
class B(A):
    pass
print(dir(B))
class C:
    pass
print(dir(C))