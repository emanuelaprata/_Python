from hashlib import md5

userN={}

def cadastro():
     userN[input("Login: ")] = md5(input("Senha: ").encode("utf8")).hexdigest()


def log(user,passw):
    if user in userN and passw == userN[user]:
        return True
    else:
        return False

def calculadora(op, x, y):
 ini = '0'
 while ini != 0:
     if op == '01':
         print("Bolt: O resultado é: %2f" %(x+y))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '02':
         print("Bolt: O resultado é: %2f" %(x-y))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '03':
         print("Bolt: O resultado é: %2f" %(x*y))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '04':
         print("Bolt: O resultado é: %2f" %(x-y))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '05':
         print("Bolt: O resultado é: %2f" %(x**y))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '06':
         print("Bolt: O resultado é: %2f" %(x**(y/z)))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     elif op == '07':
         print("Bolt: O resultado é: %2f" %(x%z))
         op = input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar")
     else: 
         ini = 0