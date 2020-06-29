# Verificar o tamanho da String: Funcao len()
s = "pizza"
z = len(s)
print(z)

# Acessar caracteres individuais: da esquerda p/ direita a partir do 0
# Indice negativo imprime da direita p/ esquerda
x = "Taste"
print(x[0])  # imprime T
print(x[1])  # imprime a
print(x[-1]) # imprime e
print(x[-3]) # imprime s

# Slicing
t = "bicicleta"

print(t[:]) # retorna todos os caracteres da string

print(t[1:3]) # retorna os caracteres da posicao 1 ate 2 , a posicao 3
#               e o delimitador.

# CONCATENACAO: usa o caracter de soma (+)
print(s + " portuguesa") # imprime: pizza portuguesa

# Repeticao: usa o caracter de multiplicacao (*)
print(s * 5) # imprime a string s 5 vezes
print((s + " ") * 5)

#                       METODOS em STRINGS
str = "cerveja"
st = "ps4"
print(str.find("vej")) # retorna a posicao de uma substring

print(str.replace("veja", "ca")) # substitui as ocorrencias de ums substring
                                # por outra, porem NAO ALTERA o conteudo da
                                # string original

print(str.upper()) # conversao para maiuscula

print(str.lower()) # conversao para minuscula

print(str.isalpha()) # verifica se o conteudo e ALFABETICO
print(st.isalpha())

print(str.isalnum()) # verifica se o conteudo e ALFANUMERICO
print(st.isalnum())

'''
METODO  str.format

    Realiza uma operacao de formatacao de string.
    A string onde o metodo e chamado pode conter texto literal ou campos de
substituicao delimitados por chaves.
    Esses campos podem conter um indice numerico de um argumento posicional.
'''
a = "banana"
b = 5
c = 3

print( "A {0} custa {1} reais".format(a,b))

print( "Gosto de {0}, mas {1} reais esta caro, pago {2} reais.".format(a,b,c))
