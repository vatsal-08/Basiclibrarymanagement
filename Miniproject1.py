class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lenDict = {}

    def displayBook(self):
        print("We have following books in the library: ${self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book: user})
            print("Books dictionary has been updated!! You can take the book now")
        else:
            print("Book is already being used by", self.lenDict[book])

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lenDict.pop(book)


if __name__ == '__main__':
    vatsalLib = Library(['Python', 'Rich Poor', 'Harry Potter',
                         'c basics', 'Algorithms'], 'Coding is easy')

    while True:
        print(f"Welcome to the {vatsalLib.name}")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if(user_choice == 1):
            vatsalLib.displayBook()

        elif(user_choice == 2):
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter the name")
            vatsalLib.lendBook(user, book)

        elif(user_choice == 3):
            book = input("Enter the name of the book you want to add:")
            vatsalLib.addBook(book)

        elif(user_choice == 4):
            vatsalLib.displayBook()

        else:
            print("Not a valid option")

        print("Press q to quit and c continue")
        user_choice2 = ""

        while user_choice2 != 'q' and user_choice2 != 'c':
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue
