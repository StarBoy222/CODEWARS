# import random

# def longest (s1,s2):
#     i = random.randint(100)
#     s1 = .sort(list(s1))
#     s2 = .sort(list(s2))
#     s1.sort()
#     s2.sort()
    
#     lista_caracteres = s1 + s2
#     nueva_lista = []
#     for l in range(i):
#         caracter_random = random.choice(lista_caracteres)
#         nueva_lista.append(caracter_random)
    
#     nueva_lista = ''.join(nueva_lista)
#     print(nueva_lista)

#LA PRIMERA SOLUCION PUEDE SERVIR, SIN EMBARGO PARA
#CODEWARS NO. POR LO QUE LA SOLUCION CORRECTA PARA CODEWARS
#ES LA SIGUIENTE


def longest(s1, s2):
    res = s1 + s2
    res = list(res)
    res = dict.fromkeys(res)
    res = sorted(res)
    res = ''.join(res)
    return res

    