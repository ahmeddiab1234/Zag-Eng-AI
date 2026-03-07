class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = None

    def borrow(self, member_name):
        if self.borrowed_by:
            print(f"Book '{self.title}' is already borrowed by {self.borrowed_by}.")
        else:
            self.borrowed_by = member_name
            print(f"{member_name} borrowed '{self.title}'.")

    def return_book(self):
        if self.borrowed_by:
            print(f"Book '{self.title}' returned by {self.borrowed_by}.")
            self.borrowed_by = None
        else:
            print(f"Book '{self.title}' was not borrowed.")
