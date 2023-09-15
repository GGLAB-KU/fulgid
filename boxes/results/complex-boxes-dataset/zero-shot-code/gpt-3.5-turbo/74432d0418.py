box0 = ['dice', 'zipper', 'violin']
box1 = ['fridge']
box2 = ['desert', 'brush', 'shelf', 'candle', 'blender']
box3 = ['octopus', 'paint', 'bird', 'ring', 'truck']
box4 = ['coin', 'lion', 'perfume', 'plane', 'console']

# Move lion from Box 4 to Box 1
box1.append(box4.pop(box4.index('lion')))

# Remove console, plane, and coin from Box 4
box4.remove('console')
box4.remove('plane')
box4.remove('coin')

# Remove perfume from Box 4
box4.remove('perfume')

# Move lion and fridge from Box 1 to Box 3
box3.append(box1.pop(box1.index('lion')))
box3.append(box1.pop(box1.index('fridge')))

# Replace bird, truck, and ring with snow, chair, and bicycle in Box 3
box3.remove('bird')
box3.remove('truck')
box3.remove('ring')
box3.extend(['snow', 'chair', 'bicycle'])

# Put hat into Box 3
box3.append('hat')

# Put glove, rain, and game into Box 1
box1.extend(['glove', 'rain', 'game'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)