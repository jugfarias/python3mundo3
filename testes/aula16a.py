# Variáveis compostas => tuplas, listas, dicionários

########################
#        TUPLAS        #
########################

# tuplas são imutáveis 

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')   # pode setr criado sem ()

print(lanche[1:])  # mostra tudo a partir do segundo item ([1:])
print(lanche[-1])  # mostra apenas o último item 
print(lanche[:2])  # mostra tudo até antes do terceiro ([:2])

print(f'Comprimento da tupla: {len(lanche)}') # mostra o comprimento (4) da tupla

for c in lanche:
    print(c)

# lanche[1] = 'refri'  # dá erro, tupla não pode ser mudada

print(lanche)