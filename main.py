from flask import Flask, request, render_template, redirect, flash, session
import mysql.connector

#define conexão com o banco
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='db')

#variavel metodo cursor
cursor = db_connection.cursor(buffered=True)

#Define o objeto flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kkk eae man'


def consultar_email(email):
    sql = ("SELECT email FROM cliente WHERE email = %s")
    values = (email,)

    cursor.execute(sql,values)
    print(cursor)

def guardar_dados(email,nome,senha):
    print('dados registrados')

#Abre a página em um servidor
@app.route("/")
def home():

    return render_template('home.html')

@app.route("/cadastro", methods = ['GET','POST'])
def cadastro():
    nome = request.form.get('txtNome')
    email = request.form.get('txtEmail')
    senha = request.form.get('pw')

    retorno = consultar_email(email)

    if email == retorno:
        print("este email já está sendo utilizado, faça login")
    else:
        guardar_dados(email,nome,senha)
    
    print(retorno)

    return render_template("cadastro.html")



if __name__ in '__main__':
    app.run(debug=True)



