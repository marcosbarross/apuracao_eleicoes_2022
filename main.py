from timeit import repeat
from tkinter.colorchooser import Chooser
import requests
import json
import pandas as pd
import time
import os
import random

repeat = True

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

def resultado():
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

while repeat:
    
    resultado()
    segundos_aleatorios = random.choice([1, 2, 3, 4, 5])
    time.sleep(segundos_aleatorios)
    os.system('cls')