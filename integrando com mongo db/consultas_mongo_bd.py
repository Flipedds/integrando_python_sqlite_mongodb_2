import pprint

import pymongo as pyM
# conexão omitada por questões de segurança
cliente = pyM.MongoClient(cliente)

db = cliente.test
collection = db.test_collection

print('\n Procurar por campo')
pprint.pprint(db.clientes.find_one({'nome': 'filipe'}))

