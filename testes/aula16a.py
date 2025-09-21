# Variáveis compostas => tuplas, listas, dicionários

########################
#        TUPLAS        #
########################

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

print(lanche[1:])  # mostra tudo a partir do segundo item ([1:])
print(lanche[-1])  # mostra apenas o último item 
print(lanche[:2])  # mostra tudo até antes do terceiro ([:2])

print(f'Comprimento da tupla: {len(lanche)}') # mostra o comprimento (4) da tupla

for c in lanche:
    print(c)