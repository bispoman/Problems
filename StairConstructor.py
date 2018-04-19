#Construtor de escadas
#Desenha uma escada do tamanho solicitado pelo usuario via terminal

steps = raw_input("Digite o tamanho da escada: ")
steps = int(steps)
steps = steps - 1
hashStep = 1

while steps >= 0:
    print " "*steps, "#"*hashStep
    steps -= 1
    hashStep += 1
