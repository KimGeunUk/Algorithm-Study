text = ['#', '+', '+', '+', '+']

print(''.join(text))
for i in range(1, 5):
    print(''.join(text[-i:] + text[:5-i]))