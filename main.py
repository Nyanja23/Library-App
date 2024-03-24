import csv

class LibraryApp:
    books = []
    categories = []
    def __init__(self):
        self.librarian = ""
        self.commands = {
            'help':self.showHelp,
            'quit': self.quit_app,
            'add':self.add_books,
            'remove': self.remove_book,
            'search':self.search_book,
            'display':self.display_books
        }

    # Writing to a csv file without deleting its contents.
    def write_to_csv(self,book):
        with open('books.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if csv_file.tell() == 0:
                header = ['Title','Author','Category']
                csv_writer.writerow(header)
            csv_writer.writerow(book)
    
    # Updating the csv file after operations such as delete/remove
    def update_csv(self):
        with open('books.csv','w',newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            header = ['Title','Author','Category']
            csv_writer.writerow(header)
            for book in LibraryApp.books:
                csv_writer.writerow(book)
    
    #Adding book details to a library
                 
    def add_books(self):
        title = input("Enter Book Title\n")
        author = input("Enter Book Author\n")
        category = input("Enter Book Category\n")
        new_book = [title,author,category]
        if new_book not in LibraryApp.books:
            LibraryApp.books.append(new_book)
            self.write_to_csv(new_book)
            print("Book added successfully\nEnter 'add' to Save another book")
        else:
            print("Book already exists in the library.")

    # Removing the book and Updating the CSV
    def remove_book(self):
        title = input("Enter the title of the book  you want to remove\n")
        for book in LibraryApp.books:
            if book[:1] == [title]:
                LibraryApp.books.remove(book)
                self.update_csv()
            else:
                print(f"Book with title '{title}' was not found in Library Books!")
    

    def search_book(self):
        title = input("Enter the Book title to Search\n").lower()
        for book in LibraryApp.books:
            if title in [x.lower() for x in book]:
                print(f"{title.capitalize()} is in Library")
    # Display Books
    def display_books(self):
        for book in LibraryApp.books:
            print(f"{book[0]} By {book[1]} ({book[2]})")
    def set_librarian(self,name):
        self.librarian = name
    def get_categories(self):
        for book in LibraryApp.book_objects:
            LibraryApp.categories.append(book.category)


    # Running the LibraryApp
    def run(self):
        print()
        print("Welcome To Your Library Management Application\nType 'help' To show commands")
        while True:
            user_input = input('>>>').strip()
            if user_input:
                command_parts = user_input.split()
                command = command_parts[0]
                args = command_parts[1:]
                self.execute_command(command,args)
    def execute_command(self,command,args):
        if command in self.commands:
            self.commands[command](*args)
        else:
            print("Invalid Command. Type 'help' for list of commands...")
    def showHelp(self):
        print("Available Commands.")
        for command in self.commands:
            print(command)
    def quit_app(self):
        print('Thanks for Using Your Library Management App. GoodBye!')
        exit()

class Books(LibraryApp):
    book_objects = []
    def __init__(self,title,author,category):
        super().__init__()
        self.title = title
        self.author = author
        self.category = category
        Books.book_objects.append(self)
    @classmethod
    def instanciate_from_csv(cls):
        with open('books.csv','r') as f:
            reader = csv.DictReader(f)
            books =  list(reader)
        for book in books:
            Books(
                title = book.get('Title'),
                author = book.get('Author'),
                category = book.get('Category')
            )
        
if __name__ == '__main__':
    app = LibraryApp()
    Books.instanciate_from_csv()
    app.run()
