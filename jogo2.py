numero = "12345"
tentativa = ""
total_tentativas = 5
perdeu = False

for conta_tentativas in range(total_tentativas+1):
    if conta_tentativas < total_tentativas:
        tentativa = input("Introduza um numero: ")
        if tentativa == numero:
            break
    else:
        perdeu = True

if perdeu:
    print("Perdeu!")
else:
    print("Venceu!")
