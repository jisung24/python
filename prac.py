number = [1,2,3,4,5,6]
hash = {}
for i in number:
    if not i in hash:
        hash[i] = True

print(hash)