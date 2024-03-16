height = float(input("Digite sua altura: "))
weight = int(input("Digite seu peso: "))

result = round(weight/(height**2),2)
if result<18.5:
  print(f"Seu IMC é {result}, você está abaixo do peso.")
elif result>=18.5 and result<25:
  print(f"Seu IMC é {result}, você tem um peso normal.")
elif result>=25 and result<30:
  print(f"Seu IMC é {result}, você está com sobrepeso.")
elif result>=30 and result<35:
  print(f"Seu IMC é {result}, você está obeso(a).")