
"""
def verification(tab:list)->bool:
    my_number = tab[0]
    for element in tab:
        if my_number <= element:
            my_number = element
        else:
            return False
    return True


def maxi_et_indice(tab):
    arr = []
    maxi = tab[0]
    for e in tab :
        if e > maxi:
            maxi = e
    for i in range(len(tab)):
        if tab[i] == maxi:
            arr.append(i)
    return(maxi,arr)


print(maxi_et_indice([1,2,3,55,2,3,55,0]))


def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
         x = pile_2.pop()
         pile_1.append(x)
    return pile_1



print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))

"""


"""

def moyenne(tab:list):
    divise = 0
    somme_produit = 0
    for element,val in tab:
        divise = divise + val
        somme_produit += element * val
    if somme_produit == 0 :
        return None
    else:
        return somme_produit / divise




print(moyenne(([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])))


"""

"""
def a_doublon(tab):
    arr = []
    tableau = []
    for elem in tab:
        tableau.append(elem)
        if elem not in arr:
            arr.append(elem)
    a = len(arr)
    b = len(tableau)
    if a == b:
        return False
    return True
"""
"""
def a_doublon(tab):
    arr = []
    for elem in tab:
        if elem not in arr:
            arr.append(elem)
    a = len(arr)
    b = len(tab)
    if a == b:
        return False
    return True


print(a_doublon([1,2,3,4,5,6]))

"""
#sujet 30
"""
def moyenne(tab:list):
    a = 0
    index = 0
    for element in tab:
        a += element
        index +=1
    return a / index

print(moyenne([1.0]))

print( moyenne([1.0, 2.0, 4.0]))
"""
"""
def binaire(a):
 bin_a = ""
 a = a // 2
 while a > 0 :
    bin_a = str(a%2) + bin_a
    a = a // 2
 return bin_a

print(binaire(83))





#CORRIGER BINAIRE :
def binaire ( a ):
    bin_a = str ( a % 2 )
    a = a // 2
    while a != 0 :
        bin_a = str ( a % 2 ) + bin_a
        a = a // 2
    return bin_a


"""
#SUJET 40
"""

def nombre_de_mots(phrase:str):
    compteur = 0
    new_phrase = phrase.split()
    for e in new_phrase:
        compteur += 1
    return compteur
"""

"""
def nombre_de_mots(phrase:str):
    compteur = 0
    for element in phrase:
        if element == ' ':
            compteur += 1
    return compteur + 1

print(nombre_de_mots('Fin.'))
"""
"""
class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si le sous-arbre droit est non
vide
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si le sous-arbre gauche est non
vide
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de
recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.valeur :
            if self.gaucheExiste():
                 self.gauche.inserer(cle)
            else:
                self.gauche =  Noeud(cle)
        elif cle >  self.valeur :
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
       arbre.inserer(cle)
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())
"""
#Sujet 37
"""
def recherche(elt,tab):
    compteur = 0
    if elt not in tab:
        return -1

    for i in range(len(tab)):
        if tab[i] == elt:
           compteur = i
    return compteur


print( recherche(1, [8, 1, 10, 1, 7, 1, 8]))
"""
"""
class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        if self.liste_octet()[3] == 254 or self.liste_octet()[3] == 0 :
                return True
        return False


    def adresse_suivante(self):
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False




adresse1 = AdresseIP("192.168.0.1")

adresse2 = AdresseIP('192.168.0.2')

adresse3 = AdresseIP('192.168.0.0')

print(adresse2.est_reservee())
print(adresse2.adresse_suivante().adresse)
print(adresse3.liste_octet()[3])
"""


"""
"""
"""
#Sujet 23
def multiplication(n1:int,n2:int):
    return n1 * n2

print(multiplication(3, 5))

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m)
    else:
        return m


print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) )


print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))



"""
#sujet 15

"""
def mini(releve,date):
    c = 0
    minim = releve[0]
    for element in releve:
        if element < minim:
            minim = element


""

def mini(releve,date):
    c = 0
    minim = releve[0]
    for idx,element in enumerate(releve):
        if element < minim:
            minim = element
            index = idx
    for i in range(len(date)):
        if i == index:
            my_date = date[i]
    return minim,my_date
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


print(mini(t_moy, annees))

"""

