from flask import Flask, request, render_template, redirect, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kkk eae man'

@app.route("/", methods=['POST'])
def form():

    nome = request.form.get('txtNome')
    email = request.form.get('txtEmail')
    senha = request.form.get('pw')

    print(nome,email,senha)
    return render_template('form.html')


if __name__ in '__main__':
    app.run(debug=True)
