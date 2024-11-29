from models.models import Library, Book


class LibraryService:
    def __init__(self):
        self.library = Library()


    def add_book(self, title: str, year: int) -> None:
        if title in self.library.books:
            raise ValueError(f"Book with title {title} already exists.")
        book = Book(title=title, year=year)
        self.library.books[title] = book


    def remove_book(self, title: str) -> None:
        if title not in self.library.books:
            raise ValueError(f"Book with title {title} does not exist.")
        del self.library.books[title]


    def list_books(self) -> list[dict]:
        return [book.model_dump() for book in self.library.books.values()]


    def get_book(self, title: str) -> None:
        if title not in self.library.books:
            raise ValueError(f"Book '{title}' is not found.")

        book = self.library.books[title]

        if book.borrow:
            raise ValueError(f"Book '{title}' is borrowed already.")

        book.borrow = True
        print(f"Book has been borrowed: {title}.")


    def return_book(self, title: str) -> None:
        if title not in self.library.books:
            raise ValueError(f"Book '{title}' is not found.")

        book = self.library.books[title]
        if book.borrow:
            book.borrow = False
            print(f"Book with name '{book.title}' has been returned.")
        else:
            raise ValueError(f"Book {book.title} cannot be returned because is still free.")