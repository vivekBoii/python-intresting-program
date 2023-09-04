class library:
    books={"champak":1,"Ncert":1,"Quantum":1,"R.s aggarwal":1}
    dic={}
    number_of_books=4
    def show_books(self):
        for book in self.books.keys():
            print(book)
    def issue_book(self,book_name,student_name,date):
        if(self.books[book_name]==1):
            self.number_of_books=self.number_of_books-1
            self.books[book_name]=0
            book_name_class=(book_name+'.')[:-1]
            book_name_class=book(student_name,date)
            self.dic[book_name]=book_name_class
        else:
            print("Sorry book not avaliable")
            print(f"currently it is issued to {self.dic[book_name].student_name} on {self.dic[book_name].date}")
    def add_book(self,book_name):
        self.books.update({book_name:1})
        
class book(library):
    def __init__(self,student_name,date):
        self.student_name=student_name
        self.date=date

activate=library()
activate.show_books()
activate.issue_book("champak","vivek","5 sep 2023")
print(activate.number_of_books)
activate.issue_book("champak","niraj","6 sep 2023")
activate.add_book("champak")
activate.show_books()
