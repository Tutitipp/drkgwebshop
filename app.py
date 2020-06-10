import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('mysql://drkgwebshop@localhost/merch')
database = scoped_session(sessionmaker(bind=engine))

@app.route('/admin')
def admin():
    return "Kezelőfelület helye"
@app.route('/')
def index():
    name="Attila"
    return render_template('index.html', name=name)
    
if __name__ == "__main__":
    app.run(debug=True)