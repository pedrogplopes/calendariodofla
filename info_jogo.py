import re
import requests
from datetime import datetime

# URL da agenda de jogos do Flamengo do Globo Esporte
url = "https://ge.globo.com/futebol/times/flamengo/agenda-de-jogos-do-flamengo/#/"

# Solicitação para obter o código fonte da página
response = requests.get(url)
html_content = response.text

# Usando expressões regulares para encontrar a primeira ocorrência entre "match" e "winner"
proximo_jogo_info = re.search(r'match.*?winner"', html_content, re.DOTALL | re.UNICODE)

# Se encontrou a correpondência
if proximo_jogo_info:
    proximo_jogo_info_texto = proximo_jogo_info.group(0)

    # Usando expressão regular para encontrar as instâncias entre aspas após "name", "startDate" e "startHour"
    competicao = re.search(r'"Championship","name":"([^"]+)"', proximo_jogo_info_texto)
    dia = re.search(r'startDate":"([^"]+)"', proximo_jogo_info_texto)
    hora = re.search(r'startHour":"([^"]+)"', proximo_jogo_info_texto)

    # Se encontrou a correspondência, imprima os resultados
    if competicao and dia and hora:
        competicao = competicao.group(1)
        dia = dia.group(1)
        hora = datetime.strptime(hora.group(1), "%H:%M:%S").strftime("%H:%M")
        print(f"Competição: {competicao}, Dia: {dia}, Hora: {hora}")
