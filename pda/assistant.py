global file_name
global dictionnary
dictionnary = False

def ui_treatment(cmds):
    """
        pre: Prend une liste de commande
        post: Execute la fonction demandée dans la liste
    """
    if cmds[0] == "file":
        selectfile(cmds[1:])
    elif cmds[0] == "info":
        retrieve_info()
    elif cmds[0] == "dictionnary" and len(cmds) == 1:
        dictionnary()
    elif cmds[0] == "search" and len(cmds) == 2:
        search(cmds[1])
    elif cmds[0] == "search" and len(cmds)>2:
        print("You can't search more than one word at a time!")
    elif cmds[0] == "pika" and len(cmds) == 1:
        pikachu()
    elif cmds[0] == "sum" and len(cmds) >1:
        sumation(cmds)
    elif cmds[0] == "sum" and len (cmds) == 1:
        print("""Argument needed! Expected syntax: Numbers separated by spaces""")
    elif cmds[0] == "avg" and len(cmds) > 1:
        avg(cmds[1:])
    elif cmds[0] == "avg" and len(cmds) == 1:
        print("""Argument needed! Expected syntax: Numbers separated by spaces""")   
    elif cmds[0] == "help" and len(cmds) == 1:
        help()
    elif cmds[0] == "product" and len(cmds) == 1:
        print("""Argument needed! Expected syntax: Numbers separated by spaces""")
    elif cmds[0] == "product" and len(cmds) > 1:
        product(cmds[1:])
    elif cmds[0] == "morsecode" and len(cmds) >1:
        morsecode(cmds[1:])
    else:
        print("I don't know that command... Yet? Teach me machine learning so I can learn it!")

                                              
def dictionnary():
    """
    Sets the chosen file as a dictionnary, allowing word search
    """
    try:
        file = open(file_name,"r")
    except:
        print("That didn't work, are you sure you defined a valid filename? Try using 'file <your filename>'")
        return
    dictionnary = True


def selectfile (f_name):
    """
    Defines the file f_name as the file to use for commands "info", "dictionnary" and "search"
    """
    global file_name
    file_name = ""
    for i in f_name:
        file_name = file_name + i
    try:
        file = open(file_name,"r")
        dictionnary = False
        print("Now using {0} as base file".format(file_name))
        file.close()
    except:
        print("Are you kidding me? That file doesn't even exist, could you please try again?")
    return 

    
def retrieve_info():
    """
    Displays line and character information about the file
    """
    try:
        a = line_count()
        b = char_count()
    except:
        print("That didn't work, are you sure you defined a valid filename? Try using 'file <your filename>'")
        return
    print("There are {0} lines in your file, for a total of {1} characters".format(a,b))


def line_count(): #Counts lines
    file = open(file_name,"r")
    a = file.readlines()
    file.close()
    return len(a)


def char_count(): #Counts characters
    counter = 0
    file = open(file_name,"r")
    for line in file:
        for x in line.strip():
            counter +=1
    file.close()
    return counter

    
def pikachu(): #Does it really need an explanation?
    print("█▀▀▄░░░░░░░░░░░▄▀▀█")
    print("░█░░░▀▄░▄▄▄▄▄░▄▀░░░█")
    print('░░▀▄░░░▀░░░░░▀░░░▄▀')
    print('░░░░▌░▄▄░░░▄▄░▐▀▀')
    print('░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ ')#Pikachu
    print('░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█')
    print('▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█')
    print('█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀')
    print('░▀▄░░▀░░▀▀▀░░▀░░░▄█▀')
    print('░░░█░░░░░░░░░░░▄▀▄░▀▄')
    print('░░░█░░░░░░░░░▄▀█░░█░░█')
    print('░░░█░░░░░░░░░░░█▄█░░▄▀')
    print('░░░█░░░░░░░░░░░████▀')
    print('░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀')
    return

def sumation(cmds):
    """
    Sums all the specified numbers in the command
    """
    numbers = []
    sum = 0
    try:        
        for i in cmds[1:]:
            numbers.append(float(i))
        for l in numbers:
            sum = sum + l
        print(sum)
    except TypeError:
        print("Hmmm, I guess you haven't only entered valid numbers")
                    
    
def avg(nbs):    
    """
    Calculates the average of the specified numbers in the command
    """
    try:
        sum = 0
        for nb in nbs:
            sum += float(nb)            
    except TypeError:
        print("Hmmm, I guess you haven't only entered valid numbers")
        return
    print("And the average is.... : {0} ".format(sum/len(nbs)))

