def individual_data(book):
    return {
        "id" : str(book["_id"]),
        "title" : book["title"],
        "author" : book["author"],
        "published_year" : book["published_year"],
        "isbn" : book["isbn"],
        "pages" : book["pages"]
    }
    
def all_books(books):
    return [individual_data(book) for book in books]