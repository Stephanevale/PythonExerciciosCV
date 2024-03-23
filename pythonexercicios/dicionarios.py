pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 40}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas['nome'] = ['Lola']
pessoas['peso'] = 55
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

