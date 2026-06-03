# Store books and their status
books = {
    "python basics": "available",
    "java fundamentals": "borrowed",
    "c programming": "available",
    "data structures": "borrowed",
    "machine learning": "available",
    "sql for beginners": "available",
    "web development": "borrowed",
    "operating systems": "available"
}

# Add new book
def add(library):
    """Add a book to library."""

    book_name = input("what book do you want to add: ").lower()

    if book_name in library:
        return "That book already exists"

    library[book_name] = "available"
    return "adding book was successful!"


# Borrow a book
def borrow(library):
    """Borrow a book from library."""

    name = input("can you enter the book that you want to borrow: ").lower()

    if name in library:

        if library[name] == "borrowed":
            return "sorry! that book already borrowed by someone"

        library[name] = "borrowed"
        return "borrowing book was successful"

    return "sorry! we don't have that book"


# Return borrowed book
def return_book(library):
    """Return a borrowed book."""

    return_book_name = input("Enter the name of the book that you want to return: ").lower()

    if return_book_name in library:

        if library[return_book_name] == "available":
            return "That book was not borrowed. please check the book name"

        library[return_book_name] = "available"
        return f"returning {return_book_name} was successful"

    return "invalid return"


# Show available books
def availability(library):
    """Display available books."""

    print("currently we have these books:")

    for book, status in library.items():
        if status == "available":
            print(f"- {book}")


is_on = True

while is_on:

    try:
        # Show menu
        choose = int(input("1.Add book \n2.Borrow book \n3.Return book \n4.Availability check\n5.Exit \nWhat do you want?:"))

    except ValueError:
        print("i didn't get it .please choose between them")
        continue

    # Add book
    if choose == 1:
        print(add(books))

    # Borrow book
    elif choose == 2:
        print(borrow(books))

    # Return book
    elif choose == 3:
        print(return_book(books))

    # Show available books
    elif choose == 4:
        availability(books)

    # Exit program
    elif choose == 5:
        is_on = False
        print("Thank you for visiting our library")

    else:
        print("please choose valid option")