import time
from copy import deepcopy

'''Am definit functii pentru fiecare mutare a pieselor'''

def dreapta_jos(matr, i, j, mutari, atac, simbol):
    if i + 1 < Joc.NR_LINII and j + 1 < Joc.NR_COLOANE and matr[ i + 1 ][ j + 1 ] == '#' and atac == 0:
        # aici vrem sa mutam cu o singura pozitie o piesa in dreapta jos daca e posibil(fara a ataca)
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        if i + 1 == Joc.NR_LINII - 1:
            # daca mutarea se face de pe penultima linie pe ultima linie, atunci piesa promoveaza
            mutare[ i + 1 ][ j + 1 ] = simbol.upper()
        else:
            mutare[ i + 1 ][ j + 1 ] = simbol
        mutari.append((mutare, i + 1, j + 1))

def stanga_jos(matr, i, j, mutari, atac, simbol):
    if i + 1 < Joc.NR_LINII and j > 0 and matr[ i + 1 ][ j - 1 ] == '#' and atac == 0:
        # aici vrem sa mutam cu o singura pozitie o piesa in stanga jos daca e posibil(fara a ataca)
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        if i + 1 == Joc.NR_LINII - 1:
            # daca mutarea se face de pe penultima linie pe ultima linie, atunci piesa promoveaza
            mutare[ i + 1 ][ j - 1 ] = simbol.upper()
        else:
            mutare[ i + 1 ][ j - 1 ] = simbol
        mutari.append((mutare, i + 1, j - 1))

def atac_stanga_jos(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i + 2 < Joc.NR_LINII and j >= 2 and (matr[ i + 1 ][ j - 1 ] == opus or matr[ i + 1 ][ j - 1 ] == opus.upper()) and \
            matr[ i + 2 ][ j - 2 ] == '#':
        # aici incercam sa atacam piesa din stanga jos daca este posibil
        if atac == 0:
            atac = 1
            mutari.clear()
        # setam atacul si stergem mutarile normale gesite anterior
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j - 1 ] = '#'
        if i + 2 == Joc.NR_LINII - 1:
            # daca atacul se face de pe antepenultima linie pe ultima linie, atunci piesa promoveaza
            mutare[ i + 2 ][ j - 2 ] = simbol.upper()
        else:
            mutare[ i + 2 ][ j - 2 ] = simbol
        mutari.append((mutare, i + 2, j - 2))
    return atac

def atac_dreapta_jos(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = simbol
    if i + 2 < Joc.NR_LINII and j + 2 < Joc.NR_COLOANE and (
            matr[ i + 1 ][ j + 1 ] == opus or matr[ i + 1 ][ j + 1 ] == opus.upper()) and matr[ i + 2 ][ j + 2 ] == '#':
        # aici incercam sa atacam piesa din dreapta jos daca este posibil
        if atac == 0:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 1
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j + 1 ] = '#'
        if i + 2 == Joc.NR_LINII - 1:
            # daca atacul se face de pe antepenultima linie pe ultima linie, atunci piesa promoveaza
            mutare[ i + 2 ][ j + 2 ] = simbol.upper()
        else:
            mutare[ i + 2 ][ j + 2 ] = simbol
        mutari.append((mutare, i + 2, j + 2))
    return atac


def dreapta_sus(matr, i, j, mutari, atac, simbol):
    if i > 0 and j + 1 < Joc.NR_COLOANE and matr[ i - 1 ][ j + 1 ] == '#' and atac == 0:
        # aici vrem sa mutam cu o singura pozitie o piesa in dreapta sus daca e posibil(fara a ataca)
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i - 1 ][ j + 1 ] = simbol
        mutari.append((mutare, i - 1, j + 1))

def stanga_sus(matr, i, j, mutari, atac, simbol):
    if i > 0 and j > 0 and matr[ i - 1 ][ j - 1 ] == '#' and atac == 0:
        # aici vrem sa mutam cu o singura pozitie o piesa in stanga sus daca e posibil(fara a ataca)
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i - 1 ][ j - 1 ] = simbol
        mutari.append((mutare, i - 1, j - 1))

