# parse_columnes
És un programa naïf, que permet seleccionar una columna d'un fitxer de text i treure-la per la sortida estàndar.

Requereix python3 i el mòdul re per executar-lo.

S'ofereixen dues versións:
* La primera: parse_file.py fa ús de les capacitats de python de llegir fitxers de text.
* La segona: parse_file_no_file.py, en lloc d'obrir un fitxer, utilitza la entrada estàndar per obtenir les diferents línies de text.

## Exemples d'ús:
* $ python3 parse_file.py dades.txt 2
* $ python3 parse_file_no_file.py 2 < dades.txt

