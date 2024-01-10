# imports
import networkx as nx

# definitions
limit = 25

# variables
F = []
F.append(1)
M = []
M.append(0)

# logic
for i in range(1, limit):
    M.append(i-F[M[i-1]])
    F.append(i-M[F[i-1]])

# output
print("F:")
for i in range(0, limit):
    print(f"{i}: {F[i]}")

print("\nM:")
for i in range(0, limit):
    print(f"{i}: {M[i]}")