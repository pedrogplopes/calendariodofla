import re
import requests
from datetime import datetime
import json

# URL da agenda de jogos do Flamengo do Globo Esporte
url = "https://ge.globo.com/futebol/times/flamengo/agenda-de-jogos-do-flamengo/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar o JSON dentro de window.byTeamScheduleTeamData
json_data_match = re.search(r'window\.byTeamScheduleTeamData\s*=\s*({.*?});', html_content, re.DOTALL)

# Inicializando as variáveis
competicao = None
dia = None
hora = None

# Se encontrou o JSON
if json_data_match:
    json_data = json_data_match.group(1)

    try:
        # Carregar a string JSON como um dicionário
        data = json.loads(json_data)

        # Extrair informações relevantes
        match_info = data.get('matches', [])[0]  # Primeiro jogo listado
        if match_info:
            competicao = match_info.get('phase', {}).get('championshipEdition', {}).get('championship', {}).get('name', None)
            dia = match_info.get('startDate', None)
            hora = match_info.get('startHour', None)

            # Convertendo a hora para o formato HH:MM, se disponível
            if hora:
                hora = datetime.strptime(hora, "%H:%M:%S").strftime("%H:%M")

            print(f"Competição: {competicao}, Dia: {dia}, Hora: {hora}")

    except json.JSONDecodeError:
        print("Erro ao decodificar JSON.")
else:
    print("Informações do próximo jogo não encontradas.")
