import pymongo as pyM

# conecta ao mongodb
# conexão omitada por questões de segurança
cliente = pyM.MongoClient(cliente)

db = cliente.test
collection = db.test_collection

cliente = {
    "nome": "filipe",
    "cpf": "123.123.123-23",
    "endereco": "rua ana 123",
}
clientes = db.clientes
cliente_id = clientes.insert_one(cliente).inserted_id

conta = {
    "tipo": "corrente",
    "agencia": "12.123-12",
    "num": "12",
    "id_cliente": cliente_id,
    "saldo": 150.00,
}
contas = db.contas
conta_id = contas.insert_one(conta).inserted_id


