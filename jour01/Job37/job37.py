# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:38:46 2021

@author: Arnaud
"""

from itertools import permutations 

def next_anagram(mot):
    #on génére tous les anagrammes du mot
    anagrams = list(permutations(mot))
    result = "z"
    #On garde les anagrammes qui sont plus "grand" que le mot et plus proche
    # que l'anagramme précédemment trouvé
    for anagram in anagrams: 
        if "".join(anagram) > mot and "".join(anagram) < result:
            result = "".join(anagram)
    return result

print(next_anagram("acedb"))