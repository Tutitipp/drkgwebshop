import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.debug = True

engine = create_engine('mysql://drkgwebshop:020601@localhost/merch')
database = scoped_session(sessionmaker(bind=engine))

@app.route('/admin')
def admin():
    database.execute("INSERT INTO merch (name, tags) VALUE ('Me', 1234)")
    database.commit()
    return "Kezelőfelület helye"
@app.route('/')
def index():
    
    return render_template('home.html')

@app.route('/index') #Itten e
def home():
    return render_template('index.html')
    
@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)