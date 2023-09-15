box_0 = ['controller', 'flute', 'dog', 'thunder']
box_1 = ['bowl', 'crown', 'ocean']
box_2 = ['usb', 'oven']
box_3 = []
box_4 = ['storm', 'violin', 'frame', 'coin', 'toothbrush']
box_5 = ['plate']
box_6 = ['console', 'belt', 'lightning']
box_7 = ['flower', 'rain', 'piano', 'planet']
box_8 = []
box_9 = ['pan', 'lock']

# Replace items in Box 1
box_1.remove('bowl')
box_1.remove('crown')
box_1.remove('ocean')
box_1.extend(['plane', 'shark', 'needle'])

# Remove items from Box 9
box_9.remove('pan')
box_9.remove('lock')

# Replace item in Box 5
box_5.remove('plate')
box_5.append('clock')

# Move items from Box 0 to Box 2
box_2.extend(box_0)
box_0.clear()

# Replace items in Box 2
box_2.remove('flute')
box_2.remove('controller')
box_2.remove('dog')
box_2.extend(['apple', 'fork', 'harmonica'])

# Replace item in Box 0
box_0.remove('thunder')
box_0.append('hat')

# Put items in Box 8
box_8.extend(['makeup', 'shirt', 'seaweed'])

# Replace items in Box 4
box_4.clear()
box_4.extend(['laptop', 'shirt', 'bus'])

# Swap items between Box 0 and Box 8
box_0[0], box_8[1] = box_8[1], box_0[0]

# Remove item from Box 5
box_5.remove('clock')

# Replace items in Box 2
box_2.remove('usb')
box_2.remove('oven')
box_2.remove('harmonica')
box_2.extend(['earring', 'shampoo', 'lightning'])

# Remove item from Box 6
box_6.remove('lightning')

# Put item in Box 4
box_4.append('bicycle')

# Move item from Box 4 to Box 2
box_2.append(box_4.pop())

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