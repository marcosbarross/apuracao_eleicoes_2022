import requests
import json
import pandas as pd

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []
diferenca = []

for informacoes in json_data['cand']:
    
    if informacoes['seq'] in ['1', '2']:
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'] + '%')

        if informacoes['seq'] == '1':
            diferenca.append('1º lugar')

        elif informacoes['seq'] == '2':
            diferenca.append((int(json_data['cand'][0]['vap']) - int(informacoes['vap'])))


df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem, diferenca)), columns = [
    'Candidato | ', 'Nº de Votos | ', 'Porcentagem | ', 'Votos para 1º colocado'
])

print(df_eleicao)