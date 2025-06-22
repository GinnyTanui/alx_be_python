class Library:
    def __init__(self):
         self.books = [] 
    def add_book(self, book): 
        self.books.append(book) 
    def list_books(self):
        for book in self.books:
            info = f"{book.title} by {book.author}"
            if hasattr(book, 'file_size'):
                info += f" File Size: {book.file_size}"
            elif hasattr(book, 'page_count'):
                info += f", Page Count: {book.page_count}"
            print(info)


class Book:
    def __init__(self, title, author):
        self.title = str(title) 
        self.author = str(author)         
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)  
class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)