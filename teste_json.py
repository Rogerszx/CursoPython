import json

#pessoa = {
 #   'nome': 'Luiz Otávio',
 #   'sobrenome': 'Miranda',
 #   'idade': 18,
  #  'altura': 1.8,
 #   'endereços': [
 #       {'rua': 'tal tal', 'número': 123},
 #       {'rua': 'outra rua', 'número': 321},
  #  ],
#}

#with open('teste_json.json', 'w', encoding='utf8') as arquivo:
#    json.dump(pessoa, arquivo, 
  #            ensure_ascii= False, indent= 2
           #   )

with open('teste_json.json' , 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['idade'])