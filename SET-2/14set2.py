# 14. Create a set insert some values and convert it to frozenset. Try to add and remove some elements.

s = {1,2,3,4,5}

fs = frozenset(s)

print(fs)

fs.add(6)
# Once a frozenset is created, you cannot change its values.
fs.remove(3)

print(fs)