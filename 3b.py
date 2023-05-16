alphabet = {letter: i for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}
alphabet_inversé = {i: letter for letter, i in alphabet.items()}
m = 24
n = 39
c = 29
d = 5
message_chiffré = "28 01 12 21 11 12 03 28 05"
chiffres = [int(x) for x in message_chiffré.split()] # [28, 1, 12, 21, 11, 12, 3, 28, 5]
print("Message déchiffré:",end=" ")
for chiffre in chiffres:
    print(alphabet_inversé[(chiffre**d)%n],end="") #x^d[n]
