# Processo seletivo de TI para a ROCKY/Sorocaba
# João Victor Giraldez Pereira Vilar Silva
# O código deve realizar uma série de trasnformações até que o arquivo
# JSON volte a seu formato original e então verificar se este foi recuperado
# ['ø', 'æ', '¢', 'ß']

import json
import requests
from operator import itemgetter

def imprimirOrdenado(bd):
    #newbd = sorted(bd, key=itemgetter('category'), reverse=False )
    #newbd = sorted(bd, key=lambda d: (d['category'], -d['id']), reverse=False)
    bd.sort(key=itemgetter('id'), reverse=False)
    bd.sort(key=itemgetter('category'), reverse=False)

    return bd

# Abro como leitura (read) em codificação utf8
bd = json.load(open('brokendatabase.json','r', encoding='utf-8'))

#Itera os valores do vetor de 0 até o comprimento de bd, fazendo as substituições caso necessário
for i in range(len(bd)):
    bd[i]['name'] = bd[i]['name'].replace('ø','o')
    bd[i]['name'] = bd[i]['name'].replace('æ','a')
    bd[i]['name'] = bd[i]['name'].replace('¢','c')
    bd[i]['name'] = bd[i]['name'].replace('ß','b')
    #troca as strings por números
    bd[i]['price'] = float(bd[i]['price'])
    #insere quantidade caso não exista
    if 'quantity' not in bd[i]:
        bd[i]['quantity'] = 0

newbd = imprimirOrdenado(bd)
for i in range(len(bd)):
    print(newbd[i])
# with open("a.json", "w") as f:
#      json.dump(bd, f, ensure_ascii=False)


#Printa a lista bonitinha
# for i in bd:
#     print(i)