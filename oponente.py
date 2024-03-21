import re
import requests

# URL da agenda de jogos do Flamengo do Globo Esporte
url = "https://ge.globo.com/futebol/times/flamengo/agenda-de-jogos-do-flamengo/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar a primeira ocorrência entre "match" e "location"
proximo_jogo_oponente = re.search(r'match.*?location"', html_content, re.DOTALL)

# Se encontrou a correspondência, extraia as instâncias após "popularName" entre aspas
if proximo_jogo_oponente:
    proximo_jogo_texto = proximo_jogo_oponente.group(0)
    
    # Usando expressão regular para encontrar todas as instâncias após "popularName" entre aspas
    times = re.findall(r'popularName":"(.*?)"', proximo_jogo_texto, re.UNICODE)

    # Verificando a instância diferente de "Flamengo" e armazenando em "oponente"
    oponente = next((instancia for instancia in times if instancia != "Flamengo"), None)

    # Se encontrou a correspondência, imprima o resultado
    if oponente:
        print(f"Oponente: {oponente}")
