#for i in range (100,120,+1):
#    if i%2 != 0:
#        print(i)

#negativos = []
#for numero in range(0,10,1):
#    n = int(input("Digite um número: "))
#    if n < 0:
#     negativos.append(n)
#print(len(negativos))

#dentro = []
#fora = [] 
#for valor in range (0,10,1):
#    numero = int(input("Digite um valor: "))
#    if numero > 9 and numero < 21:
#        dentro.append(numero)
#    else:
#        fora.append(numero)
#print(len(dentro))
#print(len(fora))

#inf = []
#for valor in range (0,10,1):
#    numero = int(input("Digite um valor: "))
#    if numero < 40:
#        inf.append(numero)
#print(sum(inf))

#**************** METODOS ********************

#assinatura do método sem argumento (procedure - não tem retorno), só defini
#def Menu():
#    print("Bem vindo!")
#    print("1 - Cadastrar")
#    print("2 - Editar")
#    print("3 - Excluir")
#    print("4 - Sair")

#Menu()


#pegou a variavel user que só funciona dentro desse bloco
#assinatura do método com argumentos (procedure - não tem retorno), só defini
#def MenuDois(user):
#    print("Bem vindo(a),%s!" %(user))
#    print("1 - Cadastrar")
#    print("2 - Editar")
#    print("3 - Excluir")
#    print("4 - Sair")

#MenuDois(input("Digite seu nome:"))

#com retorno

#def somarValores(v1,v2):
#    return v1+v2
#print(somarValores(2,3))

#metodo com retorno não pode ter entrada ou saida de dados, deve ocorrer na aplicação, não no método.

#def media(v1,v2):
#    a=[]
#    for i in range (v1+1,v2,1):
#        a.append(i)
#        b=len(a)+1
#        a.append(i)
#    return (sum(a))/b

#u = int(input("Valor:"))
#d = int(input("Valor:"))
#print(media(u,d))

#**********************************MODULOS**********************************************
 

#from hashlib import md5
#userN={}
#userN[input("Login: ")] = md5(input("Senha: ").encode("utf8")).hexdigest()
#print(userN)

from login.modulo.modulo import *

cadastro()

i='sim'
while i =='sim':
     if login(
           input("User:"), 
           md5(input("Senha: ").encode("utf8")).hexdigest()
     ) == True:
           print("Acesso autorizado!")
     else:
          i=("Deseja tentar novamente?")

#from hashlib import md5
#texto = "senha1243".encode("utf8")
#hash = md5(texto).hexdigest()

#print(texto)
#print(hash)
#print(hash == texto)