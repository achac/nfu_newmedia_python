# -*- coding: utf-8 -*-

def search4prepositions_zhs(phrase: str) -> set:
    """返回一个距离在提供的俩个点之间"""
    # Source http://www.cnblogs.com/Tangf/archive/2011/08/28/2156431.html
    # Source 
    PREPOSITION_zhs = set('？')
    return PREPOSITION_zhs.intersection(set(phrase))

def search4letters(phrase: str, letters: str='？') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
