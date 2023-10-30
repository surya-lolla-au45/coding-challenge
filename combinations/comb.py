from itertools import permutations
def find_combinations(characters):
    if len(characters) != len(set(characters)):
        return "Error: Duplicates not allowed"
    else:
        perms = [''.join(p) for p in permutations(characters)]
        return ', '.join(perms)

input_characters = input("Enter characters separated by commas: ").split(',')
result = find_combinations(input_characters)
print(result)
