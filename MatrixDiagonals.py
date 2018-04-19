# Recebe o input de uma matriz quadrada e calcula a diferenca entre suas diagonais

n = int(raw_input("Entre o numero de linhas ou colunas da sua matriz quadrada: "))
x = []
for i in range(n):
    for j in range(n):
        x.append(int(input("Linha {0}, Coluna {1}: ".format(i, j))))
    print("\n")
y = [[0 for p in range(n)] for q in range(n)]
k = 0
for i in range(n):
    for j in range(n):
        y[i][j] = x[k]
        k += 1
print("Abaixo a matriz inserida montada de maneira grafica:")
for i in range(n):
    print(y[i])
print("\nDiagonal 1")
print([y[i][i] for i in range(n)])
u = sum([y[i][i] for i in range(n)])
print("Soma: {0}".format(u))
print("\nDiagonal 2")
print([y[i][n - 1 - i] for i in range(n)])
v = sum([y[i][n - 1 - i] for i in range(n)])
print("Soma: {0}".format(v))
print("A diferenca entre as duas diagonais e :  |{0}-{1}|={2}".format(u, v, abs(u-v)))
