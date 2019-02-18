import os as os

def subfiles(dir):
    file_lst = []
    for fil in os.scandir(dir):
        if not fil.name.startswith('.') and fil.is_file():
            file_lst.append(fil.name)
        elif fil.is_dir():
            for fil2 in os.scandir(os.path.join(dir,fil)):
                if not fil2.name.startswith('.') and fil2.is_file():
                    file_lst.append(fil2.name)
        return file_lst

subfiles("/home/guillaume")
