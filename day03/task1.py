import string

priorities = {letter:i for i, letter in enumerate(string.ascii_lowercase+string.ascii_uppercase,1)}
backpacks = open('input.txt','r').read().splitlines()
compartments = [[backpack[:len(backpack)//2],backpack[len(backpack)//2:]] for backpack in backpacks]
sum_of_priorities = 0
for backpack in compartments:
    common_element = [element for element in backpack[0] if element in backpack[1]][0]
    sum_of_priorities += priorities.get(common_element)

print(sum_of_priorities)