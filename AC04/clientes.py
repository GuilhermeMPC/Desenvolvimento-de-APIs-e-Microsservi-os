
##### EXEMPLO DE TABELA MYSQL PARA UTILIZAÇÃO DO CÓDIGO

'''
CREATE TABLE TB_CLIENTES 
(ID INT AUTO_INCREMENT NOT NULL KEY,
CLIENTE VARCHAR(30) NOT NULL UNIQUE);
'''


from flask import Flask, request
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

@app.route("/clientes")
def todos_clientes():
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')

        consulta_sql = "select * from tb_clientes"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        return linhas
        
    except Error as e:
        print("Erro do Banco de Dados:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


@app.route("/clientes", methods=["POST"])
def add_cliente():
    cliente = request.args.get('cust')
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')
        consulta_sql =  "insert into tb_clientes (cliente) VALUE ('"+cliente+"')"
        print(consulta_sql)
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        con.commit()
        return "O cliente foi adicionado com sucesso!"
    
    except Error as e:
        print("Erro do Banco de Dados:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()

@app.route("/clientes", methods=["DELETE"])
def delete_clientes():
    cliente = request.args.get('cust')
    id = request.args.get('id')
    if cliente == None or cliente == "-----":
        cliente =""
    if id is None:
        id = "0"
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')
        cursor = con.cursor()
        consulta_sql = "delete from tb_clientes where cliente = '"+cliente+"' or id = "+id
        cursor.execute(consulta_sql)
        linhas = todos_clientes()
        con.commit()
        count = 0
        for linha in linhas:
            if int(id) in linha or cliente.lower() == linha[1].lower():
                cust = linha[1]
                count += 1
        if count == 1:
            return "O cliente "+cust+" foi removido com sucesso"
        else:
            return "O cliente não existe na base de dados"
        
    
    except Error as e:
        print("Erro do Banco de Dados:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


if __name__ == '__main__':
    app.run(debug=True, port="5000")