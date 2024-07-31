import re
import requests
import json

# URL da agenda de jogos do Flamengo do Globo Esporte
url = "https://ge.globo.com/futebol/times/flamengo/agenda-de-jogos-do-flamengo/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar o JSON dentro de window.byTeamScheduleTeamData
json_data_match = re.search(r'window\.byTeamScheduleTeamData\s*=\s*({.*?});', html_content, re.DOTALL)

# Inicializando a variável do oponente
oponente = None

# Se encontrou o JSON
if json_data_match:
    json_data = json_data_match.group(1)

    try:
        # Carregar a string JSON como um dicionário
        data = json.loads(json_data)

        # Extrair informações relevantes
        match_info = data.get('matches', [])[0]  # Primeiro jogo listado
        if match_info:
            # Identificar os times participantes
            time1 = match_info.get('firstContestant', {}).get('popularName', None)
            time2 = match_info.get('secondContestant', {}).get('popularName', None)

            # Identificar o oponente
            if time1 and time1 != "Flamengo":
                oponente = time1
            elif time2 and time2 != "Flamengo":
                oponente = time2

            if oponente:
                print(f"Oponente: {oponente}")
            else:
                print("Oponente não encontrado.")

    except json.JSONDecodeError:
        print("Erro ao decodificar JSON.")
else:
    print("Informações do próximo jogo não encontradas.")
