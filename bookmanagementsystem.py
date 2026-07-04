books = {}

def add_book():
    book_name = input("enter a new book: ")
    books[book_name] = "Not Read"
    print(f"{book_name} has been added to your library.") 


def view_book():
    if not books:
        print("Your library is empty.")
    else:
        print("Current Books in Library:")
        for name, status in books.items():
            print(f"- {name} [Status: {status}]")

def del_book():
    if not books:
        print("There are no books to delete")
        return
    
    del_name = input("Which book do you want to delete??: ")
    if del_name in books:
        del books[del_name]
        print(f"{del_name} has been deleted.")
    else:
        print(f"{del_name} not found in your library")

def change_reading_status():
    if not books:
        print("No books available to update.")
        return
    

    book_name = input("Enter the title of the book you want to update: ")
    if book_name in books:
        status = input(f"Have you read '{book_name}'? (yes/no): ").lower()
        if status == 'yes':
            books[book_name] = "Read"
            print(f"Status updated! '{book_name}' is now marked as Read.")
        elif status == 'no':
            books[book_name] = "Not Read"
            print(f"Status updated! '{book_name}' is marked as Not Read.")
        else:
            print("Invalid input! Please type 'yes' or 'no'.")
    else:
        print(f"'{book_name}' not found in your library.")
    
    

while True:
    print("\nThe book managment")
    print("1. Add book")
    print("2. View book")
    print("3. Delete book")
    print("4. Update Reading Status")
    print("5. Exit")



    choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_book()
    elif choice == '3':
        del_book()
    elif choice == '4':
        change_reading_status()
    elif choice == '5':
        print("Exiting program.Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4 or 5.")