import tweepy
from datetime import datetime
from oponente import oponente
from info_jogo import competicao, dia, hora
from config import api_key, api_secret, bearer_token, access_token, access_token_secret
# Você pode reproduzir a execução em outra conta criando um arquivo config.py e inserindo suas chaves do Twitter Developer Portal

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def calcular_dias(data_jogo):
    hoje = datetime.now()
    data_jogo = datetime.strptime(data_jogo, "%Y-%m-%d")
    dias_faltando = (data_jogo - hoje).days
    return dias_faltando + 1

dias_faltando = calcular_dias(dia)

if competicao == "Amistosos":
    if dias_faltando > 1:
        client.create_tweet(text=f"Faltam {dias_faltando} dias para o Flamengo entrar em campo contra o(a) {oponente} em um jogo amistoso.")
    if dias_faltando == 1:
        client.create_tweet(text=f"Falta {dias_faltando} dia para o Flamengo entrar em campo contra o(a) {oponente} em um jogo amistoso.")
    else:
        client.create_tweet(text=f"Hoje tem FLAMENGO! O Mengão entra em campo contra o(a) {oponente} em um jogo amistoso às {hora}.")

else:
    if dias_faltando > 1:
        client.create_tweet(text=f"Faltam {dias_faltando} dias para o Flamengo entrar em campo contra o(a) {oponente} pelo(a) {competicao}.")
    if dias_faltando == 1:
        client.create_tweet(text=f"Falta {dias_faltando} dia para o Flamengo entrar em campo contra o(a) {oponente} pelo(a) {competicao}.")
    else:
        client.create_tweet(text=f"Hoje tem FLAMENGO! O Mengão entra em campo contra o(a) {oponente} pelo(a) {competicao} às {hora}.")

print("Tweet feito!")
