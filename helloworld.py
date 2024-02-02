import math

# hello world e estudo de definição de variáveis

#frase = 'Hello World Python VS Code'
#frase2 = "Estudando Python"
#ano = 2024
#27nome = input ('Digite seu nome')
#idade = int(input('Digite a sua idade: ')) #faz a conversão da string digitada pra int
#soma = idade + 1

#print (frase)
#print (frase2)
#print (frase2 + " " + "para concursos em", ano)
#print ("Olá estudante, já sei que seu nome é " + nome)
#print ("Sua idade é ", idade)
#print (soma)

#trabalhando com strings
palavras = 'palavra'
maiuscula = palavras.upper() 
minuscula = maiuscula.lower()
palavra1 = palavras.capitalize() #-> só a 1a letra maiúscula
metade_palavra = palavras[0:3] #-> pega só as letras indicadas nos índices
ultimas_letras = palavras[3:] #-> pega tudo que estiver além do índice 3
troca = palavras.replace('avra','avrinha')
corta = palavras.strip() #equivalente ao trim() do java
n1=10
n2=5

#print (f'Dividindo {n1} por {n2} o resultado é {n1/n2}') #f (tem que ser sem o espaço depois!) consegue acessar os valores das variáveis e fazer as operações matemáticas

#print (palavras.find('l')) #encontra um caractere na string; -1 é o resultado se buscar caractere que não exista
#print(len(corta)) #tamanho da string

#realizando cálculos
#potenciação => 5**2 = 25
#raiz quadrada -> usa-se bilbioteca específica do python:
raiz = math.sqrt(81)
print(raiz)

#arredondamento -> round(variavel,número de casas)


