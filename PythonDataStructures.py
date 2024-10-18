# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your 
# task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    book_title = input("Enter the books title: ")
    book_author = input("Enter the books Author: ")
    if (book_title, book_author) not in library:
        library.append((book_title, book_author))
        print(f"'{book_title}' by {book_author} has been added to the library.")
    else:
        print(f"This '{book_title}' by {book_author} has already been added to this library!")

def view_library(library):
    for book in library:
        print(f"{book[0]}: {book[1]}")

def main():
    while True:
        print("""
                ====Library Menu====

                1. Add a book to the library
                2. View library
                3. Exit Program
            """)
        
        choice = input("Please make a choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_library(library)
        elif choice == "3":
            print("Exiting Program...")    
            break
        else:
            print("Please enter a valid option! Try Again.")

main()