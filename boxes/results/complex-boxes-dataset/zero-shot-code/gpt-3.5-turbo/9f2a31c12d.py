box_0 = ['doll']
box_1 = ['tree', 'sun', 'flute', 'moon']
box_2 = ['keyboard', 'blender', 'zipper']
box_3 = ['toy', 'bear']
box_4 = ['laptop', 'fish', 'horse', 'shoe', 'boat']
box_5 = ['bag', 'dolphin', 'spoon', 'pan']
box_6 = ['blanket']
box_7 = ['speaker', 'basket', 'jungle', 'scarf']
box_8 = ['phone', 'mask']

# Remove items from Box 2
box_2.remove('keyboard')
box_2.remove('blender')
box_2.remove('zipper')

# Remove items from Box 5
box_5.remove('bag')
box_5.remove('spoon')
box_5.remove('dolphin')
box_5.remove('pan')

# Replace items in Box 4
box_4.clear()
box_4.extend(['bicycle', 'grinder', 'polish'])

# Replace item in Box 8
box_8.remove('mask')
box_8.append('chair')

# Swap items between Box 7 and Box 8
box_7.remove('basket')
box_7.append('chair')

# Put new items into Box 1
box_1.extend(['rock', 'comet', 'butterfly'])

# Empty Box 4
box_4.clear()

# Replace item in Box 1
box_1.remove('moon')
box_1.append('mirror')

# Empty Box 6
box_6.clear()

# Replace item in Box 1
box_1.remove('tree')
box_1.append('wig')

# Put new items into Box 3
box_3.extend(['jungle', 'microwave'])

# Replace items in Box 1
box_1.remove('butterfly')
box_1.remove('mirror')
box_1.extend(['comb', 'toothbrush'])

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