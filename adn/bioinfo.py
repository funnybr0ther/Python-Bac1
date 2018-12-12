def is_adn(s):
    """pre: s, la séquence qu'on veut analyser. Doit être un string.
    post: retourne True si la séquence ne contient que des AGCT ou False dans le cas contraire."""
    s = s.upper()
    if s == "":
        return False
    for i in s:
        if i not in ["A","G","C","T"]:
            return False
    return True


def positions(s,p):
    """pre: s, la grande séquence, p, la petite séquence. Doivent être des strings.
    post: retourne les emplacements où p se retrouve dans s sous la forme d'une liste pos."""
    pos = []
    for i in range(0,len(s)-len(p)+1):
        if s[i:i+len(p)] == p:
            pos.append(i)
    return pos


def distance_h(a,b):
    """pre: a et b, deux strings de longueurs identiques.
    post: counter_h, le nombre d'emplacements aux entrées différents  dans les deux strings."""
    counter_h = 0
    for i in range (0,len(a)):
        if a[i] != b[i]:
            counter_h += 1
    return counter_h


def plus_long_palindrome(text):
    """pre: text, un string
    post: Retourne la séquence palindromique la plus longue issue du string text. Si aucun palindrome n'est
    trouvé, la séquence retourne None. Une lettre unique n'est pas un palindrome."""
    if len(text) == 2 and text[1] == text [0]: #2 lettres=cas particulier de la fonction, où elle donnait de fausses réponses
        return text
    a = 0
    b = 0
    c = 1
    long1 = 1
    long2 = 1
    if len(text)<=1: #zéro ou deux lettres = pas un palindrome.
        return None
    for i in range (1,len(text)): #Pour chaque lettre dans la séquence sauf la première ou la dernière, essaye de trouver un palindrome impair (aba) autour.
        c = 1
        while True:
            if i-c < 0 or i+c >= len(text):
                break
            elif text[i-c] == text[i+c]:
                c += 1
            elif text[i-c] != text [i+c]:
                break
        if long1 < c:
            a = i
            long1 = c
    for i in range(1,len(text)): #Pour chaque lettre dans la séquence sauf la première ou la dernière, essaye de trouver un palindrome pair (abba) autour.
        c = 0
        while True:
            if i-c < 0 or i+1+c >= len(text):
                break
            elif text[i-c] == text[i+c+1]:
                c += 1
            elif text[i-c] != text[i+c+1]:
                break
        if long2 < c:
            b = i
            long2 = c
    if long1 == 1 and long2 == 1: #si aucun palindrome n'a été trouvé
        return None
    if long1<long2+1: #Si le palindrome pair est plus long, on retourne celui-là
        return text[b-long2+1:b+long2+1]
    else: #Sinon, on retourne le palindrome impair.
        return text[a-long1+1:a+long1]


def test_is_adn():
    """pre:is_adn
    post: série de 3 tests. S'ils fonctionnent, la fonction printera Test 1-2-3 Ok."""
    if is_adn("agctgacgtagctagctcgat") == True:
        print("Test 1 Ok")
    if is_adn("agctagctagctcgatcgcdatc") == False:
        print("Test 2 Ok")
    if is_adn("") == False:
        print("Test 3 Ok")


def test_positions():
    """pre:positions()
    post: série de 3 tests. S'ils fonctionnent, la fonction printera Test 1-2-3 Ok."""
    if positions("actgtacggcatg","ac") == [0,5]:
        print("Test 1 Ok")
    if positions("","") == [0]:
        print("Test 2 Ok")
    if positions("agctcgtagcgctagcgcgcatagctcgctagctagc","agc") == [0,7,13,22,30,34]:
        print('Test 3 Ok')


def test_distance():
    """pre:test_distance
    post: série de 3 tests. S'ils fonctionnent, la fonction printera Test 1-2-3 Ok."""
    if distance_h("acgtcgacgctagcgcgcgatcgcgactg","acgtcgacactagcgcgcaatcgcaacta") == 4:
        print("Test 1 ok") 
    if distance_h("","") == 0:
        print("Test 2 ok")
    if distance_h("actgcacgt","gtcagtatg") == 9:
        print("Test 3 ok")


def test_plus_long_palindrome():
    """pre:plus_long_palindrome
    post: série de 3 tests. S'ils fonctionnent, la fonction printera Test 1-2-3 Ok."""
    if plus_long_palindrome("aaaagctcgattttt") == "agctcga":
        print("Test 1 Ok")
    if plus_long_palindrome("agctcgcatagacgctggaaggtcgcacgctcgatata") == "acgctggaaggtcgca":
        print("Test 2 Ok")
    if plus_long_palindrome("atgcatgcatgcatgcatgcatgca") == None:
        print("Test 3 Ok")


def tests():
    """ pre: Nécéssite les fonctions test_distance, test_positions, test_is_adn et test_plus_long_palindrome.
    post: réalise la série de 4*3 tests vérifiant que les 4 fonctions fonctionnent comme elles devraient."""

    test_distance()
    test_positions()
    test_is_adn()
    test_plus_long_palindrome()

print(plus_long_palindrome("abac"))
