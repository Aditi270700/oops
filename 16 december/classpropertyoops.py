class p:
    def __init__(self,p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
class c(p):
    def c_property(self,qualification):
        self.q=qualification
        print(self.h)
        print(self.b)
        print(self.q)
        print(self.x)
obj=c('Aditi')
obj.p_properties('bhopal','central')
obj.c_property('BSC')

