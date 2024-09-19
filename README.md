# Consumidor da API METAR da AISWEB

Este projeto permite acessar e processar dados meteorológicos em tempo real através da API METAR da AISWEB. O código coleta informações específicas, como vento, temperatura e pressão, baseando-se no código ICAO informado pelo usuário.

## Principais Funcionalidades

- **Requisição de Dados**: O usuário pode informar um código ICAO para obter o relatório METAR correspondente.
  
- **Conversão de XML para JSON**: A resposta da API, originalmente em XML, é convertida para um formato JSON para facilitar a manipulação dos dados.

- **Extração de Informações**: O projeto extrai dados relevantes como:
  - Código ICAO
  - Horário da observação
  - Direção e velocidade do vento
  - Temperatura em graus Celsius
  - Pressão atmosférica em hPa
