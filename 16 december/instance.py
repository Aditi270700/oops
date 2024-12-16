# Instance 

class A:
    def new(self):
        print("1st method") #declaration
    def new1(self):
        self.new()
        print("2nd method")
obj=A()
obj.new() #calling
obj.new1()