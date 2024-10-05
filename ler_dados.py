import mysql.connector

#define conexão com o banco
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='db')

#variavel metodo cursor
cursor = db_connection.cursor()

#define comando sql
sql = ("SELECT nome,email,nascimento FROM cliente WHERE sexo = 'M' AND nascimento > '1985-12-31' ORDER BY nome")

cursor.execute(sql)

for (nome,email,nascimento) in cursor:
    print(nome,email,nascimento)