#coding: utf-8

import os

import pymongo
from bson.objectid import ObjectId

# --------------------

SERVIDOR = os.getenv('SERVIDOR')
USUARIO = os.getenv('USUARIO')
SENHA = os.getenv('SENHA')
BANCO = os.getenv('BANCO')
COLECAO = os.getenv('COLECAO')

# --------------------

def abrir_colecao():
    url = 'mongodb://{}:{}@{}/{}'.format(USUARIO, SENHA, SERVIDOR, BANCO)
    client = pymongo.MongoClient(url)
    db = client[BANCO]
    colecao = db[COLECAO]
    return colecao

# --------------------

def converter_id(id):
    return ObjectId(id)
