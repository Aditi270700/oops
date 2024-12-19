class Father:
    x=10
    y=20
    z=30
    def property (self,F_name,F_bank):
        self.name = "F_name"
        self.bank = "F_bank"
        print(self.name)
        print(self.bank)
class Mother:
    p=10
    q=20
    r=30
    def property1 (self):
        self.name1 = "M_name"
        self.bank2 = "M_bank"
        print(self.name1)
        print(self.bank2)
class Son (Father,Mother):
    pass
obj = Son()
obj.property1()
# print(dir(Son))