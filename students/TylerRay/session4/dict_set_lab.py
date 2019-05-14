# Tyler Ray Dictionary and Set Lab
# Session4
# 5/5/2019


# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
# (so the keys should be: “name”, etc, and values: “Chris”, etc.)
# Display the dictionary.
# Delete the entry for “cake”.
# Display the dictionary.
# Add an entry for “fruit” with “Mango” and display the dictionary.
#     Display the dictionary keys.
#     Display the dictionary values.
#     Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
#     Display whether or not “Mango” is a value in the dictionary (i.e. True).



def step_one():
    labDict = {"Name": "Chris", "City": "Seattle", "Cake": "Chocolate"}
    stringStatement = "Step One: {} is from {} and enjoys {}.".format(labDict["Name"], labDict["City"], labDict["Cake"])
    del labDict["Cake"]
    labDict["Fruit"] = "Mangos"
    print(stringStatement)
    stringStatement ="Step Two: {} is from {} and enjoys {}.".format(labDict["Name"], labDict["City"], labDict["Fruit"])
    print(stringStatement)

    labkeys = labDict.keys()
    labvalues = labDict.values()
    print("The current dictionary keys are: ", labkeys,"\n The current dictionary values are: ", labvalues)

    cakeinvalues = "Mangoes are in the dictionary values: ","Mangos" in labvalues
    mangosinkeys = "Mangoes are in the dictionary values: ","Cake" in labkeys

    print(mangosinkeys, "\n",cakeinvalues)


    return None

if __name__ == '__main__':
    print(step_one())
