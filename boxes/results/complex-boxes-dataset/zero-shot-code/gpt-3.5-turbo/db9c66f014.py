box_0 = ['necklace', 'rocket', 'hat', 'magnet']
box_1 = ['book', 'desert', 'starfish', 'oven', 'coral']
box_2 = ['perfume', 'rock', 'button']
box_3 = ['puzzle', 'sun', 'shoe', 'skirt']
box_4 = ['moon', 'toaster', 'shark', 'shorts']

# Move items from Box 4 to Box 2
box_2.extend([box_4.pop(box_4.index('shorts')), box_4.pop(box_4.index('shark')), box_4.pop(box_4.index('toaster'))])

# Move items from Box 1 to Box 1
box_1.extend(['makeup', 'necklace', 'pants'])

# Move items from Box 1 to Box 1
box_1.extend(['chair', 'boot', 'razor'])

# Swap items between Box 1 and Box 3
box_1[box_1.index('makeup')], box_3[box_3.index('sun')] = box_3[box_3.index('sun')], box_1[box_1.index('makeup')]

# Replace items in Box 3 with items from Box 3
box_3[box_3.index('shoe')], box_3[box_3.index('makeup')] = box_1.pop(box_1.index('oven')), box_1.pop(box_1.index('swimsuit'))

# Remove items from Box 3
box_3.remove('swimsuit')
box_3.remove('puzzle')

# Move item from Box 4 to Box 3
box_3.append(box_4.pop(box_4.index('moon')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)