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

texto1 = '''Seu trabalho de stand-up tem sido um fio condutor de sua carreira, como pode se ver pelo sucesso de seu show
 (e o DVD subsequente) Robin Williams: Live on Broadway (2002). Obteve em 2004 o 13º lugar na lista de "100 maiores 
 [comediantes] stand-up de todos os tempos" do canal Comedy Central.
Após ser encorajado por sua amiga, a também comediante Whoopi Goldberg, decidiu aceitar uma participação especial na 
série Star Trek: The Next Generation, em 1991, no episódio "A Matter of Time", porém teve que cancelar sua aparição 
devido a um conflito de calendário; Matt Frewer assumiu seu lugar no papel do professor Berlingoff Rasmussen,
um viajante do tempo trapaceiro.
Williams também apareceu, em 2000, num episódio da versão americana de Whose Line Is It Anyway?.
Durante um jogo chamado "Scenes from a Hat" ("cenas de um chapéu"), a cena "What Robin Williams is thinking right now"
("O que Robin Williams está pensando agora") foi criada, e Williams declarou: "I have a career.
What the hell am I doing here?" ("Eu tenho uma carreira. Que diabos estou fazendo aqui agora?")
'''

texto2 = '''De Niro é descendente de italianos,[2][3] sendo também descendente de irlandeses, alemães e holandeses.
[carece de fontes] Apesar disso, o ator diz que se identifica "mais com o seu lado italiano que com os outros lados".
Em outubro de 2004 cancelou uma apresentação em Roma, após as autoridades italianas o terem acusado
de apresentar estereótipos negativos da sua ascendência nos seus filmes.
Em dezembro do mesmo ano voltou a Roma para apresentar pela primeira vez uma exposição de arte do seu falecido pai.
As mesmas autoridades, surpreendidas, disseram que não guardavam ressentimentos.[carece de fontes]
de Niro em 2008
O ator tem verdadeira paixão por Nova Iorque, particularmente pelo bairro que habita, TriBeCa, na baixa Manhattan.
Desde 1989, investe na região, tendo aberto lá um restaurante, uma produtora, e, principalmente, criado o festival 
de cinema independente, TriBeCa Film Festival, festival que vem ganhando importância a cada ano que passa.
'''


# print(Counter(texto1.lower()))
# aparicoes = Counter(texto1.lower())
#
# print(aparicoes.values())
# total_de_caracteres = sum(aparicoes.values())

# for letra, frequencia in aparicoes.items():
#     tupla = (letra, frequencia / total_de_caracteres)
#     print(tupla)


# proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
# proporcoes = dict(proporcoes)
#
# proporcoes = Counter(dict(proporcoes))
# proporcoes.most_common(10)


def analisa_frequencia_de_letras(texto):

    aparece = Counter(texto.lower())
    total_de_caracteres = sum(aparece.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparece.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)

    for caractere, proporcao in mais_comuns:
        print('{} => {:.2f}%'.format(caractere, proporcao * 100))


print(analisa_frequencia_de_letras(texto1))
print(analisa_frequencia_de_letras(texto2))
