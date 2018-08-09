n1 = (input("Digite a Seu nome: "))
n2 = print("Prazer eu sou a assistente virtual",n1)
n3 = print("Você veio aqui pra saber o seu resultado, so me seguir que você vai saber.")
n4 = input("ok ? ")
n5 = float(input("Digite a nota do 1° Bimestre: "))
n6 = float(input("Digite a nota do 2° Bimestre: "))
n7 = float(input("Digite a nota do 3° Bimestre: "))
n8 = float(input("Digite a nota do 4° Bimestre: "))
n9 = (n5 + n6 + n7 + n8)
n10 = n9/4
print("Nota do 1°>> [{}]\nNota do 2°>> [{}]\nNata 3°>> [{}]\nNota do 4°>> [{}]\n total:>> [{}]\nA media:>> [{}]".format(n5, n6, n7, n8, n9, n10,))

n11 = print("\n<<<<<Raiz Quadrada>>>>>>")
n12 = int(input("Digite um numero: "))
n13 = n12 ** (1/2)
n14 = print("A Raiz quadrada de {} e {:.2f}".format(n12,n13,))

n15 = print("\n<<<Dobro>>>")
n16 = int(input("Digite um numero: "))
n17 = n16 * 2
n18 = print("O dobro de {} vale [{}]".format(n16, n17,))

n19 = print("\n<<<Triplo>>>")
n20 = int(input("Digite um numero: "))
n21 = n20 * 3
n22 = print("O triplo de {} vale {}".format(n20, n21,))

n30 = print('\n<<Numero Inteiro>>')
from math import trunc
n23 = float(input("Digite um numero: "))
n24 = print("O numero digitado {} e a porção inteira <<{}>>".format(n23,trunc(n23)))

n25 = print('\nQuantado de medidas Cm e C :')
n26 = float(input('Digite a Largura: '))
n27 = float(input('Digite o Comprimento: '))
n28 = n26 * n27
n29 = (print('A largura e {}m o Comprimento e {}m Metros {:.1f}m'.format(n26, n27, n28,)))

