"""
pattest.py: Allows the checking of various patterns and target strings
"""
import re
while True:
    pat = input("Pattern: ")
    if not pat:
        break
    while True:
        s = input("Target: ")
        if not s:
            break
        mm = re.match(pat,s)
        if mm:
            print("Match : matched {0!r}, start = {1}, end = {2}".format(s[mm.start():mm.end()], mm.start(), mm.end()))
            print("Match : groups:", mm.groups())
            print("Match : gdict :", mm.groupdict())
        else:
            print("Match : no match")
        ms = re.search(pat, s)
        if ms:
            print('Search: matched {0!r}, start = {1}, end = {2}'.format(s[ms.start():ms.end()], ms.start(), ms.end()))
            print('Search: groups:', ms.groups())
            print('Search: gdict:', ms.groupdict())
        else:
            print('Search: no match')
            
