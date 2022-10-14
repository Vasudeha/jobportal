from flask import Flask, render_template, request
app = Flask(_name_)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confim", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        e = request.form.get('email')
        p = request.form.get('phone')
        return  render_template('confirm.html',name=n,email=e,phone=p)

if _name_ == "_main_":
    app.run(debug=True)