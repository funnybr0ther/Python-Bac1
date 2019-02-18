import os
class ImageFolder:

    def __init__(self, path):
        self.files_in_dir = {}
        self.__path = path
        for dire in os.scandir(path):
            try:
                for fil in os.scandir(os.path.join(path,dire)):
                    try:
                        self.files_in_dir[dire.name].append(fil.name)
                    except:
                        self.files_in_dir[dire.name] = [fil.name]
            except:
                pass
        for x in self.files_in_dir: #Y'a surement moyen de faire mieux, mais ça a le mérite de marcher...
            self.files_in_dir[x] = sorted(self.files_in_dir[x])
        self.keys = [i for i in self.files_in_dir]
        self.counter_turns = Counters(len(self.keys))
        
    def __str__(self):
        return str(self.files_in_dir)

    def next(self, image):
        a = 0
        for i in range(len(self.keys)):
            if self.keys[i] == image:
                a = i
                break
        try:
            picked_image = self.counter_turns.next(a+1)
            return self.files_in_dir[self.keys[a]][picked_image]
        except:
            picked_image = self.counter_turns.reset(a+1)
            return self.files_in_dir[self.keys[a]][picked_image]

class Counters:
    def __init__(self, number):
        self.list_of_counters = [-1 for i in range(number)]
    def next(self, number):
        try:
            self.list_of_counters[number-1] += 1
            return self.list_of_counters[number-1]
        except:
            raise
    def reset(self, number):
        self.list_of_counters[number-1] = 0
        return self.list_of_counters[number-1]


def read_ascii(name):
    list_of_lines = []
    file = open(name,"r")
    for line in file:
        list_of_lines.append(line.strip())
    for i in range(len(list_of_lines)-1):
        if len(list_of_lines[i]) != len(list_of_lines[i+1]):
            file.close()
            raise ValueError("Lines don't have the same length")
    return list_of_lines

width = input("Width?")
height = input("Height?")
name = input("Filename?")
path = input("Images Path?")
nom = input("Name of your wonderful creation?")



