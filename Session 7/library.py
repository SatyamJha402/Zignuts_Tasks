class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title):
        if title not in self.books:
            self.books.append(title)
            print(title + "added to library")
        else:
            print("this book already exists")
            
    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(title + "removed")
        else:
            print(title + "not in library")
            
    def search_book(self, title):
        result = []
        for b in self.books:
            if title.lower() in b.lower():
                result.append(b)
        return result
    
lib = Library()
lib.add_book("Python Programming")
lib.add_book("Data Science with Python")
lib.add_book("Deep Learning")

print(lib.books)

print(lib.search_book("python"))

lib.remove_book("Deep Learning")
print(lib.books)