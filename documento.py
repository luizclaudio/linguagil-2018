#coding: utf-8

import acesso_mongo

# --------------------

def criar(dados):
    if type(dados) is dict:
        if len(dados.keys()):
            colecao = acesso_mongo.abrir_colecao()
            novo_id = colecao.insert_one(dados).inserted_id
            return 201, {'_id': str(novo_id)}
    return 400, None

# --------------------

def recuperar(id):
    colecao = acesso_mongo.abrir_colecao()
    documento = colecao.find_one({'_id': acesso_mongo.converter_id(id)})
    if documento:
        documento['_id'] = str(documento['_id'])
        return 200, documento
    return 404, None

# --------------------

def buscar_todos(chave, valor):
    todos = {'documentos': []}
    colecao = acesso_mongo.abrir_colecao()
    documentos = colecao.find({chave: valor})
    if documentos.count() > 0:
        for doc in documentos:
            doc['_id'] = str(doc['_id'])
            todos['documentos'].append(doc)        
        return 200, todos
    return 404, None     

# --------------------

def recuperar_todos():
    todos = {'documentos': []}
    colecao = acesso_mongo.abrir_colecao()
    documentos = colecao.find()
    if documentos.count() > 0:
        for doc in documentos:
            doc['_id'] = str(doc['_id'])
            todos['documentos'].append(doc)
    return 200, todos
    
# --------------------

def atualizar(id, dados):
    if type(dados) is dict:
        if len(dados.keys()):
            colecao = acesso_mongo.abrir_colecao()
            resultado = colecao.update_one(
                {'_id': acesso_mongo.converter_id(id)},
                {'$set': dados}
            )
            if resultado.matched_count:
                return 200, None
            else:
                return 404, None                
    return 400, None

# --------------------

def excluir(id):
    colecao = acesso_mongo.abrir_colecao()
    resultado = colecao.delete_one({'_id': acesso_mongo.converter_id(id)})
    if resultado.deleted_count:
        return 200, None
    else:
        return 404, None

# --------------------

def excluir_todos():
    colecao = acesso_mongo.abrir_colecao()
    colecao.drop()
    return 200, None
