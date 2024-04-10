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
    return 'Hello!'

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)