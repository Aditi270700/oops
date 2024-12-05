def outer_function(func):
    def inner_function(x,y):
        x=x+5
        y=y+5
        data = func(x,y)
        return data
    return inner_function
@ outer_function
def main_function(x,y):
    z=x+y
    return z     
data=main_function(5,10)
print(data)