from flask import Flask, jsonify, request
app = Flask(__name__)

authors = [{"id" : 2001, "name" : "J.K.Rowling"}, {"id" : 2002, "name" : "Miguel de Cervantes"},
{"id":2003, "name": "Dan Brown"}]

@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(authors)

@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author:
       return jsonify(author)
    return jsonify({"error": "Author not found"}), 404

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000, debug=True)

