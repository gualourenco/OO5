from collections import defaultdict, Counter

class Conta:

    def __init__(self):
        print('Impromindo uma conta')


usuarios_ds = [15, 23, 43, 56]
usuarios_ml = [13, 23, 56, 42]
assistiram = []
print(assistiram.extend(usuarios_ds))
assistiram.extend(usuarios_ds)
print(assistiram)
assistiram.pop()
assistiram.pop()
assistiram.pop()
assistiram.pop()
assistiram = usuarios_ds.copy()
assistiram.extend(usuarios_ml)
print(len(assistiram))

print(set(assistiram))

conj_set = [1, -3, 5, -8, 5, 6, 7]
print(conj_set)

for usuario in set(assistiram):
    print(usuario)

print(set(usuarios_ds) | set(usuarios_ml))

usuarios_ml = {13, 23, 56, 42}
usuarios_ds = {15, 23, 43, 56}

print(usuarios_ds & usuarios_ml)
print(usuarios_ds - usuarios_ml)
fez_ds_mas_nfez_ml = usuarios_ds - usuarios_ml
print(15 in fez_ds_mas_nfez_ml)
print(23 in fez_ds_mas_nfez_ml)
fez_ds_e_ml = usuarios_ds & usuarios_ml
fez_ds_ou_ml = usuarios_ds ^ usuarios_ml
print(fez_ds_ou_ml)

usuarios = {1, 34, 17, 52, 5, 76, 13}
usuarios.add(17)
usuarios.add(765)
print(usuarios)
frozenset(usuarios)

print(type(usuarios))
meu_texto = 'Bem vindo meu nome é Guilherme e tenho meu cachorro e gosto muito de cachorro'
meu_texto.split()
print(set(meu_texto.split()))

aparicoes = {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
print(type(aparicoes))
print(aparicoes['Guilherme'])
print(aparicoes['cachorro'])
print(aparicoes.get('xpto', 0))
print(aparicoes.get('cachorro', 0))

aparice = dict(Guilherme=2, cachorro=1)

aparicoes['Carlos'] = 1
print(aparicoes)
aparicoes['Carlos'] = 2
print(aparicoes)
del aparicoes['Carlos']
print(aparicoes)

print('cachorro' in aparicoes)
print('Carlos' in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, '=', valor)

print(['palavra {}'.format(chave) for chave in aparicoes.keys()])


print(meu_texto)
meu_texto.lower()
meu_texto = meu_texto.lower()
aparicoes2 = {}
print(aparicoes2)

print(aparicoes)

meu_texto.split()
for palavra in meu_texto.split():
    ate_agora = aparicoes2.get(palavra, 0)
    aparicoes2[palavra] = ate_agora + 1
print(aparicoes2)

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)

dicionario = defaultdict(int)
print(dicionario['guilherme'])

dicionario['guilherme'] = 15
print(dicionario['guilherme'])

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

contas = defaultdict(Conta)
print(contas[15])

aparicoes3 = Counter(meu_texto)
print(aparicoes3)
