def display_books(books):
    if not books:
        print("The library is empty.")
    else:
        print("Books in library:")
        for book in books:
            status = "free" if not book["borrow"] else "borrowed"
            print(f"- {book["title"]} (year: {book["year"]}, status: {status})")
