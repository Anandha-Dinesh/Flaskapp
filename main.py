from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chat')
def chat():
    return render_template('chat.html')
if __name__ == "__main__":
    print("hi")
    app.run(debug=True)
   