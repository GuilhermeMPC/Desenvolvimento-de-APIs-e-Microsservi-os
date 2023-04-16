from flask import Flask, render_template

app = Flask(__name__)

produtos = [
    {
        "id": 1,
        "titulo":"Camiseta Azul"
    },
    {
        "id": 2,
        "titulo":"Camiseta Rosa"
    },
    {
        "id": 3,
        "titulo":"Camisola Preta"
    },
    {
        "id": 4,
        "titulo":"Calça Jeans"
    },
    {
        "id": 5,
        "titulo":"Calça Preta"
    },
    {
        "id": 6,
        "titulo":"Óculos Azul"
    },
    {
        "id": 7,
        "titulo":"Tenis Verde"
    },
    {
        "id": 8,
        "titulo":"Tenis Rosa"
    },
    {
        "id": 9,
        "titulo":"Tenis Azul"
    },
    {
        "id": 10,
        "titulo":"Boné Verde"
    }
]

@app.route('/produtos', methods=["GET"])
def verificar():        
    return{"produtos": produtos}

@app.route('/consultar/<int:id>', methods=["GET"])
def consultar(id):
    encontrado = []
    for produto in produtos:
        if id == produto["id"]:
           encontrado.append(produto)
           break
    if len(encontrado) > 0:
        return encontrado
    else: 
        return "Erro: Nenhum produto possui este Id", 404

@app.route('/pesquisar/<string:termo>', methods=["GET"])
def pesquisar(termo):
    encontrados = []
    for item in produtos:
        if termo in item["titulo"]:
            encontrados.append(item)
    if len(encontrados) > 0:
        return encontrados
    else:
        return f"Nenhum produto com o termo '{termo}' foi encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)