x=0
y=0
z=1
left = not (x or y or z)
right = not x and not y and not z
statment = left == right
print (statment)

x=0
y=1
z=1
left = not (x or y or z)
right = not x and not y and not z
statment = left == right
print (statment)