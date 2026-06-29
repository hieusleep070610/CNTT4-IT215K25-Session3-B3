from fastapi import FastAPI
app = FastAPI()
books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "programming",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    }
]

@app.get("/books/statistics")

def statistics():
    total_books = len(books)
    available_books = 0 
    for book in books:
        if book["is_available"]:
            available_books += 1
    borrowed_books = total_books - available_books
    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books
    }

@app.get("/books/categories")
def display():
    categories = []
    for book in books:
        if book["category"]:
            categories.append(book["category"])
    return {"categories": list(set(categories))}

@app.get("/books/latest")
def latest_Book():
    if len(books) == 0:
        return {"message": "No books available"}
    latest = books[0]
    for book in books:
        if book["year"] > latest["year"]:
            latest = book
    return latest
