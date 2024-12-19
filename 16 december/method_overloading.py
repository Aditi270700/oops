# error code
'''
class A:
    def add(self,x,y):
        return x+y
    def add(self,x,y,z):
        return x+y+z
obj=A()
obj.add(10,20,30)
'''
class A:
    def add(self,*n):
        sum=0
        for i in n: 
            sum=sum+i
        return sum
obj = A()
x=obj.add(10,20)
print(x)
y=obj.add(10,20,30)
print(y)


'''
class A:
class B(A):
class C(B):
class D:
class E(C,D):
    '''