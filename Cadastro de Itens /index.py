from modulo.mod import *


ini = 's'
ori = input("01. Cadastro de itens. \n02. Valor total em estoque. \n03. Mercadorias que precisam de reposição. \n04. Itens cadastrados \n User:")

while ini == 's':
    if ori == '01':
        cadastro()
        ori = input("01. Cadastro de itens. \n02. Valor total em estoque. \n03. Mercadorias que precisam de reposição. \n04. Itens cadastrados \n User:")
    elif ori == '02':
        print(tabelaValor)
        print('Valor total: ', sum(valorEmEstoque))
        ori = input("01. Cadastro de itens. \n02. Valor total em estoque. \n03. Mercadorias que precisam de reposição. \n04. Itens cadastrados \n User:")
    elif ori == '03':
        print(myTable)
        ori = input("01. Cadastro de itens. \n02. Valor total em estoque. \n03. Mercadorias que precisam de reposição. \n04. Itens cadastrados \n User:")
        print(produtos) 
        ori = input("01. Cadastro de itens. \n02. Valor total em estoque. \n03. Mercadorias que precisam de reposição. \n04. Itens cadastrados \n User:")
    else:
        print("Reiniciando sistema.")    
        break
