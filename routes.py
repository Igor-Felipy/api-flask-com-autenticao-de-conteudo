from flask import Flask, request

from main import insertUsuario

app = Flask("Youtube")


@app.route("/olamundo",methods=["GET"])
def olamundo():
    return {"Ola":"Mundo!"}


@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()
    
    if("nome" not in body):
        return geraResponse(400, "O parametro nome é obrigatorio")
    
    if("email" not in body):
        return geraResponse(400, "O parametro email é obrigatorio")

    if("senha" not in body):
        return geraResponse(400, "O parametro senha é obrigatorio")

    usuario = insertUsuario(body["nome"],body["email"],body["senha"])

    return geraResponse(200, "Usuario criado", "user", usuario)



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()