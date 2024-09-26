# time complexity is O(n)
l = list()
number = 36
for i in range(1, number+1):
    if number%i==0:
        l.append(i)
    else:
        continue

print(l)


# for time complexity O(root(n))
l = list()
number = 36
for i in range(1, int(number**0.5) +1):
    if number%i == 0:
        l.append(i)
        if i != number // i:
            l.append(number // i)

    else:
        continue

l.sort()
print(l)