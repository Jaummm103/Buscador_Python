'''
Nome: João Marcelo Gomes da Silva
RA: G3065C3
Turma: CC2Q04
'''
#Verifica se o elemento está na lista utilizando busca sequencial recursiva 
def buscaSequencialRecursiva(lista, e):
     x = 0
     for i in range(len(lista)):
          x+= 1
          if lista[i]== e:
               print("O Elemento {} foi localizado.".format(e))
               print("{} operações foram realizadas para achar o valor.".format(x)) 
               return i in lista
       
     return -1

    
lista1 = []
n = int(input("Quantos elementos terá a lista?: ")) #Usuário diz o tamanho da lista, seja de 10, 50, 100, 500, 1000, 5000, 10.000, 50.000 ou 100.000

lista1 = list(range(0, n))
print(lista1)
    
e = int(input("Qual o item que deseja buscar na lista?: ")) #Usuário digita o elemento que deseja buscar na lista
print(buscaSequencialRecursiva(lista1, e))
