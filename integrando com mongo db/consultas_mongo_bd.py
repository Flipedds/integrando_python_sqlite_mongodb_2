import pprint

import pymongo as pyM
from bson import ObjectId

# conecta ao mongodb
cliente = pyM.MongoClient("suas credenciais aqui")

db = cliente.test
collection = db.test_collection

# print('\n Procurar por campo')
# pprint.pprint(db.clientes.find_one({'nome': 'filipe'}))

# Outras formas de procurar por _id
# objInstance = ObjectId(id)
# print(db.clientes.find_one({"_id": objInstance}))
# print(db.clientes.find_one({"_id": ObjectId(id)}))

# procurar cliente por _id
id = "63f27486b468c5993e20f01b"

consulta = db.clientes.find_one(ObjectId(id))
if consulta is None:
    print('Não foi possível encontrar esse cliente')
print(f"""
        Id: {consulta['_id']}
        Nome: {consulta['nome']}
        Cpf: {consulta['cpf']}
        Endereço: {consulta['endereco']}
""")

id_user = "63f27486b468c5993e20f01b"

resultado = db.contas.find_one({'id_cliente': ObjectId(id_user)})

if resultado is None:
    print('Não foi possível encontrar essa conta')
else:
    print(f"""
        Id: {resultado['_id']}
        Tipo: {resultado['tipo']}
        Agência: {resultado['agencia']}
        Numero: {resultado['num']}
        Id_Cliente: {resultado['id_cliente']}
        Saldo: {resultado['saldo']}
    """)
