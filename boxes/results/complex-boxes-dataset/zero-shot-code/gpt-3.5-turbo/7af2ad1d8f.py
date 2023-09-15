box_0 = []
box_1 = ['bird', 'coin', 'dog', 'speaker']
box_2 = ['scissors', 'flute', 'shark', 'flower', 'candle']
box_3 = ['mirror']
box_4 = []
box_5 = []
box_6 = ['pan', 'pen', 'blanket', 'spoon']
box_7 = ['ocean', 'mountain', 'glove', 'tape', 'ship']
box_8 = ['cow', 'beach', 'drum', 'wire']
box_9 = ['tie', 'cat', 'crown', 'doll', 'vase']
box_10 = ['sculpture', 'gloves', 'motorcycle']
box_11 = ['watch']
box_12 = ['ring', 'swimsuit']
box_13 = ['belt', 'shoes', 'coral']
box_14 = ['dolphin', 'scarf', 'tree']

# Move the blanket, spoon, and pan from Box 6 to Box 11
box_11.extend(box_6.pop(box_6.index('blanket')))
box_11.extend(box_6.pop(box_6.index('spoon')))
box_11.extend(box_6.pop(box_6.index('pan')))

# Remove the tree, dolphin, and scarf from Box 14
box_14.remove('tree')
box_14.remove('dolphin')
box_14.remove('scarf')

# Move the drum from Box 8 to Box 3
box_3.append(box_8.pop(box_8.index('drum')))

# Swap the coin in Box 1 with the spoon in Box 11
box_1[box_1.index('coin')], box_11[box_11.index('spoon')] = box_11[box_11.index('spoon')], box_1[box_1.index('coin')]

# Put the shampoo and microscope into Box 7
box_7.extend(['shampoo', 'microscope'])

# Replace the gloves and sculpture with the glove and leaf in Box 10
box_10[box_10.index('gloves')] = 'glove'
box_10[box_10.index('sculpture')] = 'leaf'

# Put the spoon into Box 8
box_8.append('spoon')

# Remove the tape from Box 7
box_7.remove('tape')

# Move the tie, doll, and cat from Box 9 to Box 6
box_6.extend(box_9.pop(box_9.index('tie')))
box_6.extend(box_9.pop(box_9.index('doll')))
box_6.extend(box_9.pop(box_9.index('cat')))

# Swap the swimsuit in Box 12 with the coral in Box 13
box_12[box_12.index('swimsuit')], box_13[box_13.index('coral')] = box_13[box_13.index('coral')], box_12[box_12.index('swimsuit')]

# Remove the coral from Box 12
box_12.remove('coral')

# Put the piano, laptop, and bracelet into Box 13
box_13.extend(['piano', 'laptop', 'bracelet'])

# Put the blender, key, and bag into Box 13
box_13.extend(['blender', 'key', 'bag'])

# Swap the ring in Box 12 with the bird in Box 1
box_12[box_12.index('ring')], box_1[box_1.index('bird')] = box_1[box_1.index('bird')], box_12[box_12.index('ring')]

# Put the dress into Box 10
box_10.append('dress')

# Put the elephant, sun, and sculpture into Box 0
box_0.extend(['elephant', 'sun', 'sculpture'])

# Put the towel and plate into Box 7
box_7.extend(['towel', 'plate'])

# Put the microscope and bus into Box 8
box_8.extend(['microscope', 'bus'])

# Put the wire into Box 4
box_4.append('wire')

# Move the bus, wire, and cow from Box 8 to Box 12
box_12.extend(box_8.pop(box_8.index('bus')))
box_12.extend(box_8.pop(box_8.index('wire')))
box_12.extend(box_8.pop(box_8.index('cow')))

# Remove the drum and mirror from Box 3
box_3.remove('drum')
box_3.remove('mirror')

# Empty Box 0
box_0 = []

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
print("Box 13:", box_13)
print("Box 14:", box_14)