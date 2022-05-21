N, K=input().split()
N, K=int(N), int(K)

list=(input().split()) 

for x in range(len(list)):
    (list[x])=int(list[x])

def laminas_repetidas(lista):
    copias=len(list)-len(set(list))
    return copias

def laminas_repetidas_memoria(listas):
    cont=0
    memoria=K
    if memoria == 2:
        if list[0] == list[1]:
            cont+=1
    for i in list:
        if memoria < len(list):
            if i == list[memoria]:
                cont+=1
                memoria+=1
            else:
                memoria+=1
        else:
            break
    return cont

copias_detec=laminas_repetidas(list)
copias_detec_maquina=laminas_repetidas_memoria(list)
print(copias_detec, copias_detec_maquina)  