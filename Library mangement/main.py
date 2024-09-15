class Library:
    def __init__(self):
        self.nobooks = 0
        self.book = []


    def addbook(self, book):
        self.book.append(book)
        self.nobooks += 1

    def showInfo(self):
        print(f"In Library there is {self.nobooks} books")

        for i in self.book:
            print(i)

    
l1 = Library()
l1.addbook("Harry Potter")
l1.addbook("Deep Work")
l1.addbook("Rich Dad Poor Dad")
l1.addbook("The Epic Shit")
l1.showInfo()
    
