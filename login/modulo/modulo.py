from hashlib import md5

userN={}

def cadastro():
 a = input("Deseja realizar o cadastro? ")

 while a == 'sim':
     userN[input("Login: ")] = md5(input("Senha: ").encode("utf8")).hexdigest()
     a = input("Deseja realizar um novo cadastro? ")
     print(userN)

"""def login(user,passw):  
 if user in userN and passw == userN[user]:
     print("Acesso autorizado!")
     return True
 else:
     print("Acesso negado!")
     return False
      """

def login(user,passw): 
    i='sim'
    cont=0
    while i == 'sim':
         if user in userN and passw == userN[user]:
             print("Acesso autorizado!")
             break
         elif cont < 3:
             print("Acesso negado!")
             i = input("Tentar novamente?")
             cont += 1
             print(cont)
             user = input("Nome:")
             passw = md5(input("Senha: ").encode("utf8")).hexdigest()
         if cont == 3:
             print("Acesso bloqueado")
     
    #instalar pacotes =
    # pip install nomeDaBiblioteca
    # remorver = 
    # pip uninstall nomeDaBiblioteca





"""          else:
             for i in range (0,3,1):
                 b = input("Tentar novamente?")
                 i=+i
                 if i == 3:
                 return login(user,passw)
                  """
         
         

         




#def login (user,passw):
#    userN= {"manu":"senha1234", "clem":"123", "pedro":"senha12"}
#    if user in userN and passw == userN[user]:
#        return True
#    else:
#        return False

