# Please note that this is in GREEK, you might need to translate the strings to understand more things clearly.
class Book:
    def __init__(self, title, author, year, price, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.isbn = isbn

    def __repr__(self):
        return f"Βιβλίο {self.title}, Συγγραφέας: {self.author}, Έτος {self.year}, Τιμή: {self.price:.2f}, ISBN: {self.isbn}"


class BookStore:
    num_books = 0

    def __init__(self):
        self.books = []

    def addBook(self, title, author, year, price, isbn):
        new_book = Book(title, author, year, price, isbn)
        self.books.append(new_book)
        BookStore.num_books += 1

    def searchBooksByAuthor(self, author=None):
        if not author:
            author = input("Πληκτρολογήστε Όνοµα και Επώνυµο συγγραφέα: ")

        found_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book)

        return found_books

    def deleteBookWithISBN(self, isbn=None):
        if not isbn:
            isbn = input("Πληκτρολογήστε ISBN : ")

        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                BookStore.num_books -= 1
                print(f"Το βιβλίο {book.title} δεν είναι πλέον διαθέσιμο.")
                break
        else:
            print("Δεν βρέθηκε το βιβλίο.")

    def __repr__(self):
        sorted_books = sorted(self.books, key=lambda x: x.title)
        return f"Πλήθος βιβλίων: {BookStore.num_books}:\n" + "\n".join(
            [f"{i + 1}. {book}" for i, book in enumerate(sorted_books)])


if __name__ == "__main__":
    bs = BookStore()

    print("0) Καταχώρηση Βιβλίων\n=====================")
    bs.addBook("Python Crash Course", "Eric Matthews", 2016, 27.95, "1593279280")
    bs.addBook("Learning Python", "Mark Lutz", 2021, 40.29, "1449355730")
    bs.addBook("Head First Python", "Paul Barry", 2017, 36.25, "7519813630")
    bs.addBook("Introduction to Machine Learning with Python", "Andreas C. Muller", 2020, 31.99, "1449369413")
    bs.addBook("Python for Data Analysis", "Wes McKinney", 2022, 38.38, "1098104032")
    bs.addBook("Deep Learning with Python", "Francois Chollet", 2017, 30.20, "1617284433")

    print(bs)

    print(
        "\n1) Αναζήτηση βιβλίων με το όνομα και επώνυμο συγγραφέα\n==================================================")
    bk = bs.searchBooksByAuthor()
    if bk:
        print("Τα βιβλία που βρέθηκαν είναι:")
        for b in bk:
            print("\t", b)
    else:
        print("** Δεν υπάρχουν βιβλία με αυτόν τον συγγραφέα **")

    print("\n2) Διαγραφή βιβλίου με βάση το ISBN\n===================================")
    bs.deleteBookWithISBN()

    print(
        "\n3) Εκτύπωση όλων των διαθέσιμων βιβλίων με όλη την σχετική πληροφορία\n===================================================")
    print(bs)
