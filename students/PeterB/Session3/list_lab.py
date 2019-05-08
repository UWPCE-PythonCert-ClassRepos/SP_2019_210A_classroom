#series 1

Fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruits')

New_Fruit = input('Banana')
Fruits.append(New_Fruit)
print(Fruits)

Number = input('Pick a number')
print(f'the {Fruits} in the list is [int(Fruits)-1]')

Fruits = ['Bananas']+Fruits
print(Fruits)

print('Adding another fruit to the beginning of the list')
Fruits.insert(0, 'Strawberry')
print(Fruits)

for value in Fruits:
    if 'P' in value[0]:
        print(value)


#series 2

print(Fruits)
del Fruits(0)
response = input(" name a fruit to delete ")
if response in Fruits:
    Fruit.remove(response3)
    print response, "has been deleted"
else:
    print response, "cannot be deleted because it is not found in list"


#series 3
print(Fruits)

Fruits.lower()
for items in Fruits:
    Fruits.lowerappend(Fruits.lower())

for item in Fruits:
    answer = ''
    while answer ='no' and answer ='yes':
        answer = input('Do you like '+item+'? yes/no:')
        if answer =='no':
            Fruits.remove(item)
print(Fruits_3)


# series 4

print(Fruits)
def reverse(Fruits):
  str = ""
  for i in Fruits:
    str = i + str
  return str
s = Fruits
print(s.translate({ord('Strawberry'): None}))
print(Fruits)
