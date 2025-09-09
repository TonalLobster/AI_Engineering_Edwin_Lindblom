from fastapi import FastAPI
from data_processing import library_data


app = FastAPI()

library = library_data("library.json")
books = library.books
# print(library)

@app.get("/books")
async def read_books():
    return books