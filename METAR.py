!pip install xmltodict

import pprint
import json
import requests
import xmltodict

def requisicao():
  api_key = "1737636254"
  api_pass = "cf334dde-eb8c-11ee-8b18-0050569ac2e1"
  icao_code = input("Informe o código ICAO desejado: ")

  url = f"http://aisweb.decea.gov.br/api/?apiKey={api_key}&apiPass={api_pass}&area=met&icaoCode={icao_code}"

  resposta = requests.get(url)

  return resposta

def xml_to_dict(resposta):
  resposta_json = xmltodict.parse(resposta.content)

  return resposta_json

def metar_to_list(resposta_json):
  metar = resposta_json.get('aisweb').get('met').get('metar')

  lista_metar = metar.split()

  return lista_metar

def icao_code(resposta_json):
  codigo_icao = resposta_json.get('aisweb').get('met').get('loc')

  return codigo_icao

def get_horario(lista_metar):
  horario_observacao = f"{int(lista_metar[2][2:4])-3}:{lista_metar[2][4:6]}"

  return horario_observacao

def get_vento(lista_metar):
 vento = int(lista_metar[3][0:3])
 velocidade_do_vento = lista_metar[3][3:5]


 if vento >=316 or vento <=45:
   direcao_vento = "Norte"
 elif vento >=46 and vento <= 135:
   direcao_vento = "Leste"
 elif vento >=136 and vento <=225:
   direcao_vento = "Sul"
 elif vento >=226 and vento <=315:
   direcao_vento = "Oeste"


 result = f"Vento de {direcao_vento} com {velocidade_do_vento} nós"


 return result
 return vento

def get_temperatura(lista_metar):
  temperatura = f"{lista_metar[-2][0:2]}º C"

  return temperatura

def get_pressao(lista_metar):
  pressao = f"{lista_metar[-1][1:5]} hPa"

  return pressao

def resultado(resposta_json, lista_metar):
  codigo_icao = icao_code(resposta_json)
  horario_observacao = get_horario(lista_metar)
  vento = get_vento(lista_metar)
  temperatura = get_temperatura(lista_metar)
  pressao = get_pressao(lista_metar)
  print(f"\nCódigo ICAO: {codigo_icao}\nHorário da Observação: {horario_observacao}\nVento: {vento}\nTemperatura:{temperatura}\nPressão:{pressao}")

def main():
  resposta = requisicao()
  resposta_json = xml_to_dict(resposta)
  lista_metar = metar_to_list(resposta_json)
  resultado(resposta_json, lista_metar)

#----------------------------------------------------------------------------------------------------
main()
