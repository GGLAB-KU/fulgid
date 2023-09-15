box_0 = ['guitar']
box_1 = ['boot', 'zipper', 'perfume', 'pen', 'helmet']
box_2 = ['flute', 'comb', 'pillow', 'dog']
box_3 = ['swimsuit', 'needle', 'cow', 'bag']
box_4 = ['jungle', 'violin', 'sculpture']
box_5 = ['wire']
box_6 = ['mixer', 'frame', 'motorcycle', 'mirror']
box_7 = ['basket', 'storm', 'bracelet', 'mask', 'pot']
box_8 = ['flower', 'shorts', 'toy', 'oven']
box_9 = ['ship', 'pants']

# Replace items in Box 1
box_1.remove('boot')
box_1.remove('perfume')
box_1.remove('pen')
box_1.append('game')
box_1.append('scarf')
box_1.append('camera')

# Swap items between Box 6 and Box 9
box_6.remove('motorcycle')
box_9.remove('ship')
box_6.append('ship')
box_9.append('motorcycle')

# Remove items from Box 6
box_6.remove('frame')
box_6.remove('mixer')
box_6.remove('mirror')

# Replace item in Box 5
box_5.remove('wire')
box_5.append('tie')

# Move item from Box 6 to Box 8
box_6.remove('ship')
box_8.append('ship')

# Remove items from Box 7
box_7.remove('storm')
box_7.remove('mask')

# Move items from Box 4 to Box 0
box_4.remove('jungle')
box_4.remove('violin')
box_4.remove('sculpture')
box_0.append('jungle')
box_0.append('violin')
box_0.append('sculpture')

# Move item from Box 9 to Box 4
box_9.remove('motorcycle')
box_4.append('motorcycle')

# Move item from Box 5 to Box 7
box_5.remove('tie')
box_7.append('tie')

# Move item from Box 4 to Box 3
box_4.remove('motorcycle')
box_3.append('motorcycle')

# Replace item in Box 9
box_9.remove('pants')
box_9.append('motorcycle')

# Replace item in Box 1
box_1.remove('camera')
box_1.append('leaf')

# Replace item in Box 2
box_2.remove('comb')
box_2.append('ocean')

# Remove items from Box 8
box_8.remove('oven')
box_8.remove('flower')

# Swap items between Box 2 and Box 1
box_2.remove('flute')
box_1.remove('game')
box_2.append('game')
box_1.append('flute')

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