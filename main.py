from services.library_services import LibraryService
from utils.display import display_books


def main():
    service = LibraryService()
    while True:
        print("\n--- Menu ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Display books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. End")

        choice = input("Select option: ")

        try:
            if choice == "1":
                title = input("Enter book's name: ")
                year = int(input("Enter year of the book: "))
                service.add_book(title=title, year=year)
                print(f"Book '{title}' has been add to the library.")

            elif choice == "2":
                title = input("Enter name of the book for removing: ")
                service.remove_book(title=title)
                print(f"Book'{title}' has been removed from library.")

            elif choice == "3":
                books = service.list_books()
                display_books(books)

            elif choice == "4":
                title = input("Enter name of the book for borrowing: ")
                service.get_book(title=title)
                print(f"Book '{title}' has been borrowed from library.")

            elif choice == "5":
                title = input("Enter name of the book for returning: ")
                service.return_book(title=title)
                print(f"Book '{title}' has been returned.")

            elif choice == "6":
                print("End")
                break

            else:
                print("The chosen option is not valid.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
