# IF - Condicional Simples

nota1 = 8.00
nota2 = 7.00
media = (nota1+nota2)/2

if media >= 7.00:
    print("Aluno aprovado!\n")
    print("Parabens!\n")

print("*********************\n")

# IF - ELSE - Condicional Composto

nota1 = 6.00
nota2 = 7.00
media = (nota1+nota2)/2

if media >= 7.00:
    print("Aluno aprovado!\n")
    print("Parabens!")
else:
    print("Sifu vagabundo. Estude mais.\n")
    print("A media e %f" %media)

print("*********************\n")

# IF - Aninhado

nota1 = 6.00
nota2 = 7.00
media = (nota1+nota2)/2

if media >= 7.00:
    print("Aluno aprovado!\n")
    print("Parabens!")
else:
    if media >= 5.00:
        print("Levou sorte, foi pra recuperacao.")
    else:
        print("Sifu vagabundo. Estude mais.\n")

print("A media e %f" %media)
