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
