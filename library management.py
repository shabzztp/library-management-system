library = {}

def add_book(title, author):
    if title in library:
        print("Book already exists in the library.")
    else:
        library[title] = author
        print("Book added successfully.")

def search_book(title):
    if title in library:
        print("Book found.")
        print("Title:", title)
        print("Author:", library[title])
    else:
        print("Book not found in the library.")

def display_books():
    if len(library) == 0:
        print("The library is empty.")
    else:
        print("Books available in the library:")
        for title, author in library.items():
            print("Title:", title)
            print("Author:", author)
            print()

# Main program loop
while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display Books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        add_book(title, author)
    elif choice == "2":
        title = input("Enter the title of the book: ")
        search_book(title)
    elif choice == "3":
        display_books()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
