"""
Chiffrer: x^c[n]
Déchiffrer: x'^d[n]
"""
alphabet = {letter: i for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}
alphabet_inversé = {i: letter for letter, i in alphabet.items()}
message = "VIVE LA CRYPTOGRAPHIE".split(" ") #les mots sont séparés et stockés dans un tableau
n = 55
c = 3
d = 27
message_chiffré = ''
for mot in message:
    for lettre in mot:
        chiffré = str(alphabet[lettre]**c % n)
        if len(chiffré) < 2:
            chiffré = "0" + chiffré
        message_chiffré += chiffré
    message_chiffré += " "

print("Message chiffré:",message_chiffré)

message_déchiffré = ''
message_chiffré_tableau = []
# 33143315 2301 27020526252013020126171415 -> [['33', '14', '33', '15'], ['23', '01'], ['27', '02', '05', '26', '25', '20', '13', '02', '01', '26', '17', '14', '15']]
for mot in message_chiffré.split(" "):
    mot_tableau = []
    for i in range(0, len(mot), 2):
        mot_tableau.append(mot[i:i+2])
    message_chiffré_tableau.append(mot_tableau)

for mot in message_chiffré_tableau:
    for chiffre in mot:
        lettre = str(alphabet_inversé[int(chiffre)**d%n])
        message_déchiffré += lettre
    message_déchiffré += " "

print("Message déchiffré:",message_déchiffré)




#Notes: Paula ne crypte pas le message elle le chiffre (car il faut une clé pour déchiffrer le message)
