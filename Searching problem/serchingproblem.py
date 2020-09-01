""" definirea problemei """
from collections import namedtuple
import time
from math import sqrt

fisiere_input = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt"]

"""
functia de citire:
param: file_path - calea fisierul din care se vor citi datele
variabile folosite:
lista = o lista de liste in care voi retine copiii si pozitionarea acestora in banci
suparati = o lista care retine perechile de copii care sunt suparati
nod_start = retine copilul de la care pornim (un tuplu care contine: numele si pozitia in clasa)
nod_scop = retine copilul la care trebuie sa ajungem (un tuplu care contine: numele si pozitia in clasa)
"""

def citire(file_path):
    lista = [ ]
    nod_start = Copil("", 0, 0)
    nod_scop = Copil("", 0, 0)
    suparati = [ ]
    with open(file_path) as fin:
        for line in fin:
            nume = line.split()
            if nume[0] == 'suparati':
                for line1 in fin:
                    nume1 = line1.split()
                    if nume1[ 0 ] == 'mesaj:':
                        start = nume1[ 1 ]
                        final = nume1[ 3 ]
                    else:
                        suparati.append(nume1)
            else:
                lista.append(nume)
        for i in range(len(lista)):
            for j in range(6):
                if lista[i][j] != "liber":
                    if lista[i][j] == start:
                        nod_start = Copil(lista[i][j], i, j)
                    if lista[i][j] == final:
                        nod_scop = Copil(lista[i][j], i, j)
    return lista, suparati, nod_start, nod_scop


""" 
functia euristica1:
param: pozx, pozy - pozitia in clasa a copilului curent
returneaza distanta euclidiana dintre nodul curent si nodul scop
"""

def euristica1(pozx, pozy):
	return round(sqrt((nod_scop.pozx - pozx) ** 2 + (nod_scop.pozy - pozy) ** 2),2)

"""
functia euristica2:
param: pozx, pozy - pozitia in clasa a copilului curent 
returneaza distanta pe axele Ox si Oy intre nodul curent si nodul scop
"""

def euristica2(pozx, pozy):
    return abs(nod_scop.pozx - pozx) + abs(nod_scop.pozy - pozy)

"""
functia euristica3:
param: pozx, pozy - pozitia in clasa a copilului curent 
returneaza numarul de copiii dintre nodul curent si nodul scop, de la nodul curent pana la ultimul copil
de pe coloana sa, mergand in sus si jos pe linii pana la nodul scop
"""

def euristica3(pozx, pozy):
    if len(lista) is None:
        nr_linii = 1
    else:
        nr_linii = len(lista)
    d = nr_linii - pozx + 1
    d += (nod_scop.pozy - pozy - 1) * nr_linii
    d += nr_linii - nod_scop.pozy + 1

    return d

