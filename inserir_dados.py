import mysql.connector
from datetime import date

#define conexão com o banco
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='db')

#define uma variavel para o metodo cursor
cursor = db_connection.cursor()

#define o comando sql e os valores a serem inseridos
sql = ('INSERT INTO cliente values(%s,%s,%s,%s,%s,%s)')
values = ('53218172861','José scooby Martins de Oliveira','jose.martins@gmail.com','2006-09-13','M','$2b$12$abcd1234examplehash')

#insere o comando e os valores
cursor.execute(sql,values)

#usa a data para registrar o momento da ação
current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')

print("\n")
print(formatted_date)
print("\n")
print(cursor.rowcount, "record inserted.")
print("\n")
