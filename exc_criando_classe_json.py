import json

pessoa = {'nome': 'Roger',
     'sobrenome' : 'Gonçalves'}
    


with open('exc_criando_classe_json.json', 'w+', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii= False)

