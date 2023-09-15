box_0 = ['wire', 'console', 'pillow', 'book']
box_1 = []
box_2 = ['controller', 'blender', 'cup', 'storm', 'gloves']
box_3 = ['spoon', 'necklace']
box_4 = ['camera', 'mixer']
box_5 = ['flower', 'blanket', 'butterfly', 'pot', 'crown']
box_6 = []
box_7 = ['shampoo', 'jungle', 'scissors', 'shelf', 'skirt']

# Remove flower, pot, and crown from Box 5
box_5.remove('flower')
box_5.remove('pot')
box_5.remove('crown')

# Move shelf and skirt from Box 7 to Box 2
box_2.append(box_7.pop(box_7.index('shelf')))
box_2.append(box_7.pop(box_7.index('skirt')))

# Swap pillow in Box 0 with necklace in Box 3
box_0[box_0.index('pillow')], box_3[box_3.index('necklace')] = box_3[box_3.index('necklace')], box_0[box_0.index('pillow')]

# Move camera from Box 4 to Box 5
box_5.append(box_4.pop(box_4.index('camera')))

# Replace mixer with island in Box 4
box_4[box_4.index('mixer')] = 'island'

# Move scissors, jungle, and shampoo from Box 7 to Box 5
box_5.append(box_7.pop(box_7.index('scissors')))
box_5.append(box_7.pop(box_7.index('jungle')))
box_5.append(box_7.pop(box_7.index('shampoo')))

# Move book from Box 0 to Box 2
box_2.append(box_0.pop(box_0.index('book')))

# Swap island in Box 4 with necklace in Box 0
box_4[box_4.index('island')], box_0[box_0.index('necklace')] = box_0[box_0.index('necklace')], box_4[box_4.index('island')]

# Empty Box 3
box_3.clear()

# Move necklace from Box 4 to Box 3
box_3.append(box_4.pop(box_4.index('necklace')))

# Replace necklace with violin in Box 3
box_3[box_3.index('necklace')] = 'violin'

# Move controller and blender from Box 2 to Box 1
box_1.append(box_2.pop(box_2.index('controller')))
box_1.append(box_2.pop(box_2.index('blender')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)