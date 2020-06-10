from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/admin')
def admin():
    return "Kezelőfelület helye"
@app.route('/')
def index():
    
    return render_template('home.html')

@app.route('/index.html') #Itten e
def home():
    
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()