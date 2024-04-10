# Author: Daniel J. Ourai
# Date: 4/10/24
# Assignment: M04 Lab - Case Study: Python APIs
# Description: This code functions as an API developed in Python. Using the provided link in the output, you will
# find information relevant to the books listed below in either a singular (by id) fashion, or as a list of all books.

from flask import Flask, jsonify

app = Flask(__name__)

# Placeholder book data
books = [
    {"id": 1, "title": "Harry Potter and the Chamber of Secrets", "author": "J.K Rowling", "description": "The second book of the Harry Poter series."},
    {"id": 2, "title": "Jack and the Beanstalk", "author": "Joseph Jacobs", "description": "A classic English tale."},
    {"id": 3, "title": "Twilight", "author": "Stephenie Meyer", "description": "The first book in the Twilight series."}
]

@app.route('/')
def index():
    """Route for the root endpoint.
    
    Returns:
        str: A simple greeting message.
    """
    return 'Hello!'

@app.route('/books', methods=['GET'])
def get_books():
    """Route to retrieve all books.
    
    Returns:
        Response: JSON response containing information about all books.
    """
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    """Route to retrieve a book by its ID.
    
    Args:
        book_id (int): The ID of the book to retrieve.
        
    Returns:
        Response: JSON response containing information about the specified book.
    """
    # Search for the book with the specified ID in the books list
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        # If the book is found, return it as a JSON response
        return jsonify(book)
    else:
        # If the book is not found, return an error message with a 404 status code
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)