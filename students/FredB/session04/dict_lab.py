#Dict_lab
#FredBallyns
#Session04

#Dictionaries 1
dict_data = {"name": "Fred","city": "Seattle","cake": "Carrot"}

print(dict_data)

dict_data.pop("cake")

print(dict_data)

dict_data["Fruit"] = "Mango"

print(dict_data)
print(dict_data.keys())
print(dict_data.values())

print("cake" in dict_data)

print("Fruit" in dict_data)

#Dictionaries 2
dict_count={}
for i in dict_data.keys():
    dict_count[i]=dict_data[i].lower().count("t")
print(dict_count)


#Sets
s2 = set(i for i in range(0, 21, 2))
s3 = set(i for i in range(0, 21, 3))
s4 = set(i for i in range(0, 21, 4))
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))


#Sets2
letter_set = set("Python")
print(letter_set)
letter_set.add("i")
print(letter_set)
frozenset = set("marathon")
print(letter_set.union(frozenset))
print(letter_set.intersection(frozenset))