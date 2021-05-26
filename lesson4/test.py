from threading import Thread, Condition, RLock
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import clean
import os
import shutil

type_folder = ("folder", "images", "video", "documents", "audio", "archives", "other")
dictFiles = {clean.cortFolder: [], clean.cortImage: [], clean.cortVideo: [], clean.cortText: [], clean.cortMusic: [], clean.cortArchive: [], clean.cortVarious: []}

def new_copyring(type_folder):
    global a_file, path_parent, path_destination
    if type_folder != "folder":
        if type_folder != "archives":
            os.chdir(f"{path_destination}/{type_folder}")
            #new_file_name = a_file.rsplit(".", 1)
            #shutil.copyfile(path_parent + "/" + a_file, normalize(new_file_name[0]) + "." + new_file_name[1])
            shutil.copyfile(path_parent + "/" + a_file, a_file)
        else:
            #new_file_name = a_file.rsplit(".", 1)
            #shutil.unpack_archive(path_parent + "/" + a_file, path_destination + f"/{type_folder}/" + normalize(new_file_name[0]))
            pass
            #shutil.unpack_archive(path_parent + "/" + a_file, path_destination + f"/{type_folder}/" + a_file)
        return f"The working of the thread with the data {type_folder}"
    else:
        # поток-заглушка, because dictFiles.keys() is unsubcritable
        return "folder"

def main():
    global a_file, path_parent, path_destination
    path_parent = "/media/teosoph/Data/Квартира"
    path_destination = f"{path_parent}"
    data = dict()
    a_file = "1.jpg"
    print("The running")
    data[type_folder] = [a_file, path_parent, path_destination]
    print(data)
    with ThreadPoolExecutor(max_workers=1) as executor:
        for res in executor.map(new_copyring, type_folder):
            print(res)

if __name__ == "__main__":
    main()
