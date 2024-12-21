class Calculator:
    def add (self,*n):
        sum = 0
        for i in n:
            sum=sum+i
        print(sum)
    def sub(self,*n):
        sub=0
        for i in n:
            sub=sub-i
        print(sub)