def atac_stanga_sus(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 2 and j >= 2 and (matr[ i - 1 ][ j - 1 ] == opus or matr[ i - 1 ][ j - 1 ] == opus.upper()) \
            and matr[ i - 2 ][j - 2 ] == '#':
        # aici incercam sa atacam piesa din stanga sus daca este posibil
        if atac == 0:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 1
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i - 1 ][ j - 1 ] = '#'
        mutare[ i - 2 ][ j - 2 ] = simbol
        mutari.append((mutare, i - 2, j - 2))
    return atac

def atac_dreapta_sus(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 2 and j + 2 < Joc.NR_COLOANE and (matr[ i - 1 ][ j + 1 ] == opus or matr[ i - 1 ][ j + 1 ] == opus.upper()) \
            and matr[ i - 2 ][ j + 2 ] == '#':
        # aici incercam sa atacam piesa din dreapta sus daca este posibil
        if atac == 0:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 1
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i - 1 ][ j + 1 ] = '#'
        mutare[ i - 2 ][ j + 2 ] = simbol
        mutari.append((mutare, i - 2, j + 2))
    return atac

def atac_dublu_sus_dreapta_dreapta(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 4 and j + 4 < Joc.NR_COLOANE and (matr[ i - 1 ][ j + 1 ] == opus or matr[ i - 1 ][ j + 1 ] == opus.upper()) \
            and matr[ i - 2 ][ j + 2 ] == '#' and (matr[ i - 3 ][ j + 3 ] == opus or
                                                   matr[ i - 3 ][ j + 3 ] == opus.upper()) and \
            matr[ i - 4 ][ j + 4 ] == '#':
        # aici incercam capturam 2 piese ce se afla ambele pe diagonala din dreapta sus a piesei curente
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[i - 1][j + 1] = '#'
        mutare[i - 2][j + 2] = '#'
        mutare[i - 3][j + 3] = '#'
        mutare[i - 4][j + 4] = simbol
        if i - 4 == 0:
            mutare[i - 4][j - 4] = simbol.upper()
        mutari.append((mutare, i - 4, j + 4))
    return atac

def atac_dublu_sus_dreapta_stanga(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 4 and j + 2 < Joc.NR_COLOANE and (matr[ i - 1 ][ j + 1 ] == opus or matr[ i - 1 ][ j + 1 ] == opus.upper()) \
            and matr[ i - 2 ][ j + 2 ] == '#' and (matr[ i - 3 ][ j + 1 ] == opus or
                                                   matr[ i - 3 ][ j + 1 ] == opus.upper()) \
            and matr[ i - 4 ][ j ] == '#':
        # aici incercam capturam 2 piese ce se afla ambele pe diagonala din dreapta sus a piesei curente
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[i - 1][j + 1] = '#'
        mutare[i - 2][j + 2] = '#'
        mutare[i - 3][j + 1] = '#'
        mutare[i - 4][j] = simbol
        if i - 4 == 0:
            mutare[i - 4][j] = simbol.upper()
        mutari.append((mutare, i - 4, j))
    return atac

def atac_dublu_sus_stanga_stanga(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 4 and j >= 4 and (matr[ i - 1 ][ j - 1 ] == opus or matr[ i - 1 ][ j - 1 ] == opus.upper()) and \
            matr[ i - 2 ][ j - 2 ] == '#' and (matr[ i - 3 ][ j - 3 ] == opus or
                                               matr[ i - 3 ][ j - 3 ] == opus.upper())\
            and matr[ i - 4 ][ j - 4] == '#':
        # aici incercam capturam 2 piese ce se afla ambele pe diagonala din dreapta sus a piesei curente
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[i - 1][j - 1] = '#'
        mutare[i - 2][j - 2] = '#'
        mutare[i - 3][j - 3] = '#'
        mutare[i - 4][j - 4] = simbol
        if i - 4 == 0:
            mutare[i - 4][j - 4] = simbol.upper()
        mutari.append((mutare, i - 4, j- 4))
    return atac

def atac_dublu_sus_stanga_dreapta(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = 'a'
    if i >= 4 and j >= 2 and (matr[ i - 1 ][ j - 1 ] == opus or matr[ i - 1 ][ j - 1 ] == opus.upper()) and \
            matr[ i - 2 ][ j - 2 ] == '#' and (matr[ i - 3 ][ j - 1 ] == opus or
                                               matr[ i - 3 ][ j - 1 ] == opus.upper())\
            and matr[ i - 4 ][ j ] == '#':
        # aici incercam capturam 2 piese ce se afla ambele pe diagonala din dreapta sus a piesei curente
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[i - 1][j - 1] = '#'
        mutare[i - 2][j - 2] = '#'
        mutare[i - 3][j - 1] = '#'
        mutare[i - 4][j] = simbol
        if i - 4 == 0:
            mutare[i - 4][j] = simbol.upper()
        mutari.append((mutare, i - 4, j))
    return atac

def atac_dublu_jos_dreapta_dreapta(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = simbol
    if i + 4 < Joc.NR_LINII and j + 4 < Joc.NR_COLOANE and (matr[ i + 1 ][ j + 1 ] == opus or
                                                            matr[ i + 1 ][ j + 1 ] == opus.upper()) \
            and matr[ i + 2 ][ j + 2 ] == '#' and (matr[ i + 3 ][ j + 3 ] == opus or
                                                            matr[ i + 3 ][ j + 3 ] == opus.upper()) and\
            matr[i + 4][j + 4] == '#':
        # aici incercam sa atacam piesa din dreapta jos daca este posibil
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j + 1 ] = '#'
        mutare[i + 2][j + 2] = '#'
        mutare[i + 3][j + 3] = '#'
        mutare[i + 4][j + 4] = simbol
        if i + 4 == Joc.NR_LINII - 1:
            mutare[i + 4][j + 4] = simbol.upper()
        mutari.append((mutare, i + 4, j + 4))
    return atac

def atac_dublu_jos_stanga_stanga(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = simbol
    if i + 4 < Joc.NR_LINII and j >= 4 and (matr[ i + 1 ][ j - 1 ] == opus or
                                                            matr[ i + 1 ][ j - 1 ] == opus.upper()) \
            and matr[ i + 2 ][ j - 2 ] == '#' and (matr[ i + 3 ][ j - 3 ] == opus or
                                                            matr[ i + 3 ][ j - 3 ] == opus.upper()) and\
            matr[i + 4][j - 4] == '#':
        # aici incercam sa atacam piesa din dreapta jos daca este posibil
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j - 1 ] = '#'
        mutare[i + 2][j - 2] = '#'
        mutare[i + 3][j - 3] = '#'
        mutare[i + 4][j - 4] = simbol
        if i + 4 == Joc.NR_LINII - 1:
            mutare[i + 4][j - 4] = simbol.upper()
        mutari.append((mutare, i + 4, j - 4))
    return atac

def atac_dublu_jos_stanga_dreapta(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = simbol
    if i + 4 < Joc.NR_LINII and j >= 2 and (matr[ i + 1 ][ j - 1 ] == opus or
                                                            matr[ i + 1 ][ j - 1 ] == opus.upper()) \
            and matr[ i + 2 ][ j - 2 ] == '#' and (matr[ i + 3 ][ j - 1 ] == opus or
                                                            matr[ i + 3 ][ j - 1] == opus.upper()) and\
            matr[i + 4][j] == '#':
        # aici incercam sa atacam piesa din dreapta jos daca este posibil
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j - 1 ] = '#'
        mutare[i + 2][j - 2] = '#'
        mutare[i + 3][j - 1] = '#'
        mutare[i + 4][j] = simbol
        if i + 4 == Joc.NR_LINII - 1:
            mutare[i + 4][j] = simbol.upper()
        mutari.append((mutare, i + 4, j))
    return atac

def atac_dublu_jos_dreapta_stanga(matr, i, j, mutari, atac, simbol):
    if simbol.lower() == 'a':
        opus = 'n'
    else:
        opus = simbol
    if i + 4 < Joc.NR_LINII and j + 2 < Joc.NR_COLOANE and  (matr[ i + 1 ][ j + 1 ] == opus or
                                                            matr[ i + 1 ][ j - 1 ] == opus.upper()) \
            and matr[ i + 2 ][ j + 2 ] == '#' and (matr[ i + 3 ][ j + 1 ] == opus or
                                                            matr[ i + 3 ][ j + 1] == opus.upper()) and\
            matr[i + 4][j] == '#':
        # aici incercam sa atacam piesa din dreapta jos daca este posibil
        if atac == 0 or atac == 1:
            # daca mutarile gasite pana acum sunt doar normale setam atacul si stergem mutarile gasite
            atac = 2
            mutari.clear()
        mutare = deepcopy(matr)
        mutare[ i ][ j ] = '#'
        mutare[ i + 1 ][ j + 1 ] = '#'
        mutare[i + 2][j + 2] = '#'
        mutare[i + 3][j + 1] = '#'
        mutare[i + 4][j] = simbol
        if i + 4 == Joc.NR_LINII - 1:
            mutare[i + 4][j] = simbol.upper()
        mutari.append((mutare, i + 4, j))
    return atac


def mutare_piesa(matr, i, j):
    mutari = [ ]
    # mutarile posibile(ori de atac ori fara atac, nu amandoua)
    atac = 0
    # flag pentru mutari posibile de atac sau mutari posibile normale

    if matr[ i ][ j ] == 'a' or matr[ i ][ j ] == 'A' or matr[i][j] == 'N':
        # pentru a nu avea cod duplicat tratam impreuna miscarile in jos ale pieselor normale si promovate deja
        simbol = matr[ i ][ j ]
        dreapta_jos(matr, i, j, mutari, atac, simbol)
        stanga_jos(matr, i, j, mutari, atac, simbol)
        atac = atac_stanga_jos(matr, i, j, mutari, atac, simbol)
        atac = atac_dreapta_jos(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_jos_dreapta_dreapta(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_jos_dreapta_stanga(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_jos_stanga_dreapta(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_jos_stanga_stanga(matr, i, j, mutari, atac, simbol)

    if matr[ i ][ j ] == 'n' or matr[ i ][ j ] == 'N' or matr[i][j] == 'A':
        # pentru a nu avea cod duplicat tratam impreuna miscarile in jos ale pieselor normale si promovate deja
        simbol = matr[ i ][ j ]
        dreapta_sus(matr, i, j, mutari, atac, simbol)
        stanga_sus(matr, i, j, mutari, atac, simbol)
        atac = atac_stanga_sus(matr, i, j, mutari, atac, simbol)
        atac = atac_dreapta_sus(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_sus_dreapta_dreapta(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_sus_dreapta_stanga(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_sus_stanga_dreapta(matr, i, j, mutari, atac, simbol)
        atac = atac_dublu_sus_stanga_stanga(matr, i, j, mutari, atac, simbol)

    return mutari, atac



class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_LINII = 8
    NR_COLOANE = 8
    JMIN = None
    JMAX = None
    GOL = '#'
    default_table = [['#', 'a', '#', 'a', '#', 'a', '#', 'a'],
                     ['a', '#', 'a', '#', 'a', '#', 'a', '#'],
                     ['#', 'a', '#', 'a', '#', 'a', '#', 'a'],
                     ['#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#'],
                     ['n', '#', 'n', '#', 'n', '#', 'n', '#'],
                     ['#', 'n', '#', 'n', '#', 'n', '#', 'n'],
                     ['n', '#', 'n', '#', 'n', '#', 'n', '#']]

    def __init__(self, tabla=None):
        self.matr = tabla or self.default_table
        self.nr_a = 0
        self.nr_n = 0
        for row in self.matr:
            for p in row:
                if p == 'a' :
                    self.nr_a += 1
                elif p == 'A':
                    self.nr_a += 2
                elif p == 'n':
                    self.nr_n += 1
                elif p == 'N':
                    self.nr_n += 2

    def final(self):
        #daca nu mai avem mutari pentru unul dintre jucatori
        if len(self.mutari_joc(self.JMAX)) == 0:
            return self.JMIN
        elif len(self.mutari_joc(self.JMIN)) == 0:
            return self.JMAX
        else:
            return None

    def mutari_joc(self, jucator):
        """
        Pentru configuratia curenta de joc "self.matr" (de tip lista, cu 9 elemente),
        trebuie sa returnati o lista "l_mutari" cu elemente de tip Joc,
        corespunzatoare tuturor configuratiilor-succesor posibile.

        "jucator" este simbolul jucatorului care face mutarea
        """
        l_mutari = []
        atac = 0
        #cautam lista tuturor mutarilor posibile pentru un jucator (normale, atac sau atac dublu)
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLOANE):
                if self.matr[i][j] == jucator or self.matr[i][j] == jucator.upper():
                    mutari, atac_curent = mutare_piesa(self.matr, i, j)
                    # daca piesa curenta are mutari de atac, stergem mutarile normale de pana acum
                    if atac_curent == 1 and atac == 0:
                        l_mutari.clear()
                        atac = 1
                    #daca piesa curenta are mutari de atac dublu, stergem mutarile de atac sau normale de pana acum
                    if atac_curent == 2 and (atac == 1 or atac == 0):
                        l_mutari.clear()
                        atac = 2
                    #punem mutarile in lista de mutari
                    if atac_curent == 1 or atac_curent == 2 or atac == 0:
                        for mutare in mutari:
                            l_mutari.append(Joc(mutare[0]))
        return l_mutari

    def estimeaza_scor(self):
        #diferenta dintre numarul de piese
        if self.JMAX == 'a':
            return self.nr_a - self.nr_n
        return self.nr_n - self.nr_a





    def __str__(self):
        sir = ' '
        for index in range(8):
            sir += ' '
            sir += str(index)

        for index, line in enumerate(self.matr):
            sir += ' \n'
            sir += str(index)
            for piece in line:
                sir += ' '
                if piece == '#':
                    sir += ' '
                elif piece == 'a':
                    sir += '●'
                elif piece == 'n':
                    sir += '○'
                else:
                    sir += str(piece);
        sir += '\n '

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari_joc() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        # (scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        self.parinte = parinte
        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucator curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if final:
        if final == "remiza":
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-Beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare nivel de dificultate
    raspuns_valid = False
    while not raspuns_valid:
        print("Alege dificultatea")
        print("\t1 = Incepator")
        print("\t2 = Mediu")
        print("\t3 = Avansat")

        dificultate = int(input())

        if dificultate == 1:
            Stare.ADANCIME_MAX = 3
            raspuns_valid = True
        elif dificultate == 2:
            Stare.ADANCIME_MAX = 4
            raspuns_valid = True
        elif dificultate == 3:
            Stare.ADANCIME_MAX = 5
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu a sau cu n? ").lower()
        if Joc.JMIN in ['a', 'n']:
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie a sau n.")
    if Joc.JMIN == 'n':
        Joc.JMAX = 'a'
    else:
        Joc.JMAX = 'n'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'n', Stare.ADANCIME_MAX)

    while True:
        if stare_curenta.j_curent == Joc.JMIN:
            # muta jucatorul
            raspuns_valid = False
            #verificarea corectitudinii mutarilor utilizatorului
            while not raspuns_valid:
                try:
                    #verificam daca pozitia introdusa de jucator este una valida
                    linie = int(input("linie="))
                    coloana = int(input("coloana="))
                    if linie in range(0, Joc.NR_LINII) and coloana in range(0, Joc.NR_COLOANE):
                        #verific daca piesa de pe pozitia linie, coloana este pentru jucatorul curent
                        #verific daca pe pozitia respectiva avem culoarea corespunzatoare
                        stare = stare_curenta.tabla_joc.matr[linie][coloana]
                        if stare == Joc.JMIN or stare.upper() == Joc.JMIN:
                            linie_noua = int(input("linie noua="))
                            coloana_noua = int(input("coloana noua="))
                            # verific daca lina si coloana noua sunt valide
                            if linie_noua in range(0, Joc.NR_LINII) and coloana_noua in range(0, Joc.NR_COLOANE):
                                # iau toate mutarile si verific daca linia si coloana introduse corespund
                                # unei mutari valide
                                mutari, _ = mutare_piesa(stare_curenta.tabla_joc.matr, linie, coloana)
                                for mutare in mutari:
                                    if mutare[1] == linie_noua and mutare[2] == coloana_noua:
                                        raspuns_valid = mutare
                                        print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor())
                                        print("Scor jucator:", -stare_curenta.tabla_joc.estimeaza_scor())
                                if not raspuns_valid:
                                    print("Mutare imposibila.")
                            else:
                                print("Linie sau coloana invalida.")
                        else:
                            print("Nu este o piesa al jucatorului curent acolo.")
                    else:
                        print("Linie sau coloana invalida.")

                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi! Doriti sa iesiti (Y/N)?")
                    exit_func = input()
                    if exit_func == 'Y':
                        print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor())
                        print("Scor jucator:", -stare_curenta.tabla_joc.estimeaza_scor())
                        return

            # dupa iesirea din while sigur am valide atat linia cat si coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr = raspuns_valid[0]

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()






