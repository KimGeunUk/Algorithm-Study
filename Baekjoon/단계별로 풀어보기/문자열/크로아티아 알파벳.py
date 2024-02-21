croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c_ in croatia:
    word = word.replace(c_, '!')
    
print(len(word))