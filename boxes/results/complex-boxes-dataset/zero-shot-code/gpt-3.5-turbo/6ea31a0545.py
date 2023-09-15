box_0 = ['boat', 'laptop', 'bag', 'key']
box_1 = ['comb']
box_2 = ['cow', 'toy', 'rock', 'comet', 'bell']
box_3 = ['mountain', 'controller', 'console', 'tie', 'glasses']
box_4 = ['seaweed', 'flute', 'telescope', 'magnet']
box_5 = ['towel', 'dress', 'note']
box_6 = ['scarf', 'sandals', 'belt']
box_7 = ['crown', 'guitar', 'bowl', 'dolphin']
box_8 = ['chair']
box_9 = []
box_10 = ['table']
box_11 = []
box_12 = ['book', 'shoe', 'skirt']

# Remove items from Box 4
box_4.remove('telescope')
box_4.remove('magnet')
box_4.remove('flute')

# Add items to Box 1
box_1.append('cow')
box_1.append('paint')

# Add items to Box 2
box_2.append('mixer')
box_2.append('swimsuit')

# Swap items between Box 8 and Box 3
box_8, box_3 = box_3, box_8

# Replace items in Box 3
box_3.remove('mountain')
box_3.remove('tie')
box_3.append('note')
box_3.append('shelf')

# Remove items from Box 6
box_6.remove('belt')
box_6.remove('sandals')

# Replace items in Box 10
box_10.remove('table')
box_10.append('shoes')

# Add item to Box 12
box_12.append('makeup')

# Move items from Box 5 to Box 0
box_0.extend(box_5)
box_5.clear()

# Add item to Box 11
box_11.append('cloud')

# Swap items between Box 11 and Box 0
box_11, box_0 = box_0, box_11

# Add item to Box 10
box_10.append('bowl')

# Move item from Box 4 to Box 2
box_2.append(box_4.pop(0))

# Swap items between Box 10 and Box 7
box_10, box_7 = box_7, box_10

# Add item to Box 8
box_8.append('ship')

# Move items from Box 2 to Box 0
box_0.extend(box_2)
box_2.clear()

# Replace item in Box 1
box_1.remove('comb')
box_1.append('star')

# Add items to Box 6
box_6.append('controller')
box_6.append('bus')
box_6.append('card')

# Move items from Box 1 to Box 11
box_11.extend(box_1)
box_1.clear()

# Add items to Box 6
box_6.append('ocean')
box_6.append('scissors')
box_6.append('swimsuit')

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
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)