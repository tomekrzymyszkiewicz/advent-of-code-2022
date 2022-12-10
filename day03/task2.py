import string

priorities = {letter:i for i, letter in enumerate(string.ascii_lowercase+string.ascii_uppercase,1)}
backpacks = open('input.txt','r').read().splitlines()
groups_backpacks = [backpacks[group_start_index:group_start_index+3] for group_start_index in range(0,len(backpacks),3) ]
sum_of_priorities = 0
for group_backpacks in groups_backpacks:
    common_element = [element for element in group_backpacks[0] if element in group_backpacks[1] and element in group_backpacks[2]][0]
    sum_of_priorities += priorities.get(common_element)

print(sum_of_priorities)