from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "Kezelőfelület helye"
@app.route('/')
def index():
    name="Attila"
    return render_template('index.html', name=name)
    
if __name__ == "__main__":
    app.run()