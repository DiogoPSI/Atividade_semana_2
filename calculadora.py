num1 = float(input("Introduza um numero: "))
op = input("Introduza operador: ")
num2 = float(input("Introduza um numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Operador Invalido")


