# Task to create a simple CRUD (Create, Read, Update, Delete) API for managing a collection	of books in	a library using FastAPI (a Python Framework), MongoDB (for database) and Docker Compose.

## Prerequisites
1. Python installed
2. MongoDB Desktop installed
3. Docker Desktop installed

## Features
1. CRUD operations: Create, read, update, and delete books.
2. MongoDB integration: Use MongoDB as the database.
3. SOLID and Clean Architecture: The project is designed with modularity and separation of concerns in mind.
4. Swagger documentation: Automatically generated API documentation with Swagger UI.

## Technologies
1. FastAPI - Fast, modern web framework for building APIs.
2. MongoDB - NoSQL database used for storing book records.
3. Docker - Containerization platform for running the application.
4. Pymongo & Motor - MongoDB drivers for interacting with the database.

## Setup Instructions

### Local Setup (Without Docker)

1. Clone the repository:
```
git clone https://github.com/AshantC/LibraryBooksAPI_01.git
```
2. Create a virtual environment and activate it:
```
python -m venv venv
venv/bin/activate
cd app
```
3. Install the dependencies:
```
pip install -r requirenments.txt
```
4. Run the application:
```
uvicorn main:app --reload
```
5. The API will be available at http://localhost:8000/docs


## Usage
Once the server is running, you can access the Swagger UI at:
```
http://localhost:8000/docs
```

## API Endpoints
1. GET /books/: Retrieve all books
2. POST /books/: Add a new book
3. GET /books/{book_id}: Get details of a specific book by ID
4. PUT /books/{book_id}: Update a book by ID
5. DELETE /books/{book_id}: Delete a book by ID

## Example JSON Payload for Creating/Updating a Book:
```
{
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt, David Thomas",
  "published_year": 1999,
  "isbn": "978-0201616224",
  "pages": 352
}
```
