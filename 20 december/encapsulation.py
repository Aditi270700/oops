# encapsulation
'''
encapsulation is used for to stop hacking.
multiple attribute combines is convert into  a single unit is called encapsulation.

 access specifies:--

 1.  x=10 public (govt place)
 2. -x=10(-) protected (covered capus)
 3. --x=10(--)private (private house)

'''

class A:
    x=10
    def __init__(self,name):
        self.name=name
    @classmethod
    def show(cls,age):
        cls.age=age
    @staticmethod
    def display(school):
        print(school)