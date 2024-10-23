tabela = []
contato = {
    'nome': 'Edson',
    'Email': 'eds@hotmail.com'
}

tabela.append(contato.copy())
print(tabela)
contato['nome'] = input("Nome: ")
contato['Email'] = input("email: ")