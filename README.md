# Task to create a simple CRUD (Create, Read, Update, Delete) API for managing a collection	of books in	a library using FastAPI (a Python Framework), MongoDB (for database) and Docker Compose.

## Prerequisites
1. Python installed
2. MongoDB Desktop installed
3. Docker Desktop installed

## How to start the application

### The commands:
First you have to git clone the files by entering in your terminal:

```
git clone https://github.com/AshantC/LibraryBooksAPI_01.git
```
Then create the virtual environment
```
python -m venv venv
```
Go to the app directory and install the requirenments.txt file
```
cd app
pip install -r requirenments.txt
```
Finally, to start the server use the following command: 
```
uvicorn main:app --reload
```

### For visualizing the application, open up your browser and enter:

http://127.0.0.1:8000/docs
