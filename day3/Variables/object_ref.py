# when we create multiple variable with same value then its memory address  is same since python has created one object initially so only referencing is done

a = 4
b = 4
c = 4
d = 4.0

print(id(a))
print(id(b))
print(id(c))
print(id(d))
