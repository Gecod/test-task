dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

# way #1
new_dct = {}
for k, v in dct.items():
    if v >= 3:
        new_dct[k] = v

# way #2
new_dct = dict((k, v) for k, v in dct.items() if v >= 3)

print(new_dct)
