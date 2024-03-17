# represents group of byte number(0-255), similar to an array, immutable, bytes() constructor, 

a = [9, 14, 34, 25, 255]
b = bytes(a)
print(type(b))

print(b[0])