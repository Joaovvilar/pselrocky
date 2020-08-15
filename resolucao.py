# Processo seletivo de TI para a ROCKY/Sorocaba
# João Victor Giraldez Pereira Vilar Silva
# O código deve realizar uma série de trasnformações até que o arquivo
# JSON volte a seu formato original e então verificar se este foi recuperado
# ['ø', 'æ', '¢', 'ß']

import json
import requests
from operator import itemgetter

#ordena em ordem crescente as categorias e os ID's , imprimindo-os ao final
def imprimirOrdenado(bd):
    #funções para ordenação
    bd.sort(key=itemgetter('id'), reverse=False)
    bd.sort(key=itemgetter('category'), reverse=False)
    for i in range(len(bd)):
        print(bd[i]['name'])
    return bd

#Calcular o estoque de cada categoria e em seguida imprime o valor de todos os produtos desta
def calcularEstoque(bd):
    #inicialização das variáveis
    estoqueAcessorios = 0
    estoqueEletrodomesticos = 0
    estoqueEletronicos = 0
    estoquePanelas = 0
    #percorre a lista com vários dicts, adicionando o valor do produto de acordo com a categoria
    for i in range(len(bd)):
        if bd[i]['category'] in 'Acessórios':
            estoqueAcessorios += bd[i]['quantity'] * bd[i]['price']
        elif bd[i]['category'] in 'Eletrodomésticos':
            estoqueEletrodomesticos += bd[i]['quantity'] * bd[i]['price']
        elif bd[i]['category'] in 'Eletrônicos':
            estoqueEletronicos += bd[i]['quantity'] * bd[i]['price']
        elif bd[i]['category'] in 'Panelas':
            estoquePanelas += bd[i]['quantity'] * bd[i]['price']            
    print('Valor Acessórios:',estoqueAcessorios)
    print('Valor Eletrodomésticos:',estoqueEletrodomesticos)
    print('Valor Eletrônicos:',estoqueEletronicos)
    print('Valor Panelas:',estoquePanelas)
    return



# Abro como leitura (read) em codificação utf8
bd = json.load(open('brokendatabase.json','r', encoding='utf-8'))

#Itera os valores do vetor de 0 até o comprimento de bd, fazendo as substituições caso necessário
for i in range(len(bd)):
    #uso da função replace() para substituir os chars incorretos 
    bd[i]['name'] = bd[i]['name'].replace('ø','o')
    bd[i]['name'] = bd[i]['name'].replace('æ','a')
    bd[i]['name'] = bd[i]['name'].replace('¢','c')
    bd[i]['name'] = bd[i]['name'].replace('ß','b')
    #troca as strings por números de ponto flutuante
    bd[i]['price'] = float(bd[i]['price'])
    #insere quantidade caso não exista
    if 'quantity' not in bd[i]:
        bd[i]['quantity'] = 0

#chama as funções de validação
newbd = imprimirOrdenado(bd)
calcularEstoque(bd)

#escreve o bd corrigido para a saída
with open('saida.json', 'w', encoding='utf-8') as saida:
    #para evitar uma sequência de escape \u, foi necessário assegurar que não escaparia como ASCII
    json.dump(newbd, saida, ensure_ascii=False)
