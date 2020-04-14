a = int ( input() ) #lado a, sem unidades
b = int ( input() ) #lado b, sem unidades
c = int ( input() ) #lado c, sem unidades

if a <= 0 or b <= 0 or c <= 0: #valor inválido se algum dos lados não for maior que zero
    triangulo = 'Valores invalidos na entrada.'
elif a > b + c or b > a + c or c > a + b: #viola condição de existência de 
#                                       'menor distância entre dois pontos é uma reta'
    triangulo = 'Valores fornecidos nao podem formar um triangulo.'
elif a == b + c or b == a + c or c == a + b: #degenerado: um é igual à soma dos outros dois
    triangulo = 'Triangulo degenerado.'
elif a != b and a != c and b != c: #escaleno
    triangulo = 'Triangulo escaleno.'
elif (a == b != c) or (a == c != b) or (b == c != a): #isósceles
    triangulo = 'Triangulo isosceles.'
elif a == b == c: #equilátero não-isósceles
    triangulo = 'Triangulo equilatero.'

print (triangulo)