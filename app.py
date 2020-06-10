import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.debug = True

@app.route('/admin')
def admin():
    return "Kezelőfelület helye"
@app.route('/')
def index():
    
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)