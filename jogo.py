numero = "12345"
tentativa = ""
conta_tentativas = 0
total_tentativas = 5
perdeu = False

while numero != tentativa and not perdeu:
    if conta_tentativas < total_tentativas:
        tentativa = input("Introduza um numero: ")
        conta_tentativas += 1
    else:
        perdeu = True

if perdeu:
    print("Perdeu!")
else:
    print("Venceu!")
