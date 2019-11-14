#codiding:utf-8

fichier = open("mytext.txt", "r")
contenu = fichier.read()
ligne = fichier.readline
print(contenu)

fichier.close()


with open("mytext.txt", "w") as fichier:
	chiff = 567
	fichier.write(str(chiff))
	fichier.write("Bonjour")