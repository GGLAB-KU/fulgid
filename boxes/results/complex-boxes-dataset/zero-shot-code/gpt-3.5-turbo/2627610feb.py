box_0 = []
box_1 = ['table']
box_2 = ['lamp', 'tree', 'crown', 'blanket', 'soap']
box_3 = ['rain', 'mountain']
box_4 = ['storm']
box_5 = ['whistle', 'blender', 'tie', 'horn']
box_6 = ['headphone', 'truck', 'butterfly']
box_7 = ['toy']
box_8 = []

# Swap table and freezer
box_0.append(box_1.pop(0))
box_1.append('freezer')

# Put scarf into Box 1
box_1.append('scarf')

# Swap mountain and rain
box_3.append(box_6.pop(1))
box_6.append(box_3.pop(0))

# Remove toy from Box 7
box_7.pop(0)

# Remove storm from Box 4
box_4.pop(0)

# Empty Box 0
box_0.clear()

# Move mountain from Box 3 to Box 5
box_5.append(box_3.pop(0))

# Remove crown from Box 2
box_2.remove('crown')

# Replace horn, tie, and blender with toy, key, and shampoo in Box 5
box_5.remove('horn')
box_5.remove('tie')
box_5.remove('blender')
box_5.append('toy')
box_5.append('key')
box_5.append('shampoo')

# Swap truck in Box 6 with key in Box 5
box_6.append(box_5.pop(1))
box_5.append(box_6.pop(1))

# Remove soap from Box 2
box_2.remove('soap')

# Remove key and rain from Box 6
box_6.remove('key')
box_6.remove('rain')

# Replace lamp with chair in Box 2
box_2.remove('lamp')
box_2.append('chair')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)