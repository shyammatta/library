from flask import Flask, render_template, request, redirect, url_for, session
from .models import User, Book, Cart
from . import db
cart = []
from flask import current_app as app
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        session['logged_in'] = True
        return redirect(url_for('book_management'))
    else:
        return "Invalid credentials, please try again."

@app.route('/book_management', methods=['GET', 'POST'])
def book_management():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        selected_books = request.form.getlist('book')

        Book.query.update({Book.selected: False})
        for book_name in selected_books:
            book = Book.query.filter_by(name=book_name).first()
            if book:
                book.selected = True
        db.session.commit()

        return redirect(url_for('lend'))
    
    books = Book.query.all()
    return render_template('book_management.html', books=books)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    books = Book.query.filter_by(selected=True).all()
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        for book in books:
            cart.append({
                "book": book.name,
                "start_date": start_date,
                "end_date": end_date
            })

            cart_item = Cart(book_name=book.name, start_date=start_date, end_date=end_date)
            db.session.add(cart_item)
        db.session.commit()

        return redirect(url_for('cart_page'))
    
    return render_template('lend.html', selected_books=books)

@app.route('/cart')
def cart_page():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    cart_items = Cart.query.all()

    return render_template('cart.html', cart=cart)
