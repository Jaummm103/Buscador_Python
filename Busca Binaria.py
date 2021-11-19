'''
Nome: João Marcelo Gomes da Silva
RA: G3065C3
Turma: CC2Q04
'''
#Verifica se o elemento está na lista utilizando a busca binária
def buscaBinaria(lista, e): 
    x = 0 
    primeiro = 0
    ultimo = len(lista)-1
    found = False
    #Definindo os parâmetros da busca binária 
    while primeiro<=ultimo and not found:
        x+=1
        midpoint = (primeiro + ultimo)//2
        if lista[midpoint] == e:
            print("Elemento {} localizado".format(midpoint))
            return "Foram feitas {} tentativas para achar o valor".format(x) 
        else:
            if e < lista[midpoint]:
                ultimo = midpoint-1
            else:     
                primeiro = midpoint+1
    print("-1")
    
lista1 = []
n = int(input("Quantos elementos terá a lista?: "))

lista1 = list(range(0, n))
print(lista1)
    
e = int(input("Qual o item que deseja buscar na lista?: "))
print(buscaBinaria(lista1, e))