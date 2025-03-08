class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity=1):
        self.books[title] = self.books.get(title, 0) + quantity
        print(f'Added {quantity} copies of "{title}" to the library.')

    def display_books(self):
        print("\nAvailable Books:")
        for title, quantity in self.books.items():
            if quantity > 0:
                print(f'"{title}" - {quantity} copies')

    def borrow_book(self, title):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            print(f'You have borrowed "{title}".')
        else:
            print(f'Sorry, "{title}" is not available right now.')

    def return_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1
        print(f'You have returned "{title}".')


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            quantity = int(input("Enter quantity: "))
            library.add_book(title, quantity)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")


if __name__ == "__main__":
    main()
