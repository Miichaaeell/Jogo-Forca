def aleatorio():
    from random import randint
    palavras = (
    {'palavra': 'MELISSA', 'dica': 'nome feminino'}, {'palavra': 'ADRIANA', 'dica': 'nome feminino'}, {'palavra': 'MICHAEL', 'dica': 'nome masculino'},
    {'palavra': 'CLAUDETE', 'dica': 'nome feminino'}, {'palavra': 'KAMILLY', 'dica': 'nome feminino'}, {'palavra': 'CAROL', 'dica': 'nome feminino'},
    {'palavra': 'YURI', 'dica': 'nome masculino'}, {'palavra': 'THEO', 'dica': 'nome masculino'}, {'palavra': 'CAROLINE', 'dica': 'nome feminino'},
    {'palavra': 'ACSA', 'dica': 'nome feminino'}
    )
    return palavras[randint(0 , len(palavras) - 1)]
palavras = aleatorio()
print(palavras)
