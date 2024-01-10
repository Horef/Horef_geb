# definitions
limit = 15

G = []
G.append(0)

for i in range(1, limit):
    G.append(i-G[G[i-1]])

print("G:")
for i in range(0, limit):
    print(f"{i}: {G[i]}")

G_flip = []
G_flip.append(0)
G_flip.append(0)

for i in range(1, limit):
    G_flip.append(i-1-G_flip[G_flip[i-2]])

print("G_flip:")
for i in range(0, limit):
    print(f"{i}: {G_flip[i]}")