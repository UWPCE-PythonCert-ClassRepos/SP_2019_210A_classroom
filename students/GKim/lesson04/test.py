def read_file(file_name):
    with open(file_name, "r") as obj_file:
        student_lang_lst = []
        list_of_student_names = []
        list_of_nicknames = []
        for line in obj_file:
            student_name = line.strip().split(":")[0]
            student_nick_name = ''
            student_language = []
            second_half = line.replace(' ', "").strip().split(":")[1].split(",")
            for part in second_half:
                if part:
                    if not part[0].islower():
                        student_nick_name = part
                    else:
                        student_language.append(part)
            student_lang_lst.append(student_language)
        unique_data = [list(uni) for uni in set(tuple(uni) for uni in student_lang_lst)]
        res = ()
        for item in unique_data:
            res = list(set(res) | set(item))
        print("Here is a list of distinct programming languages used: \n")
        for index, language in enumerate(res):
            print(str((index + 1)) +".", language)

read_file("students.txt")