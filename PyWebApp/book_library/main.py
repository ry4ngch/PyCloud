from flask import Flask, render_template, request, redirect, url_for
from Book import books
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    all_books = books.get_books()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        books.insert_book(
            request.form['title'],
            request.form['author'],
            request.form['rating']
        )
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<index>', methods=['GET', 'POST'])
def edit(index: int):
    if request.method == "POST":
        books.update_book(
            index,
            request.form['title'],
            request.form['author'],
            request.form['rating']
        )
        return redirect(url_for('home'))
    return render_template('edit.html', book=books.get_book(index))


@app.route('/delete')
def delete():
    books.delete_book(request.args.get('index'))

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

