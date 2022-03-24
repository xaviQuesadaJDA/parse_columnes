#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re

"""
parse_file.py llegeix el fitxer que li passem per línia de comandes
                com a paràmetre i selecciona una columna que també 
                li passem per línia de comandes.
                · La numeració de les columnes comença en 1.

                Exemple d'ús:
                python3 parse_file.py el_meu_fitxer.txt 2
"""
__author__   = "Xavi Quesada"
__email__    = "f.javier.quesada@iesjoandaustria.org"
__license__  = "GPL V3. https://www.gnu.org/licenses/gpl-3.0.en.html"


def get_camp(lin, col):
    """
    >>> get_camp("col1   col2   col3   col4", 1)
    'col1'

    >>> get_camp("col1   col2   col3   col4", 2)
    'col2'

    >>> get_camp("col1   col2   col3   col4", 3)
    'col3'

    >>> get_camp("col1   col2   col3   col4", 4)
    'col4'

    >>> get_camp("col1   col2   col3   col4", 9)
    '*_*_*<<<<<Error_en_temps_d_execucio>>>>>*_*_*'
    """
    resultat = ""
    exreg = ""
    for i in range(col):
        if (i==0):
            exreg = "^(\S+)"
        else:
            exreg += "\s+(\S+)"
    exreg +=  ".*$" 

    trobat = re.search(exreg, lin)
    try:
        resultat = trobat.group(col)
    except:
        resultat = "*_*_*<<<<<Error_en_temps_d_execucio>>>>>*_*_*"
    return resultat


def get_columna(fitxer, n):
    camps = []
    with open(fitxer) as file:
        for linia in file:
            camps.append(get_camp(linia, n))
    return camps
    

def main(fitxer_entrada, columna):
    columna = get_columna(fitxer_entrada, columna)
    for dada in columna:
        print (dada)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))