class Book:

    '''
    Requirements:

    Fields: title, author, isbn, isAvailable
    Constructor that initializes all fields (book starts as available)
    borrowBook(): marks book as unavailable if currently available, returns success/failure
    returnBook(): marks book as available
    displayInfo(): prints book details including availability status
    '''

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = not self.is_available
            return True
        print("Book is not available")
        return False
    
    def return_book(self):
        print("Book has been successfully returned")
        self.is_available = True

    def display_info(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable: {self.is_available}"
        )

if __name__ == "__main__":
    book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")

    book.return_book()
    book.display_info()
    