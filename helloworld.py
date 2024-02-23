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
#print(raiz)

#arredondamento -> round(variavel,número de casas)

#operadores lógicos no python:

'''
    True/False (case sensitive, 1a letra maiúscula)
    and/& (ex: a and b)
    or/ |
    not 
'''

#operadores relacionais
'''
    == / != comparação de valores     
'''

#operadores condicionais
'''
    if 5>4 :  => ':' inicia um bloco. É equivalente ao then. Se não estiver identado o que deve ser feito dentro do if, não vai funcionar. não existe {}
        print('True')

    if 5>4 :
        comando
    else:
        comando

    if (condicao1) and/or (condicao2):
        comando
    
'''
# dicionários -> é chave-valor
coleta = {'Aedes aegypt': 32, 'Aedes albopictus':22, 'Anopheles darlingi':14} #nome e quantidade de amostras coletadas, por exemplo.

#adicionando nova entrada no dicionário:
coleta ['Rhodnius montenegrensis'] = 11

#del(coleta) apaga a variável inteira

#del(coleta)['Rhodnius montenegrensis']
#print(coleta.items()) ->imprime o dicionário completo

#print(coleta.keys()) ->traz só as chaves guardadas no dicionário
#print(coleta.values()) ->traz só os valores guardadas no dicionário

coleta2 = {'Anopheles gambiae':13, 'Anopheles deaneorum':14}

#atualizando um dicionário a partir de outro dicionário
coleta.update(coleta2)

#percorrendo um dicionário
#for especie, num_especimens in coleta.items():  
 #   print(f'Espécie: {especie}, Número de especimens coletados: {num_especimens} ')

#trabalhando com sets
biomoleculas = ('proteína', 'ácido nucleico', 'carboidrato', 'lipídio', 'ácido nucleico', 'carboidrato', 'carboidrato','carboidrato')
#print(set(biomoleculas)) -> trará os elementos 1x, sem repetir nenhum

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)  #exibe a interseção entre os conjuntos
print(c1.difference(c2)) #exibe a diferença entre os conjuntos
