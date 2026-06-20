from flask import Flask, jsonify, request
from flask_cors import CORS

#Criar o nosso app
app = Flask(__name__)
#Habilitar o CORS
CORS(app)

#Criando nosso banco de dados local.
produtos = [
    {"id":1, "nome":"Notebook Gamer","preco": 5000},
    {"id":2, "nome":"Cadeira Gamer","preco": 300},
    {"id":3, "nome":"Mouse Gamer","preco": 150}
]

#Criar rota para listar os produtos
@app.route('/listar', methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)

#Criar rota para adicionar um produto
@app.route('/criar', methods=['POST'])
def criarProduto():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    return jsonify(produtoNovo),201
    #return jsonify({"message": "Produto criado com sucesso!"}), 201

#Criar rota para atualizar um produto
@app.route('/atualizar/<int:id>', methods=['PUT'])
def atualizarProduto(id):
    dados = request.get_json()
    for produto in produtos:
        if produto["id"] == id:
            produto["preco"] = dados["preco"]
            return jsonify(dados)
    return jsonify({"mensagem": "ID não encontrado!"}), 404

#Criar rota para deletar um produto
@app.route('/apagar/<int:id>', methods=['DELETE'])
def apagarProduto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"mensagem": "Produto deletado com sucesso!"})
    return jsonify({"mensagem": "ID não encontrado!"}), 404
    
#Rodar o programa
if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")