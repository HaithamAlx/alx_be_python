class Book:
    def __init__(self, Title,Author, Year: int):
        self.Title = Title
        self.Author = Author
        self.year = Year
    
    def __str__(self):

        return f"{self.Title} by {self.Author}, published in {self.year}"

    def __repr__(self):

        return f"Book('{self.Title}', '{self.Author}', {self.year})"
    
    def __del__(self):

        print (f"Deleting {self.Title}")

    
  
# my_book = Book("Harry Potter","Egypt",2025)

# print(my_book)

# print(f"this is a test {my_book}")
# # Delete the object manually
# del my_book