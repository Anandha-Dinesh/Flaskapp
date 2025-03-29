from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        age = "you are eligible to vote" if int(request.form['age'])>18 else "go to school da thambiii"
        return f"Hello, {name}! \n {age}"
    return render_template('index.html')

if __name__ == "__main__":
    print("hi")
    app.run(debug=True)
   