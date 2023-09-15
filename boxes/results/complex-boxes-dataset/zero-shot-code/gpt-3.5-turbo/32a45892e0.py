box0 = ['zipper', 'ocean', 'rain', 'swimsuit']
box1 = ['snow', 'desert']
box2 = ['cup', 'cat']
box3 = []
box4 = ['usb', 'telescope']

# Swap usb in Box 4 with snow in Box 1
box1.append(box4.pop(box4.index('snow')))
box4.append(box1.pop(box1.index('usb')))

# Remove swimsuit and ocean from Box 0
box0.remove('swimsuit')
box0.remove('ocean')

# Swap telescope in Box 4 with cup in Box 2
box2.append(box4.pop(box4.index('cup')))
box4.append(box2.pop(box2.index('telescope')))

# Replace desert and usb with bag and button in Box 1
box1.append('bag')
box1.append('button')
box1.remove('desert')
box1.remove('usb')

# Remove bag and button from Box 1
box1.remove('bag')
box1.remove('button')

# Replace rain and zipper with dice and jungle in Box 0
box0.append('dice')
box0.append('jungle')
box0.remove('rain')
box0.remove('zipper')

# Put tree, pillow, and starfish into Box 2
box2.append('tree')
box2.append('pillow')
box2.append('starfish')

# Put mask and crown into Box 4
box4.append('mask')
box4.append('crown')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)