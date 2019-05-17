import os

'''
Paths and File Processing
'''
def listFiles():
    for line in os.listdir():
        print(os.path.abspath(line))

# listFiles()


def CopyFile(src, dest):
    with open(src, "rb") as source:
        with open(dest, "wb") as destination:
            while True:
                data = source.read(1)
                if data:
                    destination.write(data)
                else:
                    break


#CopyFile("from.pdf", "to.pdf")
#CopyFile("from.txt", "to.txt")


'''
File reading and parsing
'''
def GenLanguages():
    ExistingLanguages = {
        "python", "java", "perl", "fortran",
        "shell", "matlab", "bash", "c#",
        "javascript", "typescript", "c++", "c",
        "erlang", "ansible", "powershell", "r",
        "visualbasic", "php", "mysql", "rex",
        "db", "vb", "lisp", "sql",
        "someNewLanguage"}
    LanguagesFromStudents = set()
    with open("students.txt", "r") as f:
        for line in f:
            #print("line:" + line)
            values = line.strip().split(":")
            if not values[1]:
                # no potential language list
                continue
            else:
                potentialLanguages = values[1]
                for potentialLanguage in potentialLanguages.split(","):
                    potentialLanguage = potentialLanguage.strip()
                    #print("potentialLanguage:" + potentialLanguage)
                    if potentialLanguage in ExistingLanguages:
                        LanguagesFromStudents.add(potentialLanguage)

    return LanguagesFromStudents

#print(GenLanguages())

def FormatStudents():
    languages = GenLanguages()

    original = []
    with open("students.txt", "r") as f:
        #original = f.readlines()

        for line in f:
            #print("originalLine: " + line.strip())
            values = line.strip().split(":")
            #print(values)
            modifiedLine = values[0] + ": "
            if not values[1]:
                # nothing after colon, so append Nones
                modifiedLine += " None, None"
            else:
                allItems = values[1].strip().split(", ")
                # check if first item is nickname
                firstItem = allItems[0]
                if firstItem in languages:
                    # not a nick name, so add None
                    allItems.insert(0, "None")
                else:
                    if len(allItems) == 1:
                        allItems.append("None")
                modifiedLine += ", ".join(allItems)
            print(modifiedLine)

FormatStudents()