def product(nbs):
    """
    Calculates the product of the specified numbers in the command
    """
    try:
        prod = 0
        for nb in nbs:
            prod *= float(nb)
    except TypeError:
        print("Hmmm, I guess you haven't only entered valid numbers")
        return
    print("And the product is.... : {0} ".format(prod))


def help():
    """
    Diplays help about the program
    """
    print("""##########Help Page##########""")
    print(">>> file <filename.extension>:")
    print("Selects that file as the one to use for the following commands: dictionnary, info, search")
    print(">>> info:")
    print("Displays the number of lines and characters in the file specified by the 'file' function")
    print(">>> dictionnary:")
    print("Switches to dictionnary mode")
    print(">>> search <word>")
    print("If dictionnary mode is on and a file is selected, searches the closest word in that file.")
    print(">>>sum <number1 number2 number3 ...>:")
    print("Sums the given numbers")
    print(">>>avg <number1 number2 number3 ...>:")
    print("Averages the given numbers")
    print(">>>product <number1 number2 number3 ...>:")
    print("Multiplies the given numbers")
    print(">>>morsecode <Sentence>:")
    print("Translates the given sentence into morsecode. No accents!")
    print(">>>help:")
    print("Displays this very list")
    print(">>>exit, q, quit, exit():")
    print("Exits the assistant")
    print(">>>pika:")
    print("Just see for yourself")


def search(word):
    """
    Prints the closest word in the file
    """
    try:
        words = list_every_word(file_name)
        if len(words) > 20000:
            print("This might take a while.")
    except IOError:
        print("This file doesn't exist... Are you sure you defined a valid filename? Use 'file <your filename>'")
    except:
        print("An undefined error occured")
    if dictionnary == False:         
        print("You forgot to switch to dictionnary mode. Just use 'dictionnary'")
        return
    else:
        try:
            ld = smallest_ld(word,words)                                                
            print("The closest word found in the file is: {0}".format(ld[0][1]))
            return ld[0][1]
        except:
            print("An unexpected error occured, be sure to have valid input in your file")
        return 
    

def list_every_word(file_name): #considers file_name is valid
    """
    return a sorted list of all the words contained in a file
    """
    file = open(file_name,"r")
    words = []
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        for word in line:
            words.append(word)
    return words

def smallest_ld(word, l):
    ld = 100
    nearest = []
    for i in l:
        n_ld = iterative_levenshtein(word, i)
        if ld > n_ld:
            ld = n_ld
            nearest = [(ld, i)]
        elif ld == n_ld:
            nearest.append((ld,i))                                                
    return nearest


def iterative_levenshtein(s, t):
    """ 
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings 
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein 
        distance between the first i characters of s and the 
        first j characters of t
    """
    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
    #for r in range(rows):
        #print(dist[r])
    
 
    return dist[row][col]

def morsecode(stripped_sentence):
    morse_code = [("A",'.-'),("B",'-...'),("C",'-.-.'),("D",'-..'),("E",'.'),("F",'..-.'),("g",'--.'),("h",'....'),("i",'..'),("j",'.--.'),("k","-.-"),("l",'.-..')]
    morse_code += [("m",'--'),("n",'-.'),("o",'---'),("p",'.--.'),("q",'--.-'),("r",'.-.'),("s",'...'),("t",'-'),("u",'..-'),("v",'...-'),("w",'.--'),("x",'-..-'),("y",'-.--'),("z",'--..')]
    morse_code += [("0",'-----'),("1",'.----'),("2",'..---'),("3",'...--'),("4",'....-'),("5",'.....'),("6",'-....'),("7",'--...'),("8",'---..'),("9",'----.')]
    morse_code += [(".",'.-.-.-'),(",",'--..--'),("?",'..--..'),(":",'---...'),("/",'-..-.'),("-",'-....-'),("=",'-...-'),("""'""",'.----.'),("()",'-.--.-'),("_",'..--.-')]
    morse_code += [("!",'-.-.--'),("&",'.-...'),('''"''','.-..-.')]
    sentence = ""
    translation = ""
    for word in stripped_sentence:
        for letter in word:
            translated_letter = conversion(letter,morse_code)
            if translated_letter == None:
                return
            translation = translation + translated_letter + "/"
        translation = translation + "/"
    print(translation)
    return

def conversion(letter,alphabet):
    for i in range(len(alphabet)):
        if alphabet[i][0].upper() == letter.upper():
            return alphabet[i][1]
    print("That wasn't a valid sentence, please replace character {0}".format(letter))
    return None


while True:
    cmd = input("Enter a command, my master: ") #the name of the command 
    cmds = cmd.split(" ")
    if cmds[0] in ["q","quit","exit","exit()"]:
        print("cya")
        break
    else:
        ui_treatment(cmds)