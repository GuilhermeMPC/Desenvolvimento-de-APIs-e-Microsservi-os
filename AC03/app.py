
##### EXEMPLO DE TABELA MYSQL PARA UTILIZAÇÃO DO CÓDIGO

'''
CREATE TABLE TB_PRODUTOS 
(ID INT NOT NULL AUTO_INCREMENT NOT NULL KEY,
PRODUTO VARCHAR(30) NOT NULL UNIQUE);
'''


from flask import Flask, request
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

@app.route("/produtos", methods=["GET"])
def todos_produtos():
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')

        consulta_sql = "select * from tb_produtos"
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


@app.route("/produtos/adicionar", methods=["POST"])
def add_produto():
    produto = request.args.get('prod')
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')
        consulta_sql =  "insert into tb_produtos (produto) VALUE ('"+produto+"')"
        print(consulta_sql)
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        con.commit()
        return "O produto foi adicionado com sucesso foi adicionado com sucesso!"
    
    except Error as e:
        print("Erro do Banco de Dados:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()

@app.route("/produtos/remover", methods=["DELETE"])
def delete_produto():
    produto = request.args.get('prod')
    id = request.args.get('id')
    if produto == None:
        produto =""
    if id is None:
        id = "0"
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='abc123de45')
        cursor = con.cursor()
        consulta_sql = "delete from tb_produtos where produto = '"+produto+"' or id = "+id
        cursor.execute(consulta_sql)
        linhas = todos_produtos()
        con.commit()
        count = 0
        prod = ""
        for linha in linhas:
            if int(id) in linha or produto.lower() == linha[1].lower():
                prod = linha[1]
                count += 1
        if count == 1:
            return "O produto "+prod+" foi removido com sucesso"
        else:
            return "O produto não existe na base de dados"
        
    
    except Error as e:
        print("Erro do Banco de Dados:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


if __name__ == '__main__':
    app.run(debug=True)