from flask import Flask, request, jsonify
from Books import books

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Catálogo de libros</h1>'

@app.route('/libros')
def get_all_books():
    return jsonify({"Libros":books})

@app.route('/libros/<book_name>')
def get_books(book_name):
    booksFound = [book for book in books if book['name'] == book_name]
    if (len(booksFound) > 0):
        return jsonify({"Libro":booksFound[0]})
    return jsonify({"message":"No se encuentra el libro"})

@app.route('/libros', methods=['POST'])
def add_books():
    newBook = {
        'name': request.json['name'],
        'author': request.json['author'],
        'category': request.json['category'],
        'publisher': request.json['publisher'],
        'type': request.json['type']
    }
    books.append(newBook)
    return jsonify({"message":"Producto agregado", "books":books})

@app.route('/libros/<book_name>', methods=['PUT'])
def edit_book(book_name):
    bookFound = [book for book in books if book['name'] == book_name]
    if (len(bookFound) > 0):
        bookFound[0]['name'] = request.json['name']
        bookFound[0]['author'] = request.json['author']
        bookFound[0]['category'] = request.json['category']
        bookFound[0]['publisher'] = request.json['publisher']
        bookFound[0]['type'] = request.json['type']
        return jsonify({
            "message":"Libro actualizado",
            "book":bookFound[0]
        })
    return jsonify({"message":"No se encuentra el libro"})

@app.route('/autores/<author_name>')
def get_books_by_author(author_name):
    booksFound = [book for book in books if book['author'] == author_name]
    if (len(booksFound) > 0):
        return jsonify({"Libros":booksFound})
    return jsonify({"message":"No hay libros del autor %s" % author_name})

@app.route('/editoriales/<pub_name>')
def get_books_by_publisher(pub_name):
    booksFound = [book for book in books if book['publisher'] == pub_name]
    if (len(booksFound) > 0):
        return jsonify({"Libros":booksFound})
    return jsonify({"message":"No hay libros de la editorial %s" % pub_name})

@app.route('/categorias/<cat_name>')
def get_books_by_category(cat_name):
    booksFound = [book for book in books if book['category'] == cat_name]
    if(len(booksFound) > 0):
        return jsonify({"Libros":booksFound})
    return jsonify({"message":"No hay libros de la categoria %s" % cat_name})

if __name__ == '__main__':
    app.run(debug=True)
