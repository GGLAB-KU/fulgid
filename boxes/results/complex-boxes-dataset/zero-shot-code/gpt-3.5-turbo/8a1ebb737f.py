box_0 = ['pillow', 'note', 'bell', 'coat']
box_1 = ['earring', 'elephant', 'clock']
box_2 = ['crown', 'fridge', 'freezer']
box_3 = []
box_4 = ['rocket', 'car']
box_5 = ['perfume', 'train', 'dice', 'pants', 'pen']
box_6 = ['jungle', 'console', 'zipper']
box_7 = ['flute', 'lipstick']
box_8 = ['shoe']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the earring and the clock from Box 1 to Box 8
box_8.extend([box_1.pop(box_1.index('earring')), box_1.pop(box_1.index('clock'))])

# Move the clock from Box 8 to Box 7
box_7.append(box_8.pop(box_8.index('clock')))

# Replace the rocket and the car with the shoes and the sculpture in Box 4
box_4 = ['shoes', 'sculpture']

# Move the note and the pillow and the bell from Box 0 to Box 5
box_5.extend([box_0.pop(box_0.index('note')), box_0.pop(box_0.index('pillow')), box_0.pop(box_0.index('bell'))])

# Replace the elephant with the whistle in Box 1
box_1[box_1.index('elephant')] = 'whistle'

# Remove the coat from Box 0
box_0.remove('coat')

# Put the paint and the magnet and the grass into Box 3
box_3.extend(['paint', 'magnet', 'grass'])

# Replace the crown and the fridge and the freezer with the coral and the forest and the table in Box 2
box_2 = ['coral', 'forest', 'table']

# Replace the bell with the basket in Box 5
box_5[box_5.index('bell')] = 'basket'

# Move the shoe and the earring from Box 8 to Box 0
box_0.extend([box_8.pop(box_8.index('shoe')), box_8.pop(box_8.index('earring'))])

# Move the lipstick and the clock and the flute from Box 7 to Box 6
box_6.extend([box_7.pop(box_7.index('lipstick')), box_7.pop(box_7.index('clock')), box_7.pop(box_7.index('flute'))])

# Remove the shoes and the sculpture from Box 4
box_4 = []

# Remove the dice and the basket from Box 5
box_5.remove('dice')
box_5.remove('basket')

# Move the lipstick and the zipper and the console from Box 6 to Box 8
box_8.extend([box_6.pop(box_6.index('lipstick')), box_6.pop(box_6.index('zipper')), box_6.pop(box_6.index('console'))])

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)