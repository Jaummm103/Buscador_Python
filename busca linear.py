'''
Nome: João Marcelo Gomes da Silva
RA: G3065C3
Turma: CC2Q04
'''

def linearSearchLast(L,e):
  e_posicao= -1
  tamanho_lista= len(L)
  for indice_lista in range(tamanho_lista):
    if L[indice_lista] == e:
      e_posicao = indice_lista
  return e_posicao

lista= []

n = int(input("Digite o limite da sua lista :")) #criar a lista até certo valor

for num in range(1, n+1): # o n com +1 vai permanecer com o mesmo elemento que digitar pois o range ele não chega no valor digitado
    lista.append(num)
    
print (lista)   

procure_elemento = int(input("Qual o item que deseja buscar na lista?: "))

resultado= linearSearchLast(lista, procure_elemento) #o resultado vai mostrar o indice do elemento

print(resultado)