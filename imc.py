
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso /(altura * altura)

if imc <= 18.5:
    print(f"Abaixo do peso! IMC de {imc:.2f}")

elif (imc >= 18.5) and (imc <= 24.9):
    print(f"Peso normal! IMC de {imc:.2f}")

elif (imc >= 24.9) and (imc<= 29.9):
    print(f"Sobrepeso! IMC de {imc:.2f}")

elif (imc >= 30) and (imc<= 34.9):
    print(f"Obesidade grau I, IMC de {imc:.2f}")

elif (imc >= 35) and (imc<= 39.9):
    print(f"Obesidade grau II, IMC de {imc:.2f}")

elif imc >= 40:
    print(f"Obesidade grau III, IMC de {imc:.2f}")
    print("Gordããaaaaooo!!!")


    