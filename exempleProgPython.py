def Valeurs(var_a,var_b):
    print("Voici le résultat de a + b :" + str(var_c) + "!")
    
print("Donnez moi la valeur de a")

var_a = input ()

print("Donnez moi la valeur de b")

var_b = input ()

var_c = int(var_a) + int(var_b)

var_d = 1 + 1

var_e = 1
var_f = 1
var_g = var_e + var_f

Valeurs(var_a,var_b)

nom = 'Jean'
index = 0
while index < len(nom):
    print (nom[index])
    index = index +1
    
nom = 'Jean'
for caract in nom:
    print (caract)
    
liste = ['chien','chat','crocodile']
for animal in liste: 
    print ('longueur de la chaîne', animal, '=', len(animal))
    
car = 1
voyelles = 10
if car < voyelles:
    print (car, "est inferieur a voyelle")
