import pymongo as pyM


# conecta ao mongodb
cliente = pyM.MongoClient("suas credenciais aqui")
# Abrir banco de dados
db = cliente.test
collection = db.test_collection

# Criar cliente
cliente = {
    "nome": "filipe",
    "cpf": "123.123.123-23",
    "endereco": "rua ana 123",
}

# cria a coleção clientes e adicione-lhe o documento
clientes = db.clientes
cliente_id = clientes.insert_one(cliente).inserted_id

# Criar conta
conta = {
    "tipo": "corrente",
    "agencia": "12.123-12",
    "num": "12",
    "id_cliente": cliente_id,
    "saldo": 150.00,
}
# cria a coleção contas e adicione-lhe o documento
contas = db.contas
conta_id = contas.insert_one(conta).inserted_id


