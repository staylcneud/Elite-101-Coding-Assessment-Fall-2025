from datetime import datetime, timedelta



# LEVEL 1 — View Available Books

def view_available_books():
    print("\nAvailable Books:")
    count = 0
    for book in library_books:
        if book["available"]:
            print(book["id"], "-", book["title"], "by", book["author"])
            count += 1
    if count == 0:
        print("No books available right now.")



# LEVEL 2 — Search by Author or Genre

def search_books():
    term = input("\nEnter author or genre: ").strip().lower()
    found = 0
    print("\nSearch Results:")
    for book in library_books:
        if term in book["author"].lower() or term in book["genre"].lower():
            print(book["id"], "-", book["title"], "by", book["author"], "(", book["genre"], ")")
            found += 1
    if found == 0:
        print("No matches found.")



# LEVEL 3 — Checkout a Book


def checkout_book():
    book_id = input("\nEnter book ID to check out: ").strip()
    for book in library_books:
        if book["id"].lower() == book_id.lower():
            if book["available"]:
                book["available"] = False
                due = datetime.now() + timedelta(days=14)
                book["due_date"] = due.strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print("Book checked out. Due:", book["due_date"])
            else:
                print("That book is already checked out until", book["due_date"])
            return
    print("Book not found.")



# LEVEL 4 — Return a Book + View Overdue Books

def return_book():
    book_id = input("\nEnter book ID to return: ").strip()
    for book in library_books:
        if book["id"].lower() == book_id.lower():
            if not book["available"]:
                book["available"] = True
                book["due_date"] = None
                print("Book returned successfully.")
            else:
                print("This book was not checked out.")
            return
    print("Book not found.")


def view_overdue_books():
    print("\nOverdue Books:")
    today = datetime.now()
    found = 0
    for book in library_books:
        if not book["available"] and book["due_date"]:
            try:
                due = datetime.strptime(book["due_date"], "%Y-%m-%d")
                if due < today:
                    print(book["id"], "-", book["title"], "was due on", book["due_date"])
                    found += 1
            except ValueError:
                continue
    if found == 0:
        print("No overdue books.")



# LEVEL 5 — Book Recommendation System


def recommend_books():
    available = [b for b in library_books if b["available"]]

    if len(available) == 0:
        print("There are no books available to recommend right now.")
        return

    sorted_books = sorted(available, key=lambda b: b["checkouts"], reverse=True)
    top_three = sorted_books[:3]

    print("\nTop Book Recommendations:")
    for book in top_three:
        print(f"- {book['title']} by {book['author']} (Genre: {book['genre']})")



# MENU SYSTEM

def main_menu():
    while True:
        print("\nLibrary Menu")
        print("1. View available books")
        print("2. Search by author or genre")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. View overdue books")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_available_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            checkout_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_overdue_books()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
