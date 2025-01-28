from flask import Flask

app = Flask(__name__) #creating the app instance

@app.route('/home')
def home():
    return '<h2>Madrine Denla Nansimbi is my name.</h2>'

if __name__== '__main__':
    app.run(debug=True)