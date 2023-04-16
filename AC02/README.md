# Desenvolvimento-de-APIs-e-Microsserviços- AC02

Na AC02 foi proposto: <br>
<br>
"Criar uma api em Python usando a implementação de consulta/busca (GET). Lembre de colocar o Method e status code."<br>
<br>
Nessa atividade implementei o método GET de três formas, utilizando uma lista de produtos em JSON que possuem seus IDs e título do produto. As APIs criadas foram:<br>
<br>
## /produtos <br>
    Uma busca simples de todos os produtos cadastrados.
## /consultar/id <br>
    Uma consulta por ID, no qual retorna apenas o produto com aquele ID.
## /pesquisar/termo <br>
    Uma consulta que pesquisa um termo dentro de cada título e retorna todos os produtos com aquele termo (No caso, é Case Sensitve).
<br>
Caso alguma das consultas não retorne nenhum produto, o sistema retornará uma mensagem de erro e o Status Code será 404.<br>
<br>
<br>
Atividade entregue dia 16/04/2023 por Guilherme Midea Paoliello Castilho.
