class Gf:
    def name(self,name):
        self.x=name
        print(self.x)
class F(Gf):
    def f_name(self,f_name):
        self.y=f_name
class C(F):
    def C_name(self,C_name):
        self.z=C_name
obj=C()
obj.name('Aditi')