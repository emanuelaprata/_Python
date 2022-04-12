
from importlib import import_module
from re import A
from pacotes.mod import *

#BoltDeMilhões
nome = input("Bolt: Olá, qual o seu nome? \n User: ")
print("Bolt: Olá, %s! EU sou o Bolt e vou te ajudar." %(nome))
a = 'i'
i = input("Bolt: O que deseja fazer agora?\n 01. Cadastrar\n 02. Logar\n 03.Saber mais informações.\n 04. Verificar cadastros. \n 05. Calcular valores. \n 05. Sair \n User:")

while a != 0:
    cont = 0
    logou = 0
    if i == 'b':
         i = input("Bolt: O que deseja fazer agora?\n 01. Cadastrar\n 02. Logar\n 03. Saber mais informações.\n 04. Verificar cadastros. \n 06. Sair \n User:")
    elif i == '01' or i == 'a':
          cadastro()
          i = input("Bolt: Deseja realizar um novo cadastro? \n A: Novo Cadastro. \n B: Voltar. \n User: ")
    elif i == '02':
         user = input("Bolt: Ok, vamos começar. \n Digite seu nome de usuário: ")
         senha =  md5(input("Bolt: Agora digite a sua senha: ").encode("utf8")).hexdigest()
         if log(user,senha) == True:
             print("Bolt: Acesso autorizado!")
             i= input("Bolt: Vamos retornar ao menu principal? Digite B \n User:")
             logou +=1  
         elif log(user,senha) == False:
             print("Bolt: Acesso negado.")
             i = input("Bolt: Deseja tentar novamente? \n Não: A \n Sim: Digite 02. \n User:")
             cont =+ 1 
         elif cont >= 3:        
                 print("Bolt: Acesso bloqueado!")
                 i = input("Bolt: A:Desbloquear\n B: Voltar. \n User:")
    elif logou != 0:
         deslog = input("Bolt: Já possui um usuário logado. \n Deseja deslogar? \n A: Sim \n B: Não. \n User:")
         if deslog == 'a':
             logou =-1
             i  = input("Bolt: Deslogue realizado! Deseja retornar ao menu inicial? \n A: Sim \n B: Não \n User:")
         else: 
             i = input("Bolt: Tudo bem! Deseja retornar ao menu inicial? \n A: Sim \n B: Não \n User:")
    elif i == '03':
             print("Infos")
             i = input("Bolt: O que deseja fazer agora? \n Bolt: A: Verificar novo valor \n B: Voltar. \n User:")
    elif i == '04':
         for chave in userN.keys():
             print(f'Bolt: User: {chave} e Password = {userN[chave]}')
    elif i == '05':
         calculadora(input("Bolt: O que deseja fazer? \n 01. Somar \n 02. Subtrair \n 03. Multiplicar \n 04. Dividir \n 05. Potênciação \n 06. Raiz \n 07. Verificar resto da dividsão \n 08: Voltar"), float(input("Valor 01:")), float(input("Valor 02:")))
    elif i == '06':
         i= 0