#coding: utf-8

import json
from flask import Flask, request

import documento

# --------------------

def preparar_resposta_erro(codigo, titulo, mensagem):
    erro = {'titulo': titulo, 'mensagem': mensagem}
    payload = json.dumps(erro, ensure_ascii=False).encode('utf8')
    response = app.response_class(
        response = payload,
        status = codigo,
        mimetype = 'application/json'
    )
    return response

# --------------------

def preparar_resposta_sucesso(codigo, payload=None):
    response = app.response_class(
        response = json.dumps(payload),
        status = codigo,
        mimetype = 'application/json'
    )
    return response

# --------------------

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/api/documentos/', methods=['POST', 'GET', 'DELETE'])
@app.route('/api/documentos/<id>', methods=['GET', 'PUT', 'DELETE'])
def processar_documentos(id=''):
    
    dados = request.get_json()
    
    if request.method == 'POST':
        #--- CRIAR UM DOCUMENTO        
        codigo_retorno, dados_retorno = documento.criar(dados)
        #--- 
        if codigo_retorno == 201:
            response = preparar_resposta_sucesso(201, dados_retorno)
        #---     
        else:
            response = preparar_resposta_erro(
                400,
                'Conteúdo inválido.',
                'O conteúdo enviado não é JSON válido.'
            )                    
        
    elif request.method == 'GET':            
        if id:
            #--- RECUPERAR UM DOCUMENTO POR ID
            codigo_retorno, dados_retorno = documento.recuperar(id)
            #---
            if codigo_retorno == 200:
                response = preparar_resposta_sucesso(200, dados_retorno)
            #---
            else:
                response = preparar_resposta_erro(
                    404,
                    'Documento não encontrado.',
                    'Não foi encontrado nenhum documento com o id informado.'
                )
        else:            
            if request.args:               
                for k in request.args.keys():  
                    chave = k
                    valor = request.args[k]
                #--- BUSCAR UM DOCUMENTO POR CHAVE E VALOR
                codigo_retorno, dados_retorno = documento.buscar_todos(chave, valor)                
                #---
                if codigo_retorno == 200:
                    response = preparar_resposta_sucesso(200, dados_retorno)
                #---
                else:
                    response = preparar_resposta_erro(
                        404,
                        'Documento não encontrado.',
                        'Não foi encontrado nenhum documento com o id informado.'
                    )                
            else:
                #--- RECUPERAR TODOS DOCUMENTOS DA COLECAO
                codigo_retorno, dados_retorno = documento.recuperar_todos()            
                #--- 
                response = preparar_resposta_sucesso(200, dados_retorno)

   
    elif request.method == 'PUT':        
        #--- ATUALIZAR UM DOCUMENTO
        codigo_retorno, dados_retorno = documento.atualizar(id, dados)            
        #--- 
        if codigo_retorno == 200:
            response = preparar_resposta_sucesso(200, dados_retorno)
        #---             
        elif codigo_retorno == 400:
            response = preparar_resposta_erro(
                400,
                'Conteúdo inválido.',
                'O conteúdo enviado não é JSON válido.'
            )                          
        else:
            response = preparar_resposta_erro(
                404,
                'Documento não encontrado.',
                'Não foi encontrado nenhum documento com o id informado.'
            )        
    
    elif request.method == 'DELETE':
        if id:
            #--- EXCLUIR UM DOCUMENTO
            codigo_retorno, dados_retorno = documento.excluir(id)
            #---
            if codigo_retorno == 200:
                response = preparar_resposta_sucesso(200, dados_retorno)
            #---
            else:
                response = preparar_resposta_erro(
                    404,
                    'Documento não encontrado.',
                    'Não foi encontrado nenhum documento com o id informado.'
                )

        else:
            #--- EXCLUIR TODOS DOCUMENTOS (APAGAR COLEÇÃO)
            codigo_retorno, dados_retorno = documento.excluir_todos()            
            #--- 
            response = preparar_resposta_sucesso(200, dados_retorno)
    
    return response

# --------------------

if __name__ == '__main__':
    app.run()
