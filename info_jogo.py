import re
import requests
import json

# URL da agenda de jogos do Flamengo do Globo Esporte
url = "https://ge.globo.com/futebol/times/flamengo/agenda-de-jogos-do-flamengo/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar o JSON
json_string_match = re.search(r'window\.dataSportsSchedule\s*=\s*({.*?});', html_content, re.DOTALL)
if json_string_match:
    json_string = json_string_match.group(1)

    # Capturar a string completa de 'teamAgenda' até 'featuredVideo'
    team_agenda_match = re.search(r'"teamAgenda":\{.*?"featuredVideo":.*?\}', json_string, re.DOTALL)
    if team_agenda_match:
        team_agenda_string = team_agenda_match.group(0)
        # Adicionar delimitadores ao final da string
        if not team_agenda_string.endswith('}}]}'):
            team_agenda_string += '}}]}'

        # Decodificar o JSON para verificar o conteúdo
        try:
            team_agenda_data = json.loads('{' + team_agenda_string + '}')
            future_events = team_agenda_data['teamAgenda']['future']
            
            # Verificar se há eventos e processar o primeiro evento
            if future_events:
                first_game = future_events[0]
                print("\nString do Próximo Jogo Extraída:")
                print(json.dumps(first_game, indent=4))  # Imprime o JSON do primeiro jogo de forma legível
                
                # Extrair informações do primeiro jogo
                first_contestant = first_game['match']['firstContestant']['popularName']
                second_contestant = first_game['match']['secondContestant']['popularName']
                competicao = first_game['match']['phase']['championshipEdition']['championship']['name']
                dia = first_game['match']['startDate']
                hora = first_game['match']['startHour']

                # Identificar o oponente que não é o Flamengo
                if first_contestant != "Flamengo":
                    oponente = first_contestant
                else:
                    oponente = second_contestant

                print(f"\nPróximo jogo:")
                print(f"Oponente: {oponente}")
                print(f"Campeonato: {competicao}")
                print(f"Data: {dia}")
                print(f"Hora: {hora}")
            else:
                print("Não foi encontrado nenhum evento no 'teamAgenda'.")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
    else:
        print("Não foi possível encontrar a seção 'teamAgenda' até 'featuredVideo' no JSON.")
else:
    print("Não foi possível encontrar o JSON no HTML.")
