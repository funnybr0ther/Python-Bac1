file = open("testfile.txt","w")
file.write("Remix_Dubstep_Ave_Maria Roland_Keunings 45 50\n")
file.write("Two_Girls_One_Cup_Music David_Guetta 29 9\n")
file.write("Screaming_Goat Chèvre 4 5\n")
file.write("Tournevis_ASMR JMJ 15 30\n")
file.write("Bruit_Tracteur Michel_Vergautier 6 30\n")
file.write("S&M_Sounds Django 45 20\n")
file.close()

class Duree:
    def __init__(self, h=0,m=0,s=0):
        if type(m) is not int or type(h) is not int or type(s) is not int:
            print("Those are not valid numbers")
            return 

        if m not in range(0,60):
            print("Those are not valid numbers")
            return 
        else:
            self.hours = h
            self.minutes = m
            self.seconds = s


    def toSecondes(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def delta(self,d):
        return -self.toSecondes() + d.toSecondes()

    
    def apres(self,d):
        if delta(self,d) > 0:
            return True
        else:
            return False


    def ajouter(self,d):
        return Duree((((self.seconds+d.seconds)//60) + self.minutes + d.minutes)//60 + self.hours + d.hours, (((self.seconds+d.seconds)//60) + self.minutes + d.minutes)%60, ( self.seconds + d.seconds ) % 60)
    

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds)


class Chanson:
    def __init__(self, t, a, d):
        """
        t: the song title
        a: the author 
        d: the lenght of the song                        
        """
        self.title = t
        self.author = a
        self.duration = d


    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{0} - {1} - {2}".format(self.title, self.author, self.duration)

    def get_duration(self):
        return self.duration                


class Album:
    def __init__(self,name = None):
        """
        Initialize an album as a list
        """
        self.album = []
        self.album_name = name
        self.song_count = 0
        self.duration = Duree(0,0,0)

    def add(self, chanson):
        dur_temp = self.duration.ajouter(chanson.get_duration()).toSecondes()
        if isinstance(chanson, Chanson) == False:
            return False
        if len(self.album) >= 100:
            return False
        if dur_temp  >= 75*60  :
            return False

        self.duration = self.duration.ajouter(chanson.get_duration())
        self.album.append(chanson)
        return True

    def __str__(self):
        album_str = "Album {0} ({1} chansons, {2})\n".format(self.album_name, len(self.album), self.duration)
        for i, song in enumerate(self.album):
            album_str += "{0:02}: {1}\n".format(i, song)                                    
        return album_str



def db_to_list(filename):
    """
    Return a list of tuples containing the info of all the song in the db file
    """
    f = open(filename, "r")
    return [tuple(line.split()) for line in f]


 

song_lst = []

for song in db_to_list("testfile.txt"):
    song_lst.append(Chanson(song[0], song[1], Duree(0 ,int(song[2]), int(song[3]) ) ))

album = Album(1)
count = 1

for song in song_lst:
    r = album.add(song)
    if r == False:
        print(album)
        count += 1
        album = Album(count)
        #album.add(song)
