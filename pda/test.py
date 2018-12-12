file_name = "/usr/share/dict/words"
def test_selectfile():
    selectfile(file_name)
def test_dictionnary():
    dictionnary()
def test_search():
    if search("carnivol") == "carnival":
        print("Test 1 OK")
    if search("carnival") == "carnival":
        print("Test 2 OK")
    if search("dramatc") == "dramatic":
        print("Test 3 OK")
    if search("lllllengineeringlllll") == "engineering":
        print("Test 4 OK")
def test_sum():
    if sumation(["123","42","12.01"]) == 177.01:
        print("Test 5 OK")
def test_avg():
    if avg(["110","90","0"]) == 50.0:
        print("Test 6 OK")
def test_product():
    if avg(["100","10","9"]) == 9000.0:
        print("Test 7 OK")
def test_morsecode():
    if morsecode(["engine","start"]) == "./-./--./../-././/.../-/.-/.-./-//":
        print("Test 8 OK")