class Nod:
    def __init__(self, nume, pozx, pozy):
        self.nume = nume
        self.pozx = pozx
        self.pozy = pozy
        self.info = (nume, pozx, pozy)
        self.h = euristica2(pozx, pozy)

    def __str__ (self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__ (self):
        return f"({self.info}, h={self.h})"


class Arc:
    def __init__(self, capat, varf, cost):
        self.capat = capat	# de unde pleaca muchia
        self.varf = varf	# unde ajunge muchia
        self.cost = cost	# cosul g al muchiei

class Problema:
    def __init__(self):
        self.nod_start = Nod(nod_start.nume, nod_start.pozx, nod_start.pozy)  # de tip Nod
        self.nod_scop = Nod(nod_scop.nume, nod_scop.pozx, nod_scop.pozy)  # doar info (fara h)


    def cauta_nod_nume(self, info):
        """Stiind doar informatia "info" a unui nod,
        trebuie sa returnati fie obiectul de tip Nod care are acea informatie,
        fie None, daca nu exista niciun nod cu acea informatie."""
        ### TO DO ... DONE
        for nod in self.noduri:
            if nod.info == info:
                return nod
        return None



""" Sfarsit definire problema """



""" Clase folosite in algoritmul A* """

class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf

    """

    problema=None	# atribut al clasei (se suprascrie jos in __main__)


    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  	# obiect de tip Nod
        self.parinte = parinte  	# obiect de tip NodParcurgere
        self.g = g  	# costul drumului de la radacina pana la nodul curent
        if f is None :
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f


    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None :
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum


    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina
            Se compara doar informatiile nodurilor (proprietatea info)
            Returnati True sau False.

            "nod" este obiect de tip Nod (are atributul "nod.info")
            "self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        ### TO DO ... DONE
        nod_c = self
        while nod_c is not None :
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False


    """
    functia expandeaza
    pentru a genera succesorii m-am folosit de pozitiile copiilor in banci astfel:
    --- cel de pe coloana para poate sa dea doar in dreapta, sus si jos, cu exceptia cazului cand se afla
    pe ultimele doua linii ale matricei (lista de liste), cand poate da biletelul si celui din stanga sa
    --- cel de pe coloana impara poate sa dea doar in stanga, sus si jos, cu exceptia cazului cand se afla 
    pe ultimele doua linii ale matricei(lista de liste), cand poate da biletelul di celui din dreapta sa
    --- de asemenea, am verificat cazul in care se afla pe prima sau ultima linie, prima sau ultima coloana, cazul
    in care nu trebuie sa generam succesorul care este deja parintele nodului - de unde a venit biletul, dar si cazul
    in care bancile valide pentru un nod pot fi libere
    
    """
    def expandeaza(self):
        """Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
        si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
        sau lista vida, daca nu exista niciunul.
        (Fiecare tuplu contine un obiect de tip Nod si un numar.)
        """
        ### TO DO ... DONE
        l_succesori = []
        nume, pozx, pozy = self.nod_graf.info
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info[0]
        for i in range(len(lista)):
            for j in range(6):
                if nume == lista[i][j]:
                    if i != 0:
                        if lista[ i - 1][ j] != 'liber' and ([ lista[i -1][j], nume ] not in suparati and
                                                             [nume,lista[i -1][j]] not in suparati) and \
                                parinte != lista[i-1][j]:
                            l_succesori.append((Nod(lista[i-1][j], i-1, j ), 1))
                    if j % 2 == 0:
                        if j+1 <= 5:
                            if lista[i][j+1] != 'liber' and ([lista[i][j+1],nume] not in suparati and
                                                             [nume, lista[i][j+1]] not in suparati) and \
                                    parinte != lista[i][j+1]:
                                l_succesori.append((Nod(lista[i][j+1],i, j+1),1))
                        if i+1 < len(lista):
                            if lista[i+1][j] != 'liber' and ([lista[i+1][j],nume] not in suparati and
                                                             [nume, lista[i+1][j]] not in suparati) and \
                                    parinte != lista[i+1][j]:
                                l_succesori.append((Nod(lista[i+1][j],i + 1, j),1))
                        if i >= len(lista) - 2 :
                            if j - 1 >= 0:
                                if lista[ i ][ j - 1 ] != 'liber' and ([ lista[i][j - 1], nume ] not in suparati
                                                                       and [ nume, lista[ i ][j - 1 ] ] not in suparati)\
                                        and parinte != lista[i][j-1]:
                                    l_succesori.append((Nod(lista[ i ][ j - 1 ], i, j - 1), 1))
                    if j % 2 == 1:
                        if lista[i][j-1] != 'liber' and ([lista[i][j-1],nume] not in suparati and
                                                         [nume, lista[i][j-1]] not in suparati) \
                                and parinte != lista[i][j-1]:
                            l_succesori.append((Nod(lista[i][j-1],i, j-1),1))
                        if i+1 < len(lista):
                            if lista[i+1][j] != 'liber' and ([lista[i+1][j],nume] not in suparati and
                                                             [nume, lista[i+1][j]] not in suparati) and \
                                    parinte != lista[i+1][j]:
                                l_succesori.append((Nod(lista[i+1][j],i + 1, j),1))
                        if i == len(lista) - 2 or i == len(lista) - 1:
                            if j + 1 <= 5:
                                if lista[ i ][ j + 1 ] != 'liber' and ([ lista[ i ][ j +1], nume ] not in suparati
                                                                       and [ nume, lista[ i ][j+1 ] ] not in suparati) \
                                        and parinte != lista[i][j+1]:
                                    l_succesori.append((Nod(lista[ i ][ j + 1], i , j+1), 1))

        return l_succesori


    #se modifica in functie de problema
    def test_scop(self):
        return self.nod_graf.info == self.problema.nod_scop.info


    def __str__ (self):
        parinte=self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"



""" Algoritmul A* """


def str_info_noduri(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = "["
    for x in l:
        sir += str(x) + "  "
    sir += "]"
    return sir


"""
functia afisare 
param: l - drumul de la nodul start la nodul scop
       filepath - numele fisierului in care vor fi scrise datele
aceasta functie afiseaza drumul in forma ceruta in enunt
pentru aceasta afisare m-am folosit de pozitiile nodurilor
am verificat care este pozitia nodului urmator fata de nodul curent pentru a afisa semnul corespunzator
"""
def afisare(l, filepath):
    file = open(filepath, "a+")
    sir = ""
    for i in range(len(l)):
        sir += l[i].nod_graf.info[0]
        if i + 1 < len(l):
            if l[i+1].nod_graf.info[1] == l[i].nod_graf.info[1] and l[i+1].nod_graf.info[2] == l[i].nod_graf.info[2] + 1:
                if (l[i].nod_graf.info[1] == len(lista) - 1 or l[i].nod_graf.info[1] == len(lista) - 2) and l[i].nod_graf.info[2] % 2 == 1 :
                    sir += " >> "
                else:
                    sir += " > "
            if l[i+1].nod_graf.info[1] == l[i].nod_graf.info[1] and l[i+1].nod_graf.info[2] == l[i].nod_graf.info[2] - 1:
                if (l[i].nod_graf.info[1] == len(lista) - 1 or l[i].nod_graf.info[1] == len(lista) - 2) and l[i].nod_graf.info[2] % 2 == 1:
                    sir += " << "
                else:
                    sir += " < "
            if l[i+1].nod_graf.info[1] == l[i].nod_graf.info[1] - 1 and l[i+1].nod_graf.info[2] == l[i].nod_graf.info[2]:
                sir += " ^ "
            if l[i+1].nod_graf.info[1] == l[i].nod_graf.info[1] + 1 and l[i+1].nod_graf.info[2] == l[i].nod_graf.info[2]:
                sir += " v "
            else:
                sir += " "
    file.write(sir)

"""
functia afisare_mesaj
param: filepath - numele fisierului in care va fi scris mesajul
aceasta functie este folosita pentru a scrie in fisier un mesaj, atunci cand lista open este goala
"""
def afisare_mesaj(filepath):
    file = open(filepath, "a+")
    file.write("Nu exista drum de la nodul de start la nodul scop.")

def afis_succesori_cost(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: "+str(x)+", cost arc:"+ str(cost)
    return sir


def in_lista(l, nod):
    """
        lista "l" contine obiecte de tip NodParcurgere
        "nod" este de tip Nod
    """
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None



def a_star(filepath):
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    open = [ rad_arbore ]  # open va contine elemente de tip NodParcurgere
    closed = [ ]  # closed va contine elemente de tip NodParcurgere
    # cat timp lista open nu este vida
    while len(open) > 0:
        print("Lista open: ", str_info_noduri(open))
        print("Lista closed: ", str_info_noduri(closed))
        nod_curent = open[0]
        #extragem nodul curent din lista open si il introducem in lista closed
        closed.append(nod_curent)
        #verific daca nodul extras este nod scop
        if nod_curent.test_scop():
            print(str_info_noduri(nod_curent.drum_arbore()))
            break
        open.pop(0)
        #expandam nodul extras
        lista_succ = nod_curent.expandeaza()
        # print("Succesorii nodului ", nod_curent, "sunt: ", afis_succesori_cost(lista_succ))
        for (nod, cost) in lista_succ:
            if not nod_curent.contine_in_drum(nod) :
                #verific daca se afla in closed
                x = in_lista(closed, nod)
                g_succesor = nod_curent.g + cost
                f = g_succesor + nod.h
                if x is not None:
                    if f < nod_curent.f:
                        # print("Nodul se afla deja in lista open.")
                        x.parinte = nod_curent
                        x.g = g_succesor
                        x.f = f
                        # print(x.nod_graf.info)
                else:
                    #verific daca se afla in open
                    x = in_lista(open, nod)
                    if x is not None:
                        if x.g > g_succesor:
                            # print("Nodul se afla deja in lista closed.")
                            x.parinte = nod_curent
                            x.g = g_succesor
                            x.f = f
                            # print(x.nod_graf.info)

                    else:
                        nod_cautare = NodParcurgere(nod_graf=nod, parinte=nod_curent,
                                                 g=g_succesor);  # se calculeaza f automat in constructor
                        open.append(nod_cautare)
            open.sort(key=lambda x: (x.f, -x.g))
            #sortam crescator dupa f

    # print("Lista open este: ", str_info_noduri(open))
    # print("\n------------------ Concluzie -----------------------")
    if (len(open) == 0):
        afisare_mesaj(filepath)
    else:
        afisare(nod_curent.drum_arbore(),filepath)


if __name__ == "__main__":
    for i in range(len(fisiere_input)):
        Copil = namedtuple("Copil", ("nume", "pozx", "pozy"))
        fisier_output = str("output_" + str(i+1) + ".txt")
        print(fisier_output)
        t_inainte = int(round(time.time() * 1000))
        lista, suparati, nod_start, nod_scop = citire(fisiere_input[i])
        problema = Problema()
        NodParcurgere.problema = problema
        a_star(fisier_output)
        t_dupa = int(round(time.time() * 1000))
        file = open(fisier_output, "a+")
        # file.write("\n")
        # file.write("Euristica 3\n")
        # file.write("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.\n")