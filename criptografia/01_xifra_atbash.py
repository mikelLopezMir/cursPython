# La xifra atbash és un tipus de xifratge que es basa en la substitució de lletres. La substitució es fa de la següent manera:
# La primera lletra de l'alfabet és substitueix per l'última, la segona per la penúltima, i així successivament.

def atbash_cypher(text):

    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_reves = 'zyxwvutsrqponmlkjihgfedcba'

    # generem una llista per a la sortida
    text_xifrat = []
    # iterate over the text
    for lletra in text:
        # si la lletra és a l'alfabet, la substituïm
        if lletra in alfabet:
            lletra_xifrada = alfabet_reves[alfabet.index(lletra)]
            text_xifrat.append(lletra_xifrada)
        # si no, la deixem tal com està
        else:
            text_xifrat.append(lletra)
    # s'ha generat una llista, la convertim en text
    return ''.join(text_xifrat)

# provem la funció
input_text = input("Introdueixi el text a xifrar\n")
print(f'El text xifrat és: {atbash_cypher(input_text)}')