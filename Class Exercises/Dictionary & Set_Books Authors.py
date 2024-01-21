with open('book_authors.txt', 'r') as file:
    contents = file.read().splitlines()

database = {}

for element in contents:
    parts = element.split(';')
    title = parts[0]
    authors = parts[1:]
    database[title] = authors

search_author = input("Author = ")

author_book = []

for title, authors in database.items():
    if search_author in authors:
        author_book.append(title)

if author_book:
    print(f"\nBooks written by {search_author}:")
    for book in author_book:
        print(book)
else:
    print(f"No books written by {search_author}")