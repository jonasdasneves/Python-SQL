import mysql.connector

#define conexão com o banco
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='db')

#variavel metodo cursor
cursor = db_connection.cursor()

#pergunta email e ecpf
email = input('Digite seu email')
cpf = input('digite seu cpf')

sql = ("SELECT nome,email,nascimento FROM cliente WHERE email = %s AND cpf = %s")

values = (email,cpf)
cursor.execute(sql,values)

for(nome,email,nascimento) in cursor:
    print(nome,email,nascimento)



