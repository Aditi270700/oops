class gf:               #multi level inheritance
    def name(self,name):
        self.n=name
class P(gf):
    def __init__(self,P_name):
        self.x=P_name
    def P_properties(self,home,bank):
        self.h=home
        self.b=bank
        print(self.h)
        print(self.b)
class C(P):
    def C_property(self,qualification):
        self.q=qualification
        self.P_properties("bhopal","central")
        # print(self.h)
        # print(self.b)
        print(self.q)
        print(self.x)
        self.name("Aditi Saudagar")
        print(self.n)
obj=C('Aditi')
# obj.P_properties('bhopal','central')
obj.C_property('BSC')

