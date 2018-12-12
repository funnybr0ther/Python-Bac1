

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
    post: réalise la série de 4*3 tests vérifiant que les 4 fonctions fonctionnent comme elles devraient.
    """

    test_distance()
    test_positions()
    test_is_adn()
    test_plus_long_palindrome()


tests()