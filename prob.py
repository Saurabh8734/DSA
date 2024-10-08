s = "ASdfesD@#HBDHB&^GUV%*H45fdvnhw74w5e54uuU"
uppercases = ''
lowercases = ''
special_chars = ''
numbers = ''

for i in s:
    if i.isupper():
        uppercases += i
    elif i.islower():
        lowercases += i
    elif i.isnumeric():
        numbers += i
    else:
        special_chars += i

# Concatenate the parts in the required order
result = uppercases + lowercases + special_chars + numbers
print(result)