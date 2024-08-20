from fastapi import APIRouter, HTTPException
from schemas.schema import all_books
from core.database import collection
from models.model import Books
from bson import ObjectId

router = APIRouter()

# list all books
@router.get("/books/")
async def get_all_books():
    data = collection.find()
    return all_books(data)

# add a new book
@router.post("/books/")
async def new_book(new_book : Books):
    try:
        resp = collection.insert_one(dict(new_book))
        return {"status_code": 200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
# information of a particular book
@router.get("/books/{book_id}")
async def find_data(book_id : str):
    try:
        id = ObjectId(book_id)
        existing_doc = collection.find_one({"_id":id})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Book does not exist.")
        resp = collection.find({"_id":id})
        return all_books(resp)
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

# update a book
@router.put("/books/{book_id}")
async def update_book(book_id : str, updated_book : Books):
    try:
        id = ObjectId(book_id)
        existing_doc = collection.find_one({"_id":id})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Book does not exist.")
        resp = collection.update_one({"_id":id}, {"$set":dict(updated_book)})
        return {"status_code":200, "message":"Book updated successfully."}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
# remove a book
@router.delete("/books/{book_id}")
async def delete_book(book_id : str):
    try:
        id = ObjectId(book_id)
        existing_doc = collection.find_one({"_id":id})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Book does not exist.")
        resp = collection.delete_one({"_id":id})
        return {"status_code":200, "message":"Book Deleted successfully."}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")