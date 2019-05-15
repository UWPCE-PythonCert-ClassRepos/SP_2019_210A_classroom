

def reading_parsing(file_name):
    """
    this organizes and get name nickname and languages  separated
    """
    student_lst  = []
    with open(file_name,"r") as infile:
        for line in infile.readlines():
            row = line.strip().split(":")
            dct_row = {"Name": row[0], "Nickname": "", "languages": ""}
            row_other_half = line.replace(' ', "").strip().split(":")[1].split(",")
            lang = []
            name = []
            for word in row_other_half:
                if word:
                    if word[0].islower():
                        lang.append(word.strip())
                    else:
                        name.append(word.strip())
                dct_row.update(Nickname = str(name).strip().replace("[","").replace("]", "").replace("'",""),
                                    languages = str(lang).strip().replace("[","").replace("]", "").replace("'",""))
                
            student_lst.append(dct_row)
    idx = 0
    for row in student_lst:
        print("{:<2}: {:<25}-   {:^15} -{:>30}".format(idx, row["Name"], row["Nickname"], row["languages"]))
        idx += 1


    
    generator = [item["languages"] for item in student_lst]
    specific_lang = []
    for lang in generator:
        # if lang not in specific_lang:
        line = lang.split(",")
        for x in line:
            if x:
                if x.strip() == "nothing":
                    continue
                if x.strip() not in specific_lang:
                    specific_lang.append(x.strip())
                    specific_lang.sort()

    print("\nSpecific Language list: \n")
    for index, language in enumerate(specific_lang):
            print(str((index + 1)) +".", language)
    
    
          



def main():
    infile = "students.txt"
    reading_parsing(infile)

if __name__ == "__main__": main()
    