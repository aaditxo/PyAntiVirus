import glob
import time
import sys, os

os_name = sys.platform
partition = []
directory = []
files = []

def partitions(sfsFolder):
    global partition
    big = 65

    if "win" in os_name:
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    #print("Successfully found partition: " + str(chr(big + i)))
                    partition.append(str(chr(big + i)) + ":\\")
            except:
                continue
        return indeces(sfsFolder)
    if "win" not in os_name:
        return indeces(sfsFolder)
    
def indeces(sfsFolder):
    global directory
    global files
    
    if "win" in os_name:
        directory2 = glob.glob("\\*")
    else:
        directory2 = glob.glob("//*")
    directory_tmp = []
    x = 1

    if "win" in os_name:
        for ind in range(len(partition)):
            #print(partition[ind])
            while directory2 != []:
                directory2 = glob.glob(partition[ind] + "\\*"*x)
                for i in range(len(directory2)):
                    directory.append(directory2[i])
                x += 1
            x = 1

        for i in range(len(directory)):
            if "." in directory[i]:
                files.append(directory[i])
        for i in range(len(directory)):
            if not os.path.isfile(directory[i]):
                directory_tmp.append(directory[i])
        directory = directory_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    if "win" not in os_name:
        while directory2 != []:
            directory = glob.glob("//*" * x)
            for i in range(len(directory2)):
                directory.append(directory2[i])
            x += 1
        x = 1

        for i in range(len(directory)):
            if "." in directory[i]:
                files.append(directory[i])
        for i in range(len(directory)):
            if not os.path.isfile(directory[i]):
                directory_tmp.append(directory[i])
        directory = directory_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)
