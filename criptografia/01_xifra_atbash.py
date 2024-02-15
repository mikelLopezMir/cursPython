# method to implement the atbash cypher

def atbash_cypher(text):
    # create a dictionary with the atbash cypher
    atbash_dict = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p',
        'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e',
        'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
    }
    # create a list to store the cyphered text
    cyphered_text = []
    # iterate over the text
    for letter in text:
        # if the letter is in the dictionary, add the cyphered letter to the list
        if letter in atbash_dict:
            cyphered_text.append(atbash_dict[letter])
        # if the letter is not in the dictionary, add the letter to the list
        else:
            cyphered_text.append(letter)
    # join the list into a string
    return ''.join(cyphered_text)