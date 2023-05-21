#!/usr/bin/env python3

def return_evens(num_list):
    return [j for j in num_list if j % 2 == 0]
return_evens([0, 1, 3, 5, 7, 8, 9])
def make_exclamation(sentence_list):
    return [j + '!' for j in sentence_list]