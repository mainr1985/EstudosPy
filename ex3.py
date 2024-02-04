'''
Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
'''
idade = int (input ('Informe a sua idade: '))
if (idade > 0) and (idade <=12):
    print ('O(a) usuário(a) é uma criança')
else:
    if (idade>12) and (idade<=17):
        print ('O(a) usuário(a) é um adolescente')
    else:
        if idade>18:
            print ('O(a) usuário(a) é um adulto')
        else:
            if (idade)<0 :
                print ('Idade inválida')