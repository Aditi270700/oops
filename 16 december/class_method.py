class Book:
    price=150
    def __init__(self,title,author,price):
        self.author = author
        self.title = title
        self.price = price
    @classmethod
    def update_price(cls,price):
        cls.price=price
    def show_details(self):
        print(self.title)
        print(self.author)
        print(Book.price)
obj=Book("python","john",150)
obj.update_price(200)
obj.show_details()#calling
# obj.showdetails()