"""
def inverse_chaine(chaine):
    result = chaine
    for caractere in chaine:
       result = chaine[::-1]
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)   #bac et cab
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


print( inverse_chaine('bac'))



print(est_palindrome('NSI'))

print(est_palindrome('ISN-NSI'))

print(est_nbre_palindrome(214312) )



print(est_nbre_palindrome(213312))


"""
#SUJET 28
"""
def moyenne(tab:list)->float:
    add = 0
    count = 0
    for element in tab:
        add += element
        count += 1
    return add/count

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

print(moyenne([1,2]))
print(moyenne([1, 2, 3, 4, 5, 6, 7]))

"""
"""

def dichotomie(tab, x):
        #tab : tableau trié dans l’ordre croissant
        #x : nombre entier
        #La fonction renvoie True si tab contient x et False sinon

    # cas du tableau vide
    if tab == []:
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2

    debut = 0
    fin = len(tab) -1
    m = (debut + fin) // 2
    while debut <= fin:
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
        m = (debut + fin) // 2
    return False, 3


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) )
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
"""
#Sujet 39
"""
def fibonacci(n : int)->int:
    if n <= 2:
        return 1
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n


print( fibonacci(5))

"""
"""
def pantheon(eleves, notes):

    note_maxi = 0

    meilleurs_eleves =  []

    for i in range(len(notes)):

        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])

        elif notes[i] > note_maxi:

            note_maxi = notes[i]

            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(pantheon(eleves_nsi, notes_nsi))
#print(pantheon([],[]) )
"""


#Sujet 12
"""
class ABR:




    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def ajoute(self,cle,a):
        if cle == self.cle:
            return a
        elif cle > self.cle:
            if self.droit.cle is not None:
                ajoute(cle,self.droit)
        else:
            if self.gauche.cle is not None:
                ajoute(cle,self.gauche)


n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)

#abr1.ajoute(5,abr1)

"""




"""



#sujet 7





def fusion(tab1,tab2):
    if tab1 != [] and tab2 != []:
        arr = [] + tab1 + tab2
    i = 0
    while i < len(arr)-1:
        j = i + 1
        min = i
        while j <= len(arr)-1:
            if arr[j]<=arr[min]:
                min = j
            j += 1
        if min != i:
            arr[i],arr[min] = arr[min],arr[i]
        i += 1
    return arr

print(fusion([4], [2, 6]) )


"""

#sujet 41
"""
"""
"""
def recherche(caractere,chaine):
    c = 0
    for e in chaine :
        if e == caractere:
            c += 1
    return c


valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
       return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang+1)





print(rendu_glouton(67, 0) )

"""

#sujet 25
"""
def enumere(L:list)->dict:
    dico = {}
    for i in range(len(L)):
        if L[i] in dico:
            dico[L[i]].append(i)
        else:
            dico[L[i]] = [i]

    return dico





print(enumere([1, 1, 2, 3, 2, 1]))






class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
        if arbre != None:
            parcours(arbre.fg, liste)
            liste.append(arbre.v)
            parcours(arbre.fd, liste)
        return liste



def insere(arbre, cle):
        if cle < arbre.v :
            if arbre.fg != None:
                insere(arbre.fg, cle)
            else:
                arbre.fg = Arbre(cle)
        else:
            if arbre.fd != None:
                insere(arbre.fd, cle)
            else:
                arbre.fd = Arbre(cle)


Abr = Arbre(5)
a1 = Arbre(2)
a2 = Arbre(3)
a3 = Arbre(7)

Abr.fg = a1
Abr.fd = a3
Abr.fg.fd = a2

insere(Abr, 1)
insere(Abr, 4)
insere(Abr, 6)
insere(Abr, 8)

print(parcours(Abr, []))


"""

#Sujet 19
"""

def recherche(tab:list,n:int):
        debut = 0
        fin = len(tab)-1
        ind = -1
        while debut <= fin and ind == -1:
            mid = (debut+fin)//2
            if tab[mid] == n:
                ind = mid
            elif n > tab[mid]:
                debut = mid + 1
            else:
                fin = mid - 1
        return ind

print( recherche([2, 3, 4, 6, 7], 5))

print( recherche([2, 3, 4, 5, 6], 5))


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + ALPHABET[indice]
    return resultat



print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) )


"""


#Sujet 24
"""
def occ(mot,l):
    d = 0
    for e in mot:
         if e == l:
            d+=1
    return d

def nbr_occurences(chaine:str)->dict:
    dico = {}
    compteur = 0
    for e in chaine:
        dico[e] = occ(chaine,e)
    return dico

"""

"""
def nbr_occurences(chaine:str)->dict:
    dico = {}
    for e in chaine:
        if e in dico:
            dico[e] = dico[e] + 1
        else:
            dico[e] = 1
    return dico

print(nbr_occurences("Hello world"))

"""
"""

def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
      lst12[i] = lst1[i1]
      i1 = i1 + 1
      i = i + 1
    while i2 < n2:
      lst12[i] = lst2[i2]
      i2 = i2 + 1
      i = i + 1
    return lst12




print(fusion([1, 6, 10], [0, 7, 8, 9]))


"""














