num1 = int(input("Introduza um numero: "))
num2 = int(input("Introduza um numero: "))

if num1 > num2:
    print(str(num1)+" é o maior numero!")
elif num1 < num2:
    print(str(num2) + " é o maior numero!")
else:
    print("Os numeros são iguais!")

while num1 != num2:
    print(num1)
    num1 += 1

for i in range(num1):
    print(i)
