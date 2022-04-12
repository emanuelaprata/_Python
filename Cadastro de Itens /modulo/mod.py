from prettytable import PrettyTable

produtos = []
valorEmEstoque = [] 
lista = 0

#tabelaReposição
myTable = PrettyTable(['Item', 'Qtd minima', 'Qtd Atual'])
#tabelaProdutos
tabelaValor = PrettyTable(['Item', 'Quantidade Atual', 'Valor Unitário', 'Valor total'])

def cadastro():
     #cadastro dos itens
     nome = input("Nome da mercadoria: ")
     quantidadeMin = int(input("Quantidade minima: "))
     quantidadeMax = int(input("Quantidade máxima: "))
     quantidadeAtual = int(input("Quantidade atual: "))
     valorUnitario = float(input("Valor unitário: "))
     #1.1 - Não pode receber uma quantidade maior que a capacidade máxima de mercadorias.
     if quantidadeAtual > quantidadeMax: 
         print("Não é permitido adicionar uma quantidade maior que a capacidade máxima de mercadorias!")
     #1.2 - Não receber valores nagativos ou igual a zero. 
     elif quantidadeMin <= 0 or quantidadeMax <= 0 or quantidadeAtual <=0: 
         print("Não é possível adicionar um valor menor ou igual a zero.") 
     #Quantidade atual não pode passar a quantidade máx permitida 
     elif quantidadeAtual > quantidadeMax:
         print("Não é possível ultrapassar a quantidade máxima permitida.")
    #adiciona o item como um dicionário na lista + realiza a soma dos valores em estoque + cria tabela com a quantidade de itens que precisam ser repostos
     else: 
         lista = dict(Produto = nome, QuantidadeMinima = quantidadeMin, QuantidadeMaxima = quantidadeMax, QuantidadeAtual = quantidadeAtual, ValorUnitario= valorUnitario)
         produtos.append(lista)
         valorTotalItem = valorUnitario*quantidadeAtual
         tabelaValor.add_row([nome,quantidadeAtual,valorUnitario, valorTotalItem])
         #Soma dos valores em estoque
         valorEmEstoque.append(quantidadeAtual*valorUnitario)
         # Quais mercadorias precisam ser repostas em formato de tabela - prettytable
         if quantidadeAtual == quantidadeMin or quantidadeAtual < quantidadeMin+5:
             myTable.add_row([nome,quantidadeMin,quantidadeAtual])

