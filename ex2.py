'''Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
  Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
  Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
  Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
  O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem'''

tempo = float (input ('Informe o tempo gasto na viagem: '))
velocidade = float (input ('Informe a velocidade media durante a viagem: '))

distancia = tempo * velocidade
litros_usados = distancia/12

print (f"A velocidade media da viagem foi de: {velocidade} km/h")
print (f"O tempo gasto na viagem foi de: {tempo} horas")
print (f"A distancia percorrida foi de: {distancia} km")
print (f"Foram gastos {litros_usados} litros de combustível durante a viagem")