from flask import Flask, request
import requests


app = Flask(__name__)

@app.route("/")
def todos_clientes():
    try:
        print("teste")
        api_url = "http://127.0.0.1:5000/clientes"
        response = requests.get(api_url)
        return response.json()
    except:
        return "Ocorreu um erro ao contatar a API externa",502

@app.route("/", methods=["POST"])
def add_cliente():
    try:
        cliente = request.args.get('cust')
        api_url = "http://127.0.0.1:5000/clientes?cust="+cliente
        response = requests.post(api_url)
        return response.content
    except:
        return "Ocorreu um erro ao contatar a API externa",502

@app.route("/", methods=["DELETE"])
def delete_cliente():
    try:    
        cliente = request.args.get('cust')
        id = request.args.get('id')
        if cliente == None:
            cliente ="-----"
        if id is None:
            id = "0"
        api_url = "http://127.0.0.1:5000/clientes?cust="+cliente+"&id="+id
        response = requests.delete(api_url)
        return response.content
    except:
        return "Ocorreu um erro ao contatar a API externa",502


if __name__ == '__main__':
    app.run(debug=True, port="5001")