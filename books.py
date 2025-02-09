from flask import Flask, jsonify, request
app = Flask(__name__)

books = [{"id" : 101, "name": "Harry Potter"},{"id" : 102, "name": "Don Quixote"
},{"id" : 103, "name": "The Da Vinci Code"}